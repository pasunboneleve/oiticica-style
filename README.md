# Oiticica style skills

A catalogue of [Codex](https://developers.openai.com/codex/cli) writing skills
adapted from José Oiticica’s *Manual de Estilo*.

Oiticica’s method is unusually agent-friendly: name one virtue or vice of
style, define it sharply, then test prose against examples. This repository
translates that method into modern English skills for Codex.

The result is not a single “write better” instruction. It is a working taxonomy
of style: correctness, concision, clarity, harmony, originality, vigor, and the
smaller failures that damage them.

<br>

<p align="center" style="margin: 0.35rem 0 0.35rem 0;">
  <img
      src="assets/jose-oiticica-dops.jpg"
      alt="José Oiticica, DOPS prontuário photograph"
      style="width:58.5%;"
      />
</p>

<p align="center" style="margin: 0 0 1.25rem 0;">
    <sub>José Oiticica, philologist, teacher, anarchist, and author of <em>Manual de Estilo</em>, in a 1924 police-archive photograph.</sub>
</p>

## Why this exists

Most writing advice compresses too much. “Be clear” is true, but useless unless
clarity is broken into inspectable failures: ambiguity, anacoluthon,
accumulation, weak punctuation, bad rhythm, vague diction.

Oiticica’s method gives agents a better unit of work than a general prose
summary. Each skill isolates one writing operation so an agent can apply, test,
and revise against it.

A century-old style manual becomes a working taxonomy of Codex skills.

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
Use oiticica-style to diagnose and revise this paragraph.
```

or invoke a narrower principle directly:

```text
Use oiticica-concision to tighten this paragraph without losing meaning.
```

or:

```text
Use oiticica-ambiguity to find sentences that allow more than one reading.
```

## Skills

### General router

- [`oiticica-style`](src/oiticica-style/SKILL.md): Orchestrates the principle skills by identifying genre, eliminating defects, and applying qualities only where the passage needs them.

### Forms of composition

- [`oiticica-description`](src/oiticica-description/SKILL.md): Description is a sequence of aspects.
- [`oiticica-narration`](src/oiticica-narration/SKILL.md): Narration is a sequence of facts or episodes.
- [`oiticica-dissertation`](src/oiticica-dissertation/SKILL.md): Dissertation is a sequence of opinions.

### Major qualities

- [`oiticica-style-qualities`](src/oiticica-style-qualities/SKILL.md): Style has six essential qualities: correctness, concision, clarity, harmony, originality, and vigor.
- [`oiticica-correctness`](src/oiticica-correctness/SKILL.md): Correctness observes the grammatical tradition of the language being used.
- [`oiticica-concision`](src/oiticica-concision/SKILL.md): Concision expresses aspects, facts, or opinions with the fewest words compatible with the other qualities.
- [`oiticica-clarity`](src/oiticica-clarity/SKILL.md): Clarity transmits thought in the form most easily understood.
- [`oiticica-harmony`](src/oiticica-harmony/SKILL.md): Harmony is the euphonic adjustment of words in the phrase and phrases in the period.
- [`oiticica-originality`](src/oiticica-originality/SKILL.md): Originality presents aspects, facts, or opinions personally, without imitating another's processes or mannerisms.
- [`oiticica-vigor`](src/oiticica-vigor/SKILL.md): Vigor is energy of expression in aspects, episodes, or conceptions.

### Faults of correctness

- [`oiticica-solecism`](src/oiticica-solecism/SKILL.md): Solecism is an error of syntax.
- [`oiticica-spelling`](src/oiticica-spelling/SKILL.md): Cacography is an error of writing; in English practice, treat it as spelling and orthographic error.
- [`oiticica-word-formation`](src/oiticica-word-formation/SKILL.md): Deformation is an error in the form of a word.
- [`oiticica-confused-words`](src/oiticica-confused-words/SKILL.md): Crossing is the exchange of similar words.
- [`oiticica-foreignism`](src/oiticica-foreignism/SKILL.md): Barbarism is abusive use of foreign words or constructions.
- [`oiticica-latinism`](src/oiticica-latinism/SKILL.md): Latinism is foreignness drawn from Latin diction or syntax.
- [`oiticica-gallicism`](src/oiticica-gallicism/SKILL.md): Gallicism is foreignness drawn from French diction or syntax; in English, treat any imported construction by English idiom.
- [`oiticica-archaism`](src/oiticica-archaism/SKILL.md): Archaism is use of an old word or construction now out of use.
- [`oiticica-neologism`](src/oiticica-neologism/SKILL.md): Neologism is a recently created or introduced word or expression.

### Faults of clarity

- [`oiticica-ambiguity`](src/oiticica-ambiguity/SKILL.md): Ambiguity is a structure that allows more than one meaning when only one is intended.
- [`oiticica-anacoluthon`](src/oiticica-anacoluthon/SKILL.md): Anacoluthon is a break in logical order, usually by changing the expected subject or construction.
- [`oiticica-accumulation`](src/oiticica-accumulation/SKILL.md): Accumulation is excess and crossing of aspects, facts, or opinions in one period.
- [`oiticica-brachylogy`](src/oiticica-brachylogy/SKILL.md): Brachylogy is the opposite vice of accumulation: too many short, disconnected phrases with forced pauses.
- [`oiticica-precision`](src/oiticica-precision/SKILL.md): Precision uses the exact word or construction for an idea or emotion.
- [`oiticica-semicolon`](src/oiticica-semicolon/SKILL.md): The semicolon separates related clauses where a comma is too weak and a period too final.
- [`oiticica-comma`](src/oiticica-comma/SKILL.md): The comma marks coordination, interpolation, parenthesis, apposition, enumeration, ellipsis, inversion, and similar local relations.

### Faults and resources of sound

- [`oiticica-cacophony`](src/oiticica-cacophony/SKILL.md): Cacophony is an ugly or inconvenient sound produced by word contact.
- [`oiticica-assonance`](src/oiticica-assonance/SKILL.md): Assonance is repetition of vowel sounds.
- [`oiticica-alliteration`](src/oiticica-alliteration/SKILL.md): Alliteration is repetition of consonant sounds.
- [`oiticica-hiatus`](src/oiticica-hiatus/SKILL.md): Hiatus is collision of vowel sounds in adjacent syllables or words.
- [`oiticica-meter`](src/oiticica-meter/SKILL.md): Meter is measured language; Oiticica uses scansion to train the ear for rhythm.
- [`oiticica-prose-rhythm`](src/oiticica-prose-rhythm/SKILL.md): Harmony in prose comes from varied rhythmic groups arranged to fit sense.

### Force and figure

- [`oiticica-image`](src/oiticica-image/SKILL.md): An image is an aesthetic relation between objects, phenomena, or actions.
- [`oiticica-inversion`](src/oiticica-inversion/SKILL.md): Inversion alters logical word order to give relief, rhythm, or emphasis.
- [`oiticica-antithesis`](src/oiticica-antithesis/SKILL.md): Antithesis is the opposition of two truths that clarify each other.

## What is included

Each skill contains:

- `SKILL.md` — the rule, boundary, examples, and application notes.
- `agents/openai.yaml` — agent UI metadata.
- `agents/notes.md` — source notes identifying the public-domain English texts used for positive and negative examples.

Positive examples are sourced from public-domain English texts, such as
Shakespeare, the Federalist Papers, and other classic works. Source notes mark
whether each eval passage is quoted, paraphrased from a source model, or
invented as a weak contrast.

## Development

Validate the generated skills and README skill coverage:

```bash
python3 -m py_compile scripts/generate_skills.py
python3 scripts/generate_skills.py --check
bash -n scripts/link_skills.sh
direnv exec . bash scripts/validate_skills.sh oiticica-concision
```

Use `scripts/validate_skills.sh` with changed skill names so unrelated skill
evals do not run.

## Contributing

This repository is generated from structured source material. Do not edit
generated skill files casually.

See [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md) for how to add a skill,
choose public-domain English examples, regenerate files, and run validation.

## License

Code and original text in this repository are licensed under GPL-3.0-or-later.

Archival images are not covered by the repository software license unless
explicitly stated. The José Oiticica DOPS image is reproduced as a historical
archival document with source attribution.

José Oiticica, police/prontuário photograph, 1924. Source: Arquivo Público do
Estado do Rio de Janeiro (APERJ), Prontuário do Departamento de Ordem Política
e Social (DOPS), via CeDInCI.
