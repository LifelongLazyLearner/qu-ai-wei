# tests/runs/

This directory is for real captured model outputs. Keep `tests/after/` as the human-written anchor set; put actual model runs here only when they were generated in a clean session and include metadata.

## Directory format

Use one directory per captured run:

```text
tests/runs/v0.7.1-gpt-5-2026-06-13/
```

Each output file should match the fixture id:

```text
01-output.md
02-output.md
...
17-output.md
```

## Required metadata

Put this header at the top of every captured output before the model response:

```markdown
<!--
model: <model name>
skill_version: <SKILL.md version>
capture_date: YYYY-MM-DD
prompt_shape: clean session, read SKILL.md + relevant references, then process one fixture
fixture: tests/fixtures/NN-name.md
-->
```

Do not commit copied anchor outputs as model runs. If the output was hand-edited, store it in `tests/after/` or another anchor location, not here.

## Capture workflow

1. Start a clean model session.
2. Load `SKILL.md` and the relevant `references/` files the skill asks for.
3. Paste one `tests/fixtures/NN-*.md` input and ask the model to run qu-ai-wei.
4. Save the raw response, including the metadata header, as `tests/runs/<run-dir>/NN-output.md`.
5. Validate the run:

```bash
bash tests/check-runs.sh tests/runs/<run-dir>
```

For compatibility, the same checker can validate the anchor set:

```bash
bash tests/check-runs.sh tests/after
```
