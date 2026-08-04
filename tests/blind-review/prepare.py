#!/usr/bin/env python3
"""Build a blinded A/B review packet from two captured skill runs."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
from pathlib import Path


CASE_IDS = ("01", "02", "03", "04", "05", "06")
SECTION_END = re.compile(r"^(?:【(?:打磨报告|改动摘要)】|#{2,6}\s+)")
FINAL_START = re.compile(r"^#{2,6}\s*终稿\s*$")


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    if not path.is_file():
        raise SystemExit(f"missing file: {path}")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_manifest(path: Path) -> dict[str, dict[str, str]]:
    cases: dict[str, dict[str, str]] = {}
    current: dict[str, str] | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        match = re.fullmatch(r"\[([0-9]{2})\]", line)
        if match:
            current = {}
            cases[match.group(1)] = current
            continue
        if current is not None and "=" in line:
            key, value = line.split("=", 1)
            current.setdefault(key, value)
    return cases


def review_text(output: str, mode: str) -> str:
    if mode == "embedded":
        return output.strip()

    lines = output.splitlines()
    start = next((index + 1 for index, line in enumerate(lines) if FINAL_START.match(line)), None)
    if start is None:
        return output.strip()

    selected: list[str] = []
    for line in lines[start:]:
        if SECTION_END.match(line):
            break
        selected.append(line)
    text = "\n".join(selected).strip()
    return text or output.strip()


def require_file(path: Path) -> str:
    if not path.is_file():
        raise SystemExit(f"missing file: {path}")
    return path.read_text(encoding="utf-8").strip()


def build_packet(args: argparse.Namespace) -> None:
    repo_root = Path(__file__).resolve().parents[2]
    manifest = read_manifest(repo_root / "tests/eval-manifest.txt")
    rng = random.Random(args.seed)
    out_dir = args.out_dir.resolve()
    if out_dir.exists() and any(out_dir.iterdir()):
        raise SystemExit(f"output directory is not empty: {out_dir}")
    out_dir.mkdir(parents=True, exist_ok=True)

    review: list[str] = [
        "# qu-ai-wei 人工盲评",
        "",
        "不要查看同目录的 `answer-key.json`，直到所有评分完成。",
        "",
    ]
    candidate_a = set(rng.sample(CASE_IDS, len(CASE_IDS) // 2))
    key: dict[str, object] = {
        "seed": args.seed,
        "provenance": {
            "baseline_skill_sha256": file_sha256(args.baseline_skill),
            "candidate_skill_sha256": file_sha256(args.candidate_skill),
            "model": args.model,
            "settings": args.settings,
        },
        "cases": {},
    }

    for case_id in CASE_IDS:
        case = manifest.get(case_id)
        if not case:
            raise SystemExit(f"manifest missing case {case_id}")
        filename = case.get("file", f"{case_id}-output.md")
        baseline_raw = require_file(args.baseline_dir / filename)
        candidate_raw = require_file(args.candidate_dir / filename)
        baseline = review_text(baseline_raw, case.get("mode", "normal"))
        candidate = review_text(candidate_raw, case.get("mode", "normal"))
        labels = (
            [("candidate", candidate), ("baseline", baseline)]
            if case_id in candidate_a
            else [("baseline", baseline), ("candidate", candidate)]
        )
        fixture = require_file(repo_root / case["fixture"])

        review.extend(
            [
                f"## 案例 {case_id}",
                "",
                f"请求：{case.get('request', '')}",
                "",
                "原文：",
                "",
                fixture,
                "",
            ]
        )
        mapping: dict[str, str] = {}
        hashes: dict[str, str] = {}
        for label, (source, text) in zip(("A", "B"), labels):
            mapping[label] = source
            hashes[label] = sha256(text)
            review.extend([f"### 输出 {label}", "", text, ""])
        review.extend(
            [
                "评分：事实与原意 __/5；语体与声口 __/5；自然度 __/5；克制 __/5",
                "",
                "选择：A / B / 平局",
                "",
                "理由：",
                "",
                "---",
                "",
            ]
        )
        key["cases"][case_id] = {"mapping": mapping, "sha256": hashes}

    (out_dir / "review.md").write_text("\n".join(review), encoding="utf-8")
    (out_dir / "answer-key.json").write_text(
        json.dumps(key, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"wrote {out_dir / 'review.md'}")
    print(f"wrote {out_dir / 'answer-key.json'}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline-dir", type=Path, required=True)
    parser.add_argument("--candidate-dir", type=Path, required=True)
    parser.add_argument("--baseline-skill", type=Path, required=True)
    parser.add_argument("--candidate-skill", type=Path, required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--settings", required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=20260804)
    return parser.parse_args()


if __name__ == "__main__":
    build_packet(parse_args())
