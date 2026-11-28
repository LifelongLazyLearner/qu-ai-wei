"""Validate repository packaging, documentation and regression inventory."""
from __future__ import annotations

import argparse
import re
from collections.abc import Iterator
from pathlib import Path
from urllib.parse import unquote, urlsplit

from .cases import read_cases
from .common import ROOT, EvalError, read_text
from .manifests import read_sections

REQUIRED_FILES = (
    '.github/DISCUSSION_TEMPLATE/show-and-tell.yml',
    '.github/ISSUE_TEMPLATE/bug_report.yml',
    '.github/ISSUE_TEMPLATE/pattern_suggestion.yml',
    '.github/workflows/release.yml',
    '.github/workflows/validate.yml',
    '.gitignore',
    'LICENSE',
    'README.md',
    'SKILL.md',
    'VERSION',
    'agents/openai.yaml',
    'assets/demo.gif',
    'readmes/README.en.md',
    'readmes/README.es.md',
    'readmes/README.ja.md',
    'readmes/README.ko.md',
)
REQUIRED_REFERENCES = {
    'brand-voice.md', 'editing-boundaries.md', 'examples.md',
    'pattern-catalog.md', 'platform-patterns.md', 'whitelists.md',
}
LINK = re.compile(r'\]\(([^\s()]+)\)')


def skill_description(text: str) -> str:
    lines = text.splitlines()
    if not lines or lines[0] != '---' or '---' not in lines[1:]:
        raise EvalError('SKILL.md: missing frontmatter')
    header = lines[1:lines.index('---', 1)]
    fields = [line for line in header if line and not line[0].isspace()]
    if fields != ['name: qu-ai-wei', 'description: |']:
        raise EvalError('SKILL.md frontmatter must contain name: qu-ai-wei and a description block')
    description = '\n'.join(header[header.index('description: |') + 1:])
    if not description.strip():
        raise EvalError('SKILL.md: empty description')
    return description


def check_triggers(description: str, manifest: Path) -> int:
    cases = read_sections(manifest, {'query', 'expect', 'anchor', 'note'})
    for case in cases.values():
        case.single('query')
        if case.single('expect') not in ('TRIGGER', 'EXCLUDE'):
            raise EvalError(f'{case.id}: expected TRIGGER or EXCLUDE')
        anchor = case.single('anchor')
        if anchor not in description:
            raise EvalError(f'{case.id}: description anchor missing: {anchor}')
    return len(cases)


def require_text(text: str, path: str, *anchors: str) -> None:
    for anchor in anchors:
        if anchor not in text:
            raise EvalError(f'{path}: missing contract text: {anchor}')


def local_links(text: str) -> Iterator[str]:
    for link in LINK.findall(text):
        target = urlsplit(link)
        if not (target.scheme or target.netloc) and target.path:
            yield unquote(target.path)


def check_references(root: Path, skill: str) -> None:
    references = {
        path.relative_to(root).as_posix() for path in (root / 'references').rglob('*.md')
    }
    missing = {f'references/{name}' for name in REQUIRED_REFERENCES} - references
    if missing:
        raise EvalError(f'missing required references: {", ".join(sorted(missing))}')
    unrouted = references - {Path(link).as_posix() for link in local_links(skill)}
    if unrouted:
        raise EvalError(f'SKILL.md does not route to: {", ".join(sorted(unrouted))}')

    documents = (
        'SKILL.md', 'README.md', 'tests/README.md', 'tests/blind-review/README.md',
        *sorted(references), *sorted(path.relative_to(root).as_posix() for path in (root / 'readmes').glob('README.*.md')),
    )
    for document in documents:
        path = root / document
        for link in local_links(read_text(path)):
            if not (path.parent / link).exists():
                raise EvalError(f'{document}: broken local link: {link}')


def check_editor_contract(root: Path, skill: str) -> None:
    if (root / 'CONTEXT.md').exists():
        raise EvalError('CONTEXT.md duplicates runtime rules')
    require_text(
        skill, 'SKILL.md', '内嵌模式（embedded mode）', '只输出终稿正文', '敏感信息门检',
        '结构重写', '局部换词', '信息账本', '八个模式族', '全文信息账本',
        '否则一律使用普通模式', '已有可辨识声口（已授权编辑）', '无明确编辑请求',
    )

    catalog_path = 'references/pattern-catalog.md'
    catalog = read_text(root / catalog_path)
    require_text(
        catalog, catalog_path, '旧编号迁移', '表面分析与假揭示', '三连、机械排比与身份升级',
        '开头复述任务与声明计划', '## 目录\n', '[来源与引用边界](#来源与引用边界)',
        'CCL 2023 表 2', 'CCL 2023 表 4', '表 6–8', 'CCL 2025 图 2–3',
    )
    if re.search('中文直接|中文平台直接', catalog):
        raise EvalError(f'{catalog_path}: evidence labels overstate the cited feature mapping')
    evidence_heading = re.compile(r'^### .*｜(中文实证|中文研究启发|跨语言研究启发|平台研究启发)')
    for line in catalog.splitlines():
        if evidence_heading.match(line) and '](https://' not in line:
            raise EvalError(f'{catalog_path}: evidence label missing inline source: {line}')

    examples_path = 'references/examples.md'
    examples = read_text(root / examples_path)
    require_text(examples, examples_path, '体现了流程优化')
    if '完成了功能更新和流程优化' in examples:
        raise EvalError(f'{examples_path}: example strengthens reflected optimization into a completed fact')
    require_text(read_text(root / 'README.md'), 'README.md', 'assets/demo.gif')


def check_package(root: Path, skill: str) -> None:
    for name in REQUIRED_FILES:
        if not (root / name).is_file():
            raise EvalError(f'missing required file: {name}')
    check_references(root, skill)
    check_editor_contract(root, skill)

    metadata_path = 'agents/openai.yaml'
    metadata = read_text(root / metadata_path)
    require_text(metadata, metadata_path, 'display_name: "去 AI 味"', 'short_description: "')
    if not re.search(r'default_prompt: ".*\$qu-ai-wei', metadata):
        raise EvalError(f'{metadata_path}: default prompt must invoke $qu-ai-wei')

    release_path = '.github/workflows/release.yml'
    require_text(read_text(root / release_path), release_path,
                 '- "v*.*.*"', 'does not match VERSION', 'gh release create')
    validate_path = '.github/workflows/validate.yml'
    require_text(read_text(root / validate_path), validate_path, 'bash tests/validate.sh')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--triggers-only', action='store_true')
    args = parser.parse_args()
    skill = read_text(ROOT / 'SKILL.md')
    description = skill_description(skill)
    if not args.triggers_only:
        check_package(ROOT, skill)
        version = read_text(ROOT / 'VERSION').strip()
        if not re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+', version):
            raise EvalError('VERSION must use X.Y.Z')
        cases = read_cases()
        # Keep the reviewed regression inventory while permitting new cases.
        missing = {f'{number:02}' for number in range(1, 21)} - cases.keys()
        if missing:
            raise EvalError(f'missing required regression cases: {", ".join(sorted(missing))}')
        print(f'manifest and fixture checks ok: {len(cases)} cases')
        print(f'package checks ok: qu-ai-wei v{version}')
    triggers = check_triggers(description, ROOT / 'tests/trigger-manifest.txt')
    print(f'trigger and exclusion anchors ok: {triggers}')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError) as exc:
        raise SystemExit(str(exc))
