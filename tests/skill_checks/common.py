"""Paths and byte-preserving reads shared by the development checks."""
from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class EvalError(ValueError):
    pass


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_text(path: Path) -> str:
    # Preserve CRLF and all code points for literal protection and span offsets.
    return path.read_bytes().decode('utf-8')
