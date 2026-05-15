# AGENTS.md

This repository contains modern English Codex skills derived from the first part of José Oiticica's `Manual de Estilo`.

## Workflow

- Use `bd` for task tracking. Run `bd ready`, `bd show <id>`, `bd update <id> --claim`, and `bd close <id> --reason "<evidence>"`.
- Work on a feature branch. Do not implement on `main`.
- Do not push unless the user explicitly asks.
- Do not push directly to `main`.
- Run focused validation before closing tracked work.

## Skill Rules

- Every skill lives under `src/oiticica-*/SKILL.md`.
- Every skill must have `evals/evals.json` with positive and negative eval cases.
- Skill names and directories must use the `oiticica-` prefix.
- Skills must be concise, modern English, and based on one concept from the first part of the manual.
- Apply English grammar, punctuation, morphology, idiom, and prosody. Do not carry Portuguese orthography or grammar into English.
- Prefer shallow, objective rules over long explanation.

## Link Script

`scripts/link_skills.sh` installs only skill directories into Codex and Claude skill homes. It must not link, copy, or install `AGENTS.md` or `CLAUDE.md`.

## Validation

Run:

```bash
python3 -m py_compile scripts/generate_skills.py
python3 scripts/generate_skills.py --check
bash -n scripts/link_skills.sh
```
