# Contributing

This repository converts concepts from José Oiticica’s *Manual de Estilo* into
modern English Codex skills.

The source of truth for generated skill files is `scripts/generate_skills.py`.
Edit that script when adding or changing generated skill content. Do not hand
edit generated `SKILL.md`, `evals/evals.json`, `agents/openai.yaml`, or
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
