#!/usr/bin/env python3
"""Command-line entry point for A/B blind review."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from skill_checks.review import main

if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as exc:
        raise SystemExit(str(exc))
