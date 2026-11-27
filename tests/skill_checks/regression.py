"""Check a captured run using the repository's existing fixed and POSIX ERE rules."""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from .cases import Case, read_cases
from .common import EvalError, read_text
from .output import check_final

FAILURES = {
    ("require", "fixed"): "missing",
    ("forbid", "fixed"): "contains forbidden text",
    ("require", "regex"): "missing pattern",
    ("forbid", "regex"): "matches forbidden pattern",
}


def check(case: Case, output: Path) -> None:
    if not output.is_file():
        raise EvalError(f"{case.id}: missing output {output}")
    scopes = {"output": read_text(output)}
    for assertion in case.assertions:
        action, scope, kind = assertion.key.split("_")
        if scope not in scopes:
            final = check_final(scopes["output"])
            if final is None:
                raise EvalError(f"{case.id}: missing 终稿 section")
            scopes["final"] = final + "\n"
        # Use grep so existing POSIX expressions keep exactly the same dialect.
        option = "-Fq" if kind == "fixed" else "-Eq"
        result = subprocess.run(
            ["grep", option, "--", assertion.value],
            input=scopes[scope].encode("utf-8"),
        ).returncode
        if result not in (0, 1):
            raise EvalError(f"{case.id}: invalid {kind} assertion: {assertion.value}")
        if (result == 0) != (action == "require"):
            message = FAILURES[action, kind]
            raise EvalError(f"{case.id}: {scope} {message}: {assertion.value}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_directory", type=Path)
    parser.add_argument("case_ids", nargs="*")
    args = parser.parse_args()
    if not args.run_directory.is_dir():
        parser.error("run_directory must be an existing directory")
    cases = read_cases()
    selected = set(args.case_ids) if args.case_ids else cases.keys()
    if args.case_ids and (len(selected) != len(args.case_ids) or selected - cases.keys()):
        raise EvalError("one or more selected eval cases were not found or were repeated")
    for case_id, case in cases.items():
        if case_id in selected:
            check(case, args.run_directory / case.output_file)
    print(f"captured run checks ok: {args.run_directory}")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as exc:
        raise SystemExit(str(exc))
