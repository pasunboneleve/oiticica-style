# Contributing

This repository converts concepts from José Oiticica’s *Manual de Estilo* into
modern English [Codex](https://developers.openai.com/codex/cli) skills.

The source of truth for generated skill files is `scripts/generate_skills.py`.
Edit that script when adding or changing generated skill content. Do not hand
edit generated `SKILL.md`, `evals/evals.yaml`, `agents/openai.yaml`, or
`references/notes.md` files unless you are also changing the generator so the edit
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

Use public-domain English classics, civic texts, or Bible translations for
eval examples. The preferred source pool includes Shakespeare; Jonathan
Swift, especially *Gulliver’s Travels*; the Federalist Papers; Austen; Dickens;
Milton; Lincoln; Robert Louis Stevenson; William Livingston Klein’s *Why We
Punctuate*; H. W. Fowler and F. G. Fowler’s *The King’s English*; the United
States Constitution; Edward Bulwer-Lytton’s *Paul Clifford*; and the Berean
Literal Bible, World English Bible, and Berean Standard Bible.

Each `references/notes.md` entry must name the source behind the example and state
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
`~/.local/bin/skilpel` when that managed executable is not already present. Set
`SKILPEL=/path/to/skilpel` to test a local build explicitly.

[`skill-validator`](https://github.com/agent-ecosystem/skill-validator) checks
skill structure, frontmatter, Markdown, token size, and allowed files.
`skilpel` runs the model-backed evals in `evals/evals.yaml` against both a
with-skill run and a without-skill baseline, then enforces pass-rate and
baseline-delta gates. All skills use `scripts/skilpel.yaml` with GPT-5.6 Luna.
The configuration uses temperature `1` and low reasoning effort. It does not
set a seed because the OpenAI Responses API does not expose that parameter.

The wrapper requests `skilpel`'s human-readable text summary on stdout and lets
progress logs go to stderr. GitHub Actions sets `SKILPEL_LOG_FORMAT=pretty` so
intermediate eval results stay visible during long provider calls. Set
`SKILPEL_OUTPUT=json` for a machine-readable final summary.

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
when the model-validation workflow, runner, validator, or model configuration
changes broadly enough to affect every skill. Changes to authoring utilities
such as `scripts/generate_skills.py` do not widen model-backed validation; CI
derives its focused targets from the generated skill directories in the diff.

The default model-backed gate requires at least 20 percentage points of
pass-rate lift over the without-skill baseline and at least 90% with-skill pass
rate.
