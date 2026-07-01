#!/usr/bin/env bash
# check-triggers.sh — static description-content guard for the trigger manifest.
#
# Reads the SKILL.md frontmatter `description:` block and asserts that every
# TRIGGER case's `anchor` in tests/trigger-manifest.txt is present verbatim in
# that description. Catches description regressions / typos (e.g. a trigger
# phrase dropped in an edit). This is NOT a behavioral trigger test — that
# requires a non-deterministic model run, which the user runs manually per the
# manifest's `query` / `expect` fields.
#
# Usage: bash tests/check-triggers.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")/.." && pwd)"
cd "$ROOT"

MANIFEST="$ROOT/tests/trigger-manifest.txt"
SKILL="$ROOT/SKILL.md"

[ -f "$MANIFEST" ] || { echo "missing $MANIFEST" >&2; exit 1; }
[ -f "$SKILL" ] || { echo "missing $SKILL" >&2; exit 1; }

# Extract the YAML frontmatter `description:` block (block scalar after the
# `description: |` line, indented until the next top-level key or `---`).
DESC="$(awk '
  /^---$/ { fm++; next }
  fm==1 && /^description:[[:space:]]*\|?[[:space:]]*$/ { indesc=1; next }
  fm==1 && /^[^[:space:]-]/ { indesc=0 }
  indesc { print }
' "$SKILL")"

[ -n "$DESC" ] || { echo "could not extract description block from $SKILL" >&2; exit 1; }

fail() {
  echo "[${1}] ${2}" >&2
  exit 1
}

# Parse the manifest with the same [NN] block + key=value idiom as
# check-runs.sh. For each TRIGGER case, assert its `anchor` is a literal
# substring of the description block.
id=""
anchor=""
expect=""
checked=0

check_case() {
  [ -n "$id" ] || return 0
  [ "$expect" = "TRIGGER" ] || return 0
  [ -n "$anchor" ] || fail "$id" "TRIGGER case missing anchor"
  if ! printf '%s\n' "$DESC" | rg -q --fixed-strings -- "$anchor"; then
    fail "$id" "trigger anchor not found in description: $anchor"
  fi
  checked=$((checked + 1))
}

while IFS= read -r raw_line || [ -n "$raw_line" ]; do
  line="${raw_line%$'\r'}"
  case "$line" in
    ""|\#*) continue ;;
  esac

  if [[ "$line" =~ ^\[[0-9][0-9]\]$ ]]; then
    check_case
    id="${line:1:2}"
    anchor=""
    expect=""
    continue
  fi

  [ -n "$id" ] || fail "manifest" "assertion before case block: $line"
  if [[ "$line" != *=* ]]; then
    fail "$id" "manifest line missing '=': $line"
  fi

  key="${line%%=*}"
  value="${line#*=}"

  case "$key" in
    anchor) anchor="$value" ;;
    expect) expect="$value" ;;
    query|note) ;;
    *) fail "$id" "unknown manifest key: $key" ;;
  esac
done < "$MANIFEST"

check_case

[ "$checked" -ge 1 ] || { echo "no TRIGGER cases found in manifest" >&2; exit 1; }

echo "trigger anchor check ok: $checked TRIGGER case(s) anchored in description"
