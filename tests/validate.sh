#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [ "$#" -gt 1 ] || { [ "$#" -eq 1 ] && [ "$1" != "--local" ]; }; then
  echo "usage: bash tests/validate.sh [--local]" >&2
  exit 2
fi

PYTHONPATH=tests python3 -m skill_checks.package
bash tests/check-runs.sh --help >/dev/null
python3 tests/blind-review/prepare.py --help >/dev/null
python3 -m unittest discover -s tests -p 'test_*.py'

if [ "${1:-}" != "--local" ]; then
  output="$(mktemp)"
  trap 'rm -f "$output"' EXIT
  if ! npx --yes skills@1.5.13 add . --list -a codex >"$output" 2>&1; then
    cat "$output" >&2
    echo "skills CLI discovery failed" >&2
    exit 1
  fi
  plain_output="$(LC_ALL=C sed $'s/\033\\[[0-9;?]*[ -\\/]*[@-~]//g' "$output")"
  if ! grep -Fq 'Found 1 skill' <<<"$plain_output" || ! grep -Fq 'qu-ai-wei' <<<"$plain_output"; then
    cat "$output" >&2
    echo "skills CLI did not discover qu-ai-wei" >&2
    exit 1
  fi
else
  echo "skills CLI discovery skipped (--local)"
fi

git diff --check
git diff --cached --check

echo "validation ok"
