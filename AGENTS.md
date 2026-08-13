# AGENTS.md

This repository contains modern English Codex skills derived from the first part of José Oiticica's `Manual de Estilo`.

## Workflow

- Use `kata` for task tracking. Run `kata ready --json`, `kata show <ref> --json`, `kata assign <ref> <owner> --json`, `kata comment <ref> --body "<note>" --json`, and `kata close <ref> --done --message "<validation and delivery evidence>" --commit <sha>`.
- Work on a feature branch. Do not implement on `main`.
- Do not push unless the user explicitly asks.
- Do not push directly to `main`.
- Run focused validation before closing tracked work.

## Skill Rules

- Every skill lives under `src/oiticica-*/SKILL.md`.
- Every skill must have `evals/evals.yaml` with positive and negative eval cases.
- Every skill must have `agents/openai.yaml` and `references/notes.md`.
- Skill names and directories must use the `oiticica-` prefix.
- Skills must be concise, modern English, and based on one concept from the first part of the manual.
- Apply English grammar, punctuation, morphology, idiom, and prosody. Do not carry Portuguese orthography or grammar into English.
- Prefer shallow, objective rules over long explanation.
- Modern English classic examples must come from public-domain, widely read English works or civic texts.
- Preferred source pools include Shakespeare; Jonathan Swift, especially
  *Gulliver’s Travels*; the Federalist Papers; Austen; Dickens; Milton; Lincoln;
  Robert Louis Stevenson; William Livingston Klein’s *Why We Punctuate*;
  the United States Constitution; Edward Bulwer-Lytton’s *Paul Clifford*; and
  public-domain Bible translations such as the Berean Literal Bible, World
  English Bible, and Berean Standard Bible.
- `references/notes.md` must name the source behind each modern English example and say whether the eval text is a source-model paraphrase, an invented weak passage, or a quotation.
- Eval prompts must keep the prompt instruction separate from the example text. If the example is not a quotation, say so.
- Eval prompts must prove skill lift: without-skill runs should ideally fail 0% and with-skill runs should pass 100%. Do not make prompts self-contained by teaching the review shape, rubric, concept definition, or expected fault; that behavior belongs in `SKILL.md`.

## Link Script

`scripts/link_skills.sh` installs only skill directories into Codex and Claude skill homes. It must not link, copy, or install `AGENTS.md` or `CLAUDE.md`.

## Validation

Run:

```bash
python3 -m py_compile scripts/generate_skills.py
python3 scripts/generate_skills.py --check
bash -n scripts/link_skills.sh
direnv exec . bash scripts/validate_skills.sh <skill-relpath>
```

Use `scripts/validate_skills.sh` for model-backed validation. Pass changed skill relpaths such as `oiticica-description` so unrelated skill evals do not run. The CI workflow uses `scripts/skill_ci_scope.sh` to choose focused validation from changed skill directories. Changes to authoring utilities such as `scripts/generate_skills.py` do not widen that scope; changes to the skill-validation workflow, scope classifier, runner, validator, or model configuration require full validation.

The default model-backed gate requires at least 20 percentage points of pass-rate lift over the without-skill baseline and at least 90% with-skill pass rate.
