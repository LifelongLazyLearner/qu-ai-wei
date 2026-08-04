#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

description="$(awk '
  /^---$/ { frontmatter++; next }
  frontmatter == 1 && /^description:[[:space:]]*\|[[:space:]]*$/ { active=1; next }
  frontmatter == 1 && active && /^[^[:space:]]/ { active=0 }
  active { print }
' SKILL.md)"

[ -n "$description" ] || { echo "could not read SKILL.md description" >&2; exit 1; }

id=""
anchor=""
expect=""
checked=0

check_case() {
  [ -n "$id" ] || return 0
  case "$expect" in
    TRIGGER|EXCLUDE) ;;
    *) return 0 ;;
  esac
  [ -n "$anchor" ] || { echo "$id: missing description anchor" >&2; exit 1; }
  printf '%s\n' "$description" | grep -Fq -- "$anchor" || {
    echo "$id: description anchor missing: $anchor" >&2
    exit 1
  }
  checked=$((checked + 1))
}

while IFS= read -r line || [ -n "$line" ]; do
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
  key="${line%%=*}"
  value="${line#*=}"
  case "$key" in
    anchor) anchor="$value" ;;
    expect) expect="$value" ;;
    query|note) ;;
    *) echo "$id: unknown trigger key: $key" >&2; exit 1 ;;
  esac
done < tests/trigger-manifest.txt

check_case
[ "$checked" -gt 0 ] || { echo "no trigger cases checked" >&2; exit 1; }
echo "trigger and exclusion anchors ok: $checked"
