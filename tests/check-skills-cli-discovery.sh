#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

OUT="$(mktemp)"
trap 'rm -f "$OUT"' EXIT

if ! npx --yes skills@1.5.13 add . --list >"$OUT" 2>&1; then
  cat "$OUT" >&2
  echo "skills CLI discovery failed" >&2
  exit 1
fi

if ! rg -q --fixed-strings "Found 1 skill" "$OUT"; then
  cat "$OUT" >&2
  echo "skills CLI did not report exactly one discovered skill" >&2
  exit 1
fi

if ! rg -q "qu-ai-wei[[:space:]]*$" "$OUT"; then
  cat "$OUT" >&2
  echo "skills CLI did not list qu-ai-wei" >&2
  exit 1
fi

echo "skills CLI discovery ok: qu-ai-wei"
