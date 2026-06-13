#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

MANIFEST="$ROOT/tests/eval-manifest.txt"

usage() {
  echo "usage: bash tests/check-runs.sh <run-dir>" >&2
}

if [ "$#" -ne 1 ]; then
  usage
  exit 2
fi

RUN_DIR="$1"
if [ ! -d "$RUN_DIR" ]; then
  echo "run dir not found: $RUN_DIR" >&2
  exit 1
fi

fail() {
  local id="$1"
  local message="$2"
  echo "${id}: ${message}" >&2
  exit 1
}

extract_zhonggao() {
  awk '
    /^## *终稿/ { flag=1; found=1; next }
    /^## / { flag=0 }
    flag { print }
    END { if (found != 1) exit 3 }
  ' "$1"
}

reset_block() {
  file=""
  require_section=()
  require_anywhere=()
  require_final=()
  forbid_final=()
  require_anywhere_fixed=()
  require_final_fixed=()
  forbid_final_fixed=()
}

has_final_assertions() {
  set +u
  local count=$(( \
    ${#require_final[@]} \
    + ${#forbid_final[@]} \
    + ${#require_final_fixed[@]} \
    + ${#forbid_final_fixed[@]} \
  ))
  set -u

  [ "$count" -gt 0 ]
}

check_rg_file() {
  local id="$1"
  local key="$2"
  local pattern="$3"
  local path="$4"

  if ! rg -q -- "$pattern" "$path"; then
    fail "$id" "${key} failed: ${pattern}"
  fi
}

check_fixed_file() {
  local id="$1"
  local key="$2"
  local pattern="$3"
  local path="$4"

  if ! rg -q --fixed-strings -- "$pattern" "$path"; then
    fail "$id" "${key} failed: ${pattern}"
  fi
}

check_rg_text_required() {
  local id="$1"
  local key="$2"
  local pattern="$3"
  local text="$4"

  if ! printf '%s\n' "$text" | rg -q -- "$pattern"; then
    fail "$id" "${key} failed: ${pattern}"
  fi
}

check_rg_text_forbidden() {
  local id="$1"
  local key="$2"
  local pattern="$3"
  local text="$4"

  if printf '%s\n' "$text" | rg -q -- "$pattern"; then
    fail "$id" "${key} matched forbidden pattern: ${pattern}"
  fi
}

check_fixed_text_required() {
  local id="$1"
  local key="$2"
  local pattern="$3"
  local text="$4"

  if ! printf '%s\n' "$text" | rg -q --fixed-strings -- "$pattern"; then
    fail "$id" "${key} failed: ${pattern}"
  fi
}

check_fixed_text_forbidden() {
  local id="$1"
  local key="$2"
  local pattern="$3"
  local text="$4"

  if printf '%s\n' "$text" | rg -q --fixed-strings -- "$pattern"; then
    fail "$id" "${key} matched forbidden string: ${pattern}"
  fi
}

run_block() {
  [ -n "${id:-}" ] || return 0

  local output_file="${file:-${id}-output.md}"
  local output_path="$RUN_DIR/$output_file"
  [ -f "$output_path" ] || fail "$id" "missing output file: $output_path"

  local value
  set +u
  for value in "${require_section[@]}"; do
    check_rg_file "$id" "require_section" "$value" "$output_path"
  done
  for value in "${require_anywhere[@]}"; do
    check_rg_file "$id" "require_anywhere" "$value" "$output_path"
  done
  for value in "${require_anywhere_fixed[@]}"; do
    check_fixed_file "$id" "require_anywhere_fixed" "$value" "$output_path"
  done
  set -u

  if has_final_assertions; then
    local final_text
    if ! final_text="$(extract_zhonggao "$output_path")"; then
      fail "$id" "missing ## 终稿 section for final-section assertions"
    fi

    set +u
    for value in "${require_final[@]}"; do
      check_rg_text_required "$id" "require_final" "$value" "$final_text"
    done
    for value in "${forbid_final[@]}"; do
      check_rg_text_forbidden "$id" "forbid_final" "$value" "$final_text"
    done
    for value in "${require_final_fixed[@]}"; do
      check_fixed_text_required "$id" "require_final_fixed" "$value" "$final_text"
    done
    for value in "${forbid_final_fixed[@]}"; do
      check_fixed_text_forbidden "$id" "forbid_final_fixed" "$value" "$final_text"
    done
    set -u
  fi
}

id=""
reset_block

while IFS= read -r raw_line || [ -n "$raw_line" ]; do
  line="${raw_line%$'\r'}"

  case "$line" in
    ""|\#*) continue ;;
  esac

  if [[ "$line" =~ ^\[[0-9][0-9]\]$ ]]; then
    run_block
    id="${line:1:2}"
    reset_block
    continue
  fi

  [ -n "$id" ] || fail "manifest" "assertion before fixture block: $line"
  if [[ "$line" != *=* ]]; then
    fail "$id" "manifest line missing '=': $line"
  fi

  key="${line%%=*}"
  value="${line#*=}"

  case "$key" in
    file) file="$value" ;;
    require_section) require_section+=("$value") ;;
    require_anywhere) require_anywhere+=("$value") ;;
    require_final) require_final+=("$value") ;;
    forbid_final) forbid_final+=("$value") ;;
    require_anywhere_fixed) require_anywhere_fixed+=("$value") ;;
    require_final_fixed) require_final_fixed+=("$value") ;;
    forbid_final_fixed) forbid_final_fixed+=("$value") ;;
    note) ;;
    *) fail "$id" "unknown manifest key: $key" ;;
  esac
done < "$MANIFEST"

run_block

echo "run check ok: $RUN_DIR"
