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
  README.md
  SKILL.md
  VERSION
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
frontmatter_keys="$(awk '
  NR == 1 && $0 == "---" { active=1; next }
  active && $0 == "---" { exit }
  active && /^[a-z][a-z0-9_-]*:/ { sub(/:.*/, ""); print }
' SKILL.md)"
[ "$frontmatter_keys" = $'name\ndescription' ] || {
  echo "SKILL.md frontmatter must contain only name and description" >&2
  exit 1
}
[ ! -e CONTEXT.md ] || { echo "CONTEXT.md duplicates runtime rules" >&2; exit 1; }
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
grep -q '^## 目录$' references/pattern-catalog.md
grep -q '\[来源与引用边界\](#来源与引用边界)' references/pattern-catalog.md
if grep -Eq '中文直接|中文平台直接' references/pattern-catalog.md; then
  echo "pattern catalog uses evidence labels stronger than the cited feature mapping" >&2
  exit 1
fi
grep -q 'CCL 2023 表 2' references/pattern-catalog.md
grep -q 'CCL 2023 表 4' references/pattern-catalog.md
grep -q '表 6–8' references/pattern-catalog.md
grep -q 'CCL 2025 图 2–3' references/pattern-catalog.md
if ! awk '
  /^### .*｜(中文实证|中文研究启发|跨语言研究启发|平台研究启发)/ && $0 !~ /\]\(https:\/\// {
    print "evidence label missing inline source: " $0 > "/dev/stderr"
    bad=1
  }
  END { exit bad }
' references/pattern-catalog.md; then
  exit 1
fi
grep -q 'assets/demo.gif' README.md
grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+$' VERSION
grep -q '体现了流程优化' references/examples.md
if grep -q '完成了功能更新和流程优化' references/examples.md; then
  echo "examples must not strengthen reflected process optimization into a completed fact" >&2
  exit 1
fi

version="$(tr -d '[:space:]' < VERSION)"
[ -n "$version" ] || { echo "missing VERSION" >&2; exit 1; }

grep -q 'display_name: "去 AI 味"' agents/openai.yaml
grep -q 'short_description: "' agents/openai.yaml
grep -q 'default_prompt: ".*\$qu-ai-wei' agents/openai.yaml

for reference in editing-boundaries examples platform-patterns pattern-catalog brand-voice whitelists; do
  grep -q "references/${reference}.md" SKILL.md || {
    echo "SKILL.md does not route to references/${reference}.md" >&2
    exit 1
  }
done

python3 tests/blind-review/prepare.py --help >/dev/null
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import importlib.util
from pathlib import Path

path = Path("tests/blind-review/prepare.py")
spec = importlib.util.spec_from_file_location("blind_prepare", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
sample = "## 终稿\n正文。\n\n## 需作者确认\n1. 核对。\n\n【打磨报告】\n不进入盲评。"
expected = "正文。\n\n【需作者确认】\n1. 核对。"
if module.review_text(sample, "normal") != expected:
    raise SystemExit("blind review extraction includes process sections")
PY

grep -q '^      - "v\*\.\*\.\*"$' .github/workflows/release.yml
grep -q 'tag .* does not match VERSION' .github/workflows/release.yml
grep -q 'gh release create' .github/workflows/release.yml
grep -q 'bash tests/validate.sh' .github/workflows/validate.yml

bash tests/check-triggers.sh

case_count="$(grep -Ec '^\[[0-9][0-9]\]$' tests/eval-manifest.txt)"
[ "$case_count" -eq 16 ] || { echo "expected 16 eval cases, found $case_count" >&2; exit 1; }

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
