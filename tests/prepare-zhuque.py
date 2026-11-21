#!/usr/bin/env python3
"""Prepare the three-way Zhuque smoke comparison from two Git revisions."""

import argparse
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ("01", "02", "03")
REQUEST = (
    "把这篇简体中文创作者稿改得自然些，适合普通中文读者。"
    "保留原有事实、判断、证据强度和引用，不补造材料，不向作者索取新材料。只输出终稿正文。"
)


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def snapshot(ref):
    commit = git("rev-parse", "--verify", "--end-of-options", f"{ref}^{{commit}}").decode().strip()
    resources = git("ls-tree", "-rz", "--name-only", commit, "--", "references").decode().split("\0")
    paths = ["SKILL.md", *(p for p in resources if p.endswith(".md"))]
    return commit, {path: git("show", f"{commit}:{path}") for path in paths}


def digest(content):
    return hashlib.sha256(content).hexdigest()


def prepare(out, baseline, candidate):
    raw = (ROOT / "tests/zhuque-smoke.md").read_text()
    sources = dict(re.findall(r"^### (0[1-3])A 原稿\n\n(.*?)(?=^### )", raw, re.M | re.S))
    if tuple(sources) != CASES:
        raise ValueError("expected original drafts 01A, 02A and 03A in tests/zhuque-smoke.md")
    versions = {"baseline": snapshot(baseline), "candidate": snapshot(candidate)}
    if versions["baseline"][1] == versions["candidate"][1]:
        raise ValueError("the two skill bundles are identical")
    out.mkdir(parents=True, exist_ok=False)
    (out / "originals").mkdir()
    manifest = {
        "versions": {
            variant: {"commit": commit, "sha256": {p: digest(b) for p, b in files.items()}}
            for variant, (commit, files) in versions.items()
        },
        "sources": {},
        "requests": {},
    }
    for case, content in sources.items():
        source = content.strip()
        manifest["sources"][case] = digest(source.encode())
        (out / "originals" / f"{case}.txt").write_text(source + "\n")
        for variant in ("prompt", *versions):
            label = f"{variant}-{case}"
            session = out / "sessions" / label
            session.mkdir(parents=True)
            if variant in versions:
                for path, data in versions[variant][1].items():
                    target = session / path
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(data)
                setup = "先读取当前目录的 SKILL.md，按其流程处理以下请求。按该版本的要求读取参考文件。"
            else:
                setup = "只使用本请求和下方正文，无需读取外部文件或加载写作 skill。"
            request = f"{setup}\n\n{REQUEST}\n\n<待编辑正文>\n{source}\n</待编辑正文>\n"
            (session / "request.txt").write_text(request)
            manifest["requests"][label] = digest(request.encode())

    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    with (out / "results.csv").open("w", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        writer.writerow(("case", "version", "fidelity", "reader_preference", "detector_result", "checked_at", "notes"))
        for case in CASES:
            for variant in ("original", "prompt", "baseline", "candidate"):
                writer.writerow((case, variant, "", "", "", "", ""))
        writer.writerow(("04", "human_control", "", "", "", "", "See tests/zhuque-smoke.md"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", required=True, help="Git revision of the corrected skill")
    parser.add_argument("--candidate", required=True, help="Git revision of the four-step skill")
    parser.add_argument("--out-dir", required=True, type=Path, help="New directory outside the repository")
    args = parser.parse_args()
    out = args.out_dir.resolve()
    if out.is_relative_to(ROOT):
        parser.error("use an output directory outside the repository to isolate model sessions")
    try:
        prepare(out, args.baseline, args.candidate)
    except (subprocess.CalledProcessError, FileExistsError, ValueError) as exc:
        parser.error(str(exc))
    print(out)


if __name__ == "__main__":
    main()
