# Contributing

This repository converts concepts from José Oiticica’s *Manual de Estilo* into
modern English [Codex](https://developers.openai.com/codex/cli) skills.

The source of truth for generated skill files is `scripts/generate_skills.py`.
Edit that script when adding or changing generated skill content. Do not hand
edit generated `SKILL.md`, `evals/evals.yaml`, `agents/openai.yaml`, or
`agents/notes.md` files unless you are also changing the generator so the edit
is reproducible.

`README.md` is hand edited. Keep every generated skill linked in its skill
catalogue; `python3 scripts/generate_skills.py --check` validates that coverage.

## Add or Change a Skill

1. Add or update the concept entry in `scripts/generate_skills.py`.
2. Keep the skill name prefixed with `oiticica-`.
3. Use modern English grammar, spelling, idiom, punctuation, and prosody.
4. Keep rules shallow and objective.
5. Regenerate the files:

```bash
python3 scripts/generate_skills.py
```

6. Add the skill to `README.md` under the relevant taxonomy group.

## Examples and Evals

Use public-domain English classics or civic texts for positive examples, such
as Shakespeare, the Federalist Papers, Austen, Dickens, Milton, Lincoln, or
other widely read sources.

Each `agents/notes.md` entry must name the source behind the example and state
whether the eval passage is a quotation, a source-model paraphrase, or an
invented weak contrast.

Eval prompts must keep the instruction separate from the example text. Do not
teach the concept, review shape, rubric, or expected fault in the prompt; that
behavior belongs in `SKILL.md`.

## Validation

`scripts/validate_skills.sh` is the main local validation wrapper. It installs
[`skill-validator`](https://github.com/agent-ecosystem/skill-validator) into
`~/.local/bin` when that command is not already on `PATH`; this requires
[Go](https://go.dev/). It also installs the latest released
[`skilpel`](https://github.com/pasunboneleve/skilpel) executable artifact into
`~/.local/bin` when that command is not already on `PATH`.

[`skill-validator`](https://github.com/agent-ecosystem/skill-validator) checks
skill structure, frontmatter, Markdown, token size, and allowed files.
`skilpel` runs the model-backed evals in `evals/evals.yaml` against both a
with-skill run and a without-skill baseline, then enforces the pass-rate and
baseline-delta gates configured in `scripts/skilpel.yaml`.

For local model-backed evals, put `OPENAI_API_KEY` in `.env`. The committed
`.envrc` loads `.env` into the shell with direnv; `.env` is ignored by Git.

Run static checks before committing generated or documentation changes:

```bash
python3 -m py_compile scripts/generate_skills.py
python3 scripts/generate_skills.py --check
bash -n scripts/link_skills.sh
```

Run model-backed validation for changed skills only:

```bash
direnv exec . bash scripts/validate_skills.sh oiticica-concision
```

Use additional skill names when several skills changed. Run the full suite only
when shared generator, eval, or validation logic changes broadly enough to
affect every skill.

The default model-backed gate requires at least 20 percentage points of
pass-rate lift over the without-skill baseline and at least 90% with-skill pass
rate.
