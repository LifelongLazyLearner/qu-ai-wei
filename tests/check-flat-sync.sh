#!/usr/bin/env bash
# check-flat-sync.sh — flat-build determinism guard.
#
# What this catches:
#   Someone edits SKILL.md or references/ and FORGETS to re-run
#   scripts/build-flat.sh, so the committed .cursorrules / WARP.md drift out of
#   sync with the source. check-version-sync.sh only checks version *strings*;
#   it does NOT diff flat-build content. This test closes that gap.
#
# How it works:
#   1. Copy SKILL.md + references/ + scripts/ into a temp dir.
#   2. Run build-flat.sh there (it resolves DIR relative to its own path, so it
#      regenerates inside the temp dir without touching the working tree).
#   3. Diff the temp-generated .cursorrules / WARP.md against the committed ones.
#      Byte-identical = in sync.
#
# A failure means: either re-run `bash scripts/build-flat.sh` and commit the
# regenerated files, OR (if the diff is intentional) investigate why the build
# is no longer deterministic.
#
# Usage: bash tests/check-flat-sync.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")/.." && pwd)"
cd "$ROOT"

BUILD="$ROOT/scripts/build-flat.sh"
[ -f "$BUILD" ] || { echo "missing $BUILD" >&2; exit 1; }

# Source files the flat build reads from.
SOURCES=(SKILL.md references/ scripts/build-flat.sh)
for s in "${SOURCES[@]}"; do
  [ -e "$ROOT/$s" ] || { echo "missing source: $s" >&2; exit 1; }
done

# Committed flat files we validate against.
[ -f "$ROOT/.cursorrules" ] || { echo "missing committed .cursorrules" >&2; exit 1; }
[ -f "$ROOT/WARP.md" ] || { echo "missing committed WARP.md" >&2; exit 1; }

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

# Copy only the inputs the build needs. Keeping the temp tree minimal avoids
# accidentally picking up local-only files (.claude/, docs/superpowers/, etc.).
mkdir -p "$WORK/references" "$WORK/scripts"
cp "$ROOT/SKILL.md" "$WORK/SKILL.md"
cp "$ROOT/references/"*.md "$WORK/references/"
cp "$ROOT/scripts/build-flat.sh" "$WORK/scripts/build-flat.sh"

# Regenerate inside the temp dir. build-flat.sh resolves DIR from its own
# BASH_SOURCE, so it writes $WORK/.cursorrules and $WORK/WARP.md.
bash "$WORK/scripts/build-flat.sh" >/dev/null

fail() {
  local file="$1"
  echo "flat-build out of sync: $file" >&2
  echo "committed file does not match a fresh build from SKILL.md + references/" >&2
  echo "" >&2
  echo "fix: bash scripts/build-flat.sh && git add .cursorrules WARP.md" >&2
  echo "" >&2
  echo "diff (committed  <  >  fresh build):" >&2
  diff -- "$ROOT/$file" "$WORK/$file" >&2 || true
  exit 1
}

cmp -s "$ROOT/.cursorrules" "$WORK/.cursorrules" || fail ".cursorrules"
cmp -s "$ROOT/WARP.md" "$WORK/WARP.md" || fail "WARP.md"

echo "flat sync ok: .cursorrules / WARP.md match a fresh build from SKILL.md + references/"
