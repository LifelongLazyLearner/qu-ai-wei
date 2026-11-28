"""Load the shared evaluation inventory for the run checker and A/B review."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .common import ROOT, EvalError
from .manifests import read_sections

MANIFEST = ROOT / "tests/eval-manifest.txt"
# Preserve the historical order in which the run checker reports failures.
CHECK_KEYS = tuple(
    f"{action}_{scope}_{kind}"
    for scope in ("output", "final")
    for kind in ("fixed", "regex")
    for action in ("require", "forbid")
)
META_KEYS = {"fixture", "file", "mode", "request", "note"}


@dataclass(frozen=True)
class Assertion:
    key: str
    value: str


@dataclass(frozen=True)
class Case:
    id: str
    fixture: Path
    output_file: str
    mode: str
    request: str
    assertions: tuple[Assertion, ...]


def read_cases(path: Path = MANIFEST) -> dict[str, Case]:
    cases = {}
    for case_id, section in read_sections(path, META_KEYS | set(CHECK_KEYS)).items():
        fixture = ROOT / section.single("fixture")
        if not fixture.is_file():
            raise EvalError(f"{case_id}: missing eval fixture: {fixture}")
        cases[case_id] = Case(
            id=case_id,
            fixture=fixture,
            output_file=section.single("file"),
            mode=section.single("mode"),
            request=section.single("request"),
            assertions=tuple(
                Assertion(key, value)
                for key in CHECK_KEYS
                for value in section.many(key)
            ),
        )
    return cases
