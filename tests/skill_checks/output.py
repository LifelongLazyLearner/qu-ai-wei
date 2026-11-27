"""Extract text according to the regression and A/B review contracts."""
from __future__ import annotations

import re

SECTION_END = re.compile(r"^(?:【(?:打磨报告|需作者确认|改动摘要)】|#{1,6}\s*(?:打磨报告|需作者确认|改动摘要|自审)\s*)$")
CONFIRMATION_START = re.compile(r"^(?:【需作者确认】|#{1,6}\s*需作者确认\s*)$")
REPORT_START = re.compile(r"^(?:【(?:打磨报告|改动摘要)】|#{1,6}\s*(?:打磨报告|改动摘要|自审)\s*)$")
FINAL_START = re.compile(r"^(?:#{2,6}\s*)?终稿\s*$")


def review_text(output: str, mode: str) -> str:
    if mode == "embedded":
        return output.strip()

    lines = output.splitlines()
    start = next((index + 1 for index, line in enumerate(lines) if FINAL_START.match(line)), None)
    if start is None:
        return output.strip()

    selected: list[str] = []
    for line in lines[start:]:
        if SECTION_END.match(line):
            break
        selected.append(line)
    confirmation: list[str] = []
    confirmation_start = next((index for index, line in enumerate(lines) if CONFIRMATION_START.match(line)), None)
    if confirmation_start is not None:
        confirmation.append("【需作者确认】")
        for line in lines[confirmation_start + 1 :]:
            if REPORT_START.match(line):
                break
            confirmation.append(line)
    parts = ["\n".join(selected).strip()]
    if confirmation:
        parts.append("\n".join(confirmation).strip())
    text = "\n\n".join(part for part in parts if part)
    return text or output.strip()


CHECK_FINAL_START = re.compile(r"^(?:#{2,6}[^\S\n]*)?终稿[^\S\n]*$")
CHECK_FINAL_END = re.compile(r"^【(?:打磨报告|需作者确认|改动摘要)】")


def check_final(output: str) -> str | None:
    """Match the historical run checker, including its required final heading."""
    selected = []
    active = found = False
    for line in output.split("\n"):
        if CHECK_FINAL_START.match(line):
            active = found = True
        elif active and CHECK_FINAL_END.match(line):
            active = False
        elif active:
            selected.append(line)
    return "\n".join(selected).rstrip("\n") if found else None
