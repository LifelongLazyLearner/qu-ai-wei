#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

required=(
  .github/DISCUSSION_TEMPLATE/show-and-tell.yml
  .github/ISSUE_TEMPLATE/bug_report.yml
  .github/ISSUE_TEMPLATE/pattern_suggestion.yml
  .github/workflows/release.yml
  .github/workflows/validate.yml
  .gitignore
  LICENSE
  CONTEXT.md
  README.md
  SKILL.md
  agents/openai.yaml
  assets/demo.gif
  readmes/README.en.md
  readmes/README.es.md
  readmes/README.ja.md
  readmes/README.ko.md
  references/brand-voice.md
  references/editing-boundaries.md
  references/examples.md
  references/platform-patterns.md
  references/pattern-catalog.md
  references/whitelists.md
  tests/README.md
  tests/blind-review/README.md
  tests/blind-review/prepare.py
  tests/check-runs.sh
  tests/check-triggers.sh
  tests/eval-manifest.txt
  tests/trigger-manifest.txt
)

for file in "${required[@]}"; do
  [ -f "$file" ] || { echo "missing required file: $file" >&2; exit 1; }
done

grep -q '^name: qu-ai-wei$' SKILL.md
grep -q '^description: |$' SKILL.md
grep -q '内嵌模式（embedded mode）' SKILL.md
grep -q '只输出终稿正文' SKILL.md
grep -q '否则一律使用普通模式' SKILL.md
grep -q '敏感信息门检' SKILL.md
grep -q '结构重写' SKILL.md
grep -q '局部换词' SKILL.md
grep -q '信息账本' SKILL.md
grep -q '真人文本（已授权改写）' SKILL.md
grep -q '八个模式族' SKILL.md
grep -q '全文信息账本' SKILL.md
grep -q '旧编号迁移' references/pattern-catalog.md
grep -q '表面分析与假揭示' references/pattern-catalog.md
grep -q '三连、机械排比与身份升级' references/pattern-catalog.md
grep -q '开头复述任务与声明计划' references/pattern-catalog.md
if ! awk '
  /^### .*｜(中文直接|跨语言|中文平台直接)/ && $0 !~ /\]\(https:\/\// {
    print "evidence label missing inline source: " $0 > "/dev/stderr"
    bad=1
  }
  END { exit bad }
' references/pattern-catalog.md; then
  exit 1
fi
grep -q 'assets/demo.gif' README.md

version="$(sed -n 's/^  version: "\([^"]*\)"$/\1/p' SKILL.md)"
[ -n "$version" ] || { echo "missing metadata.version in SKILL.md" >&2; exit 1; }

grep -q 'display_name: "去 AI 味"' agents/openai.yaml
grep -q 'short_description: "' agents/openai.yaml
grep -q 'default_prompt: ".*\$qu-ai-wei' agents/openai.yaml

for reference in editing-boundaries examples platform-patterns pattern-catalog brand-voice whitelists; do
  grep -q "references/${reference}.md" SKILL.md || {
    echo "SKILL.md does not route to references/${reference}.md" >&2
    exit 1
  }
done
grep -Fq '[`CONTEXT.md`](CONTEXT.md)' SKILL.md

python3 tests/blind-review/prepare.py --help >/dev/null

grep -q '^      - "v\*\.\*\.\*"$' .github/workflows/release.yml
grep -q 'tag .* does not match SKILL.md version' .github/workflows/release.yml
grep -q 'gh release create' .github/workflows/release.yml
grep -q 'bash tests/validate.sh' .github/workflows/validate.yml

bash tests/check-triggers.sh

case_count="$(grep -Ec '^\[[0-9][0-9]\]$' tests/eval-manifest.txt)"
[ "$case_count" -eq 15 ] || { echo "expected 15 eval cases, found $case_count" >&2; exit 1; }

while IFS='=' read -r key value; do
  [ "$key" = "fixture" ] || continue
  [ -f "$value" ] || { echo "missing eval fixture: $value" >&2; exit 1; }
done < tests/eval-manifest.txt

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

git diff --check
git diff --cached --check

echo "validation ok: qu-ai-wei v$version"
