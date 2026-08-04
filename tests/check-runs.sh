#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [ "$#" -ne 1 ] || [ ! -d "$1" ]; then
  echo "usage: bash tests/check-runs.sh <run-directory>" >&2
  exit 2
fi

RUN_DIR="$1"
id=""
file=""
require_output_fixed=()
forbid_output_fixed=()
require_output_regex=()
forbid_output_regex=()
require_final_fixed=()
forbid_final_fixed=()

reset_case() {
  file=""
  require_output_fixed=()
  forbid_output_fixed=()
  require_output_regex=()
  forbid_output_regex=()
  require_final_fixed=()
  forbid_final_fixed=()
}

extract_final() {
  awk '
    /^#{2,6}[[:space:]]*终稿/ { active=1; found=1; next }
    active && /^【(打磨报告|改动摘要)】/ { active=0; next }
    /^#{2,6}[[:space:]]/ { active=0 }
    active { print }
    END { if (found != 1) exit 3 }
  ' "$1"
}

check_case() {
  [ -n "$id" ] || return 0
  output="$RUN_DIR/${file:-${id}-output.md}"
  [ -f "$output" ] || { echo "$id: missing output $output" >&2; exit 1; }

  set +u
  for value in "${require_output_fixed[@]}"; do
    grep -Fq -- "$value" "$output" || { echo "$id: output missing: $value" >&2; exit 1; }
  done
  for value in "${forbid_output_fixed[@]}"; do
    if grep -Fq -- "$value" "$output"; then
      echo "$id: output contains forbidden text: $value" >&2
      exit 1
    fi
  done
  for value in "${require_output_regex[@]}"; do
    grep -Eq -- "$value" "$output" || { echo "$id: output missing pattern: $value" >&2; exit 1; }
  done
  for value in "${forbid_output_regex[@]}"; do
    if grep -Eq -- "$value" "$output"; then
      echo "$id: output matches forbidden pattern: $value" >&2
      exit 1
    fi
  done
  final_check_count=$(( ${#require_final_fixed[@]} + ${#forbid_final_fixed[@]} ))
  set -u

  if [ "$final_check_count" -gt 0 ]; then
    final="$(extract_final "$output")" || { echo "$id: missing 终稿 section" >&2; exit 1; }
    set +u
    for value in "${require_final_fixed[@]}"; do
      grep -Fq -- "$value" <<<"$final" || { echo "$id: final missing: $value" >&2; exit 1; }
    done
    for value in "${forbid_final_fixed[@]}"; do
      if grep -Fq -- "$value" <<<"$final"; then
        echo "$id: final contains forbidden text: $value" >&2
        exit 1
      fi
    done
    set -u
  fi
}

while IFS= read -r line || [ -n "$line" ]; do
  case "$line" in
    ""|\#*) continue ;;
  esac
  if [[ "$line" =~ ^\[[0-9][0-9]\]$ ]]; then
    check_case
    id="${line:1:2}"
    reset_case
    continue
  fi
  key="${line%%=*}"
  value="${line#*=}"
  case "$key" in
    file) file="$value" ;;
    require_output_fixed) require_output_fixed+=("$value") ;;
    forbid_output_fixed) forbid_output_fixed+=("$value") ;;
    require_output_regex) require_output_regex+=("$value") ;;
    forbid_output_regex) forbid_output_regex+=("$value") ;;
    require_final_fixed) require_final_fixed+=("$value") ;;
    forbid_final_fixed) forbid_final_fixed+=("$value") ;;
    fixture|mode|request|note) ;;
    *) echo "$id: unknown eval key: $key" >&2; exit 1 ;;
  esac
done < tests/eval-manifest.txt

check_case
echo "captured run checks ok: $RUN_DIR"
