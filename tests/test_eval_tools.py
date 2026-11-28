"""Regression tests for the captured-output and A/B review entry points."""
import argparse
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from skill_checks.cases import read_cases
from skill_checks.common import EvalError
from skill_checks.output import review_text
from skill_checks.regression import check
from skill_checks.review import build_packet


class EvalToolsTests(unittest.TestCase):
    def test_review_keeps_confirmation_but_omits_report(self):
        raw = "## 终稿\n正文。\n\n## 需作者确认\n1. 核对。\n\n【打磨报告】\n不进入盲评。"
        self.assertEqual(review_text(raw, "normal"), "正文。\n\n【需作者确认】\n1. 核对。")
        self.assertEqual(review_text(raw, "embedded"), raw)

    def test_assertions_keep_output_and_final_scopes(self):
        case = read_cases()["09"]
        raw = "## 终稿\n撤销尚未结算的授权，并非退款。银行通常在三个工作日内恢复可用额度。\n【打磨报告】\n银行。\n"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / case.output_file
            path.write_text(raw, encoding="utf-8")
            check(case, path)
            path.write_text(raw.replace("银行通常", "通常"), encoding="utf-8")
            with self.assertRaisesRegex(EvalError, "final missing: 银行"):
                check(case, path)

    def test_packet_write_failure_leaves_no_partial_artifacts(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = argparse.Namespace(
                baseline_dir=root, candidate_dir=root,
                baseline_skill=root / "baseline.md", candidate_skill=root / "candidate.md",
                model="test", settings="test", out_dir=root / "review", seed=7, cases=["01"],
            )
            args.out_dir.mkdir()
            for path in (args.baseline_skill, args.candidate_skill, root / "01-output.md"):
                path.write_text("正文。", encoding="utf-8")
            write_text = Path.write_text

            def fail_key(path, *values, **options):
                if path.name == "answer-key.json":
                    raise OSError("simulated write failure")
                return write_text(path, *values, **options)

            cases = read_cases()
            with patch.object(Path, "write_text", fail_key), self.assertRaises(OSError):
                build_packet(args, cases)
            self.assertEqual(list(args.out_dir.iterdir()), [])
            self.assertEqual(list(root.glob(".review-*")), [])

            build_packet(args, cases)
            self.assertEqual(
                {path.name for path in args.out_dir.iterdir()},
                {"review.md", "answer-key.json"},
            )
            with self.assertRaisesRegex(SystemExit, "output directory is not empty"):
                build_packet(args, cases)
