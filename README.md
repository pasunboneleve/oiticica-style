# Oiticica style skills

A catalogue of writing skills for Codex, adapted from José Oiticica’s
*Manual de Estilo*.

Oiticica taught style by naming virtues and vices, defining each one sharply,
then showing good and bad examples. This repository turns that method into
small agent skills: one concept per skill, with rules, examples, metadata, and
validation.

<br>

<p align="center" style="margin: 0.35rem 0 0.35rem 0;">
  <img
      src="assets/jose-oiticica-dops.jpg"
      alt="José Oiticica, DOPS prontuário photograph"
      style="width:58.5%;"
      />
</p>

<p align="center" style="margin: 0 0 1.25rem 0;">
    <sub>José Oiticica in a 1924 police-archive photograph, after his arrest during the armed São Paulo tenentista uprising.</sub>
</p>

## Why this exists

Most writing advice compresses too much. “Be clear” is true, but useless unless
clarity is broken into inspectable failures: ambiguity, anacoluthon,
accumulation, weak punctuation, bad rhythm, vague diction.

Oiticica’s method is better suited to agents than a prose summary of style.
Each skill here isolates one writing operation so an agent can apply, test, and
revise against it.

The goal is not to make agents “write beautifully” by vibes. The goal is to
give them a working catalogue of style decisions.

## Quickstart

Link the skills into Codex and Claude:

```bash
bash scripts/link_skills.sh
```

This creates symlinks under:

```bash
~/.codex/skills
~/.claude/skills
```

The script links only skill directories. It does **not** install `AGENTS.md`,
`CLAUDE.md`, or project-level instructions.

After linking, start Codex and invoke a skill by name, for example:

```text
Use oiticica-concision to tighten this paragraph without losing meaning.
```

or:

```text
Use oiticica-ambiguity to find sentences that allow more than one reading.
```

## What is included

Each skill contains:

- `SKILL.md` — the rule, boundary, examples, and application notes.
- `agents/openai.yaml` — agent UI metadata.
- `agents/notes.md` — source notes identifying the public-domain English texts used for positive and negative examples.

Positive examples are sourced from public-domain English texts, such as
Shakespeare, the Federalist Papers, and other classic works. Source notes mark
whether each eval passage is quoted, paraphrased from a source model, or
invented as a weak contrast.

## Skill catalogue

| Skill                                                               | Use it to check                                                                        |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [`oiticica-description`](src/oiticica-description/SKILL.md)         | Whether a passage presents aspects in a coherent order.                                |
| [`oiticica-narration`](src/oiticica-narration/SKILL.md)             | Whether episodes or facts move in a clear sequence.                                    |
| [`oiticica-dissertation`](src/oiticica-dissertation/SKILL.md)       | Whether opinions develop in an ordered argument.                                       |
| [`oiticica-style-qualities`](src/oiticica-style-qualities/SKILL.md) | The six major qualities: correctness, concision, clarity, harmony, originality, vigor. |
| [`oiticica-correctness`](src/oiticica-correctness/SKILL.md)         | Grammatical correctness in the language being used.                                    |
| [`oiticica-concision`](src/oiticica-concision/SKILL.md)             | Unnecessary words, padding, and removable repetition.                                  |
| [`oiticica-clarity`](src/oiticica-clarity/SKILL.md)                 | Whether the thought is easy to understand.                                             |
| [`oiticica-ambiguity`](src/oiticica-ambiguity/SKILL.md)             | Structures that allow unintended meanings.                                             |
| [`oiticica-precision`](src/oiticica-precision/SKILL.md)             | Whether words name the intended idea exactly.                                          |
| [`oiticica-harmony`](src/oiticica-harmony/SKILL.md)                 | Sound, rhythm, and euphony in prose.                                                   |
| [`oiticica-originality`](src/oiticica-originality/SKILL.md)         | Dependence on imitation, cliché, or borrowed manner.                                   |
| [`oiticica-vigor`](src/oiticica-vigor/SKILL.md)                     | Energy, force, and expressive pressure.                                                |

For the full generated list, inspect the generated skill directories under
[`src/`](src/).

## Development

Validate the generated skills:

```bash
python3 -m py_compile scripts/generate_skills.py
python3 scripts/generate_skills.py --check
bash -n scripts/link_skills.sh
direnv exec . bash scripts/validate_skills.sh oiticica-concision
```

Use `scripts/validate_skills.sh` with changed skill names so unrelated skill
evals do not run.

## Contributing

Contributions should preserve the shape of the project:

- one concept per skill;
- short rules before long explanation;
- examples before abstraction where possible;
- clear citation of every public-domain source;
- explicit labeling for invented weak examples;
- no unsourced “style advice” pasted into generated skills.

See [`AGENTS.md`](AGENTS.md) for repository-local workflow and validation
rules.

## License

Code and original text in this repository are licensed under GPL-3.0-or-later.

Archival images are not covered by the repository software license unless
explicitly stated. The José Oiticica DOPS image is reproduced as a historical
archival document with source attribution.

José Oiticica, police/prontuário photograph, 1924. Source: Arquivo Público do
Estado do Rio de Janeiro (APERJ), Prontuário do Departamento de Ordem Política
e Social (DOPS), via CeDInCI.
