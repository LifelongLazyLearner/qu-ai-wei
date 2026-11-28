"""Parse the section syntax shared by evaluation cases and trigger anchors."""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .common import EvalError, read_text


@dataclass
class Section:
    id: str
    fields: dict[str, list[str]]

    def single(self, key: str) -> str:
        values = self.fields.get(key, [])
        if len(values) != 1:
            raise EvalError(f'{self.id}: expected one {key}')
        return values[0]

    def many(self, key: str) -> tuple[str, ...]:
        return tuple(self.fields.get(key, ()))


def read_sections(path: Path, allowed_keys: set[str], *, content: str | None = None) -> dict[str, Section]:
    sections = {}
    current = None
    if content is None:
        content = read_text(path)
    for number, raw in enumerate(content.splitlines(), 1):
        if not raw or raw.startswith('#'):
            continue
        match = re.fullmatch(r'\[([0-9]{2})\]', raw)
        if match:
            section_id = match[1]
            if section_id in sections:
                raise EvalError(f'{path}:{number}: duplicate case {section_id}')
            current = sections[section_id] = Section(section_id, {})
            continue
        if current is None or '=' not in raw:
            raise EvalError(f'{path}:{number}: invalid manifest line')
        key, value = raw.split('=', 1)
        if key not in allowed_keys or not value:
            raise EvalError(f'{path}:{number}: invalid key/value {key}')
        current.fields.setdefault(key, []).append(value)
    if not sections:
        raise EvalError(f'{path}: empty manifest')
    return sections
