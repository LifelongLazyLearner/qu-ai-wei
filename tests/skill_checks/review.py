"""Build the existing A/B review packet from two captured skill runs."""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from tempfile import TemporaryDirectory

from .cases import Case, read_cases
from .common import digest
from .output import review_text

EXCLUDED_CASE_IDS = {"07"}  # Credential fixture stays out of review packets.


def file_sha256(path: Path) -> str:
    if not path.is_file():
        raise SystemExit(f"missing file: {path}")
    return digest(path.read_bytes())


def require_file(path: Path) -> str:
    if not path.is_file():
        raise SystemExit(f"missing file: {path}")
    return path.read_text(encoding="utf-8").strip()


def build_packet(args: argparse.Namespace, manifest: dict[str, Case]) -> None:
    rng = random.Random(args.seed)
    out_dir = args.out_dir.resolve()
    if out_dir.exists() and any(out_dir.iterdir()):
        raise SystemExit(f"output directory is not empty: {out_dir}")

    review: list[str] = [
        "# qu-ai-wei 人工盲评",
        "",
        "不要查看同目录的 `answer-key.json`，直到所有评分完成。",
        "",
    ]
    case_ids = args.cases
    candidate_a = set(rng.sample(case_ids, len(case_ids) // 2))
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

    for case_id in case_ids:
        case = manifest.get(case_id)
        if not case:
            raise SystemExit(f"manifest missing case {case_id}")
        filename = case.output_file
        baseline_raw = require_file(args.baseline_dir / filename)
        candidate_raw = require_file(args.candidate_dir / filename)
        baseline = review_text(baseline_raw, case.mode)
        candidate = review_text(candidate_raw, case.mode)
        labels = (
            [("candidate", candidate), ("baseline", baseline)]
            if case_id in candidate_a
            else [("baseline", baseline), ("candidate", candidate)]
        )
        fixture = require_file(case.fixture)

        review.extend(
            [
                f"## 案例 {case_id}",
                "",
                f"请求：{case.request}",
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
            hashes[label] = digest(text.encode("utf-8"))
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

    out_dir.parent.mkdir(parents=True, exist_ok=True)
    # Move both artifacts into place together and reject concurrent overwrites.
    with TemporaryDirectory(prefix=".review-", dir=out_dir.parent) as stage:
        staged = Path(stage)
        (staged / "review.md").write_text("\n".join(review), encoding="utf-8")
        (staged / "answer-key.json").write_text(
            json.dumps(key, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        staged.rename(out_dir)
    print(f"wrote {out_dir / 'review.md'}")
    print(f"wrote {out_dir / 'answer-key.json'}")


def parse_args(case_ids: tuple[str, ...]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline-dir", type=Path, required=True)
    parser.add_argument("--candidate-dir", type=Path, required=True)
    parser.add_argument("--baseline-skill", type=Path, required=True)
    parser.add_argument("--candidate-skill", type=Path, required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--settings", required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=20260804)
    parser.add_argument("--cases", nargs="+", choices=case_ids, default=case_ids)
    return parser.parse_args()


def main() -> None:
    cases = read_cases()
    case_ids = tuple(case_id for case_id in cases if case_id not in EXCLUDED_CASE_IDS)
    build_packet(parse_args(case_ids), cases)
