# Oiticica style skills

Modern English Codex skills derived from the first part of Jose Oiticica's `Manual de Estilo`.

Each skill isolates one concept, gives shallow rules, applies English grammar and orthography, and includes positive and negative eval cases drawn from English-classic models or imitations.

## Use

Run:

```bash
bash scripts/link_skills.sh
```

The script links only skill directories. It does not install `AGENTS.md` or `CLAUDE.md`.

## Skills

- [`oiticica-description`](src/oiticica-description/SKILL.md): Description is a sequence of aspects.
- [`oiticica-narration`](src/oiticica-narration/SKILL.md): Narration is a sequence of facts or episodes.
- [`oiticica-dissertation`](src/oiticica-dissertation/SKILL.md): Dissertation is a sequence of opinions.
- [`oiticica-style-qualities`](src/oiticica-style-qualities/SKILL.md): Style has six essential qualities: correctness, concision, clarity, harmony, originality, and vigor.
- [`oiticica-correctness`](src/oiticica-correctness/SKILL.md): Correctness observes the grammatical tradition of the language being used.
- [`oiticica-solecism`](src/oiticica-solecism/SKILL.md): Solecism is an error of syntax.
- [`oiticica-spelling`](src/oiticica-spelling/SKILL.md): Cacography is an error of writing; in English practice, treat it as spelling and orthographic error.
- [`oiticica-word-formation`](src/oiticica-word-formation/SKILL.md): Deformation is an error in the form of a word.
- [`oiticica-confused-words`](src/oiticica-confused-words/SKILL.md): Crossing is the exchange of similar words.
- [`oiticica-foreignism`](src/oiticica-foreignism/SKILL.md): Barbarism is abusive use of foreign words or constructions.
- [`oiticica-latinism`](src/oiticica-latinism/SKILL.md): Latinism is foreignness drawn from Latin diction or syntax.
- [`oiticica-gallicism`](src/oiticica-gallicism/SKILL.md): Gallicism is foreignness drawn from French diction or syntax; in English, treat any imported construction by English idiom.
- [`oiticica-archaism`](src/oiticica-archaism/SKILL.md): Archaism is use of an old word or construction now out of use.
- [`oiticica-neologism`](src/oiticica-neologism/SKILL.md): Neologism is a recently created or introduced word or expression.
- [`oiticica-concision`](src/oiticica-concision/SKILL.md): Concision expresses aspects, facts, or opinions with the fewest words compatible with the other qualities.
- [`oiticica-clarity`](src/oiticica-clarity/SKILL.md): Clarity transmits thought in the form most easily understood.
- [`oiticica-ambiguity`](src/oiticica-ambiguity/SKILL.md): Ambiguity is a structure that allows more than one meaning when only one is intended.
- [`oiticica-anacoluthon`](src/oiticica-anacoluthon/SKILL.md): Anacoluthon is a break in logical order, usually by changing the expected subject or construction.
- [`oiticica-accumulation`](src/oiticica-accumulation/SKILL.md): Accumulation is excess and crossing of aspects, facts, or opinions in one period.
- [`oiticica-brachylogy`](src/oiticica-brachylogy/SKILL.md): Brachylogy is the opposite vice of accumulation: too many short, disconnected phrases with forced pauses.
- [`oiticica-precision`](src/oiticica-precision/SKILL.md): Precision uses the exact word or construction for an idea or emotion.
- [`oiticica-semicolon`](src/oiticica-semicolon/SKILL.md): The semicolon separates related clauses where a comma is too weak and a period too final.
- [`oiticica-comma`](src/oiticica-comma/SKILL.md): The comma marks coordination, interpolation, parenthesis, apposition, enumeration, ellipsis, inversion, and similar local relations.
- [`oiticica-harmony`](src/oiticica-harmony/SKILL.md): Harmony is the euphonic adjustment of words in the phrase and phrases in the period.
- [`oiticica-cacophony`](src/oiticica-cacophony/SKILL.md): Cacophony is an ugly or inconvenient sound produced by word contact.
- [`oiticica-assonance`](src/oiticica-assonance/SKILL.md): Assonance is repetition of vowel sounds.
- [`oiticica-alliteration`](src/oiticica-alliteration/SKILL.md): Alliteration is repetition of consonant sounds.
- [`oiticica-hiatus`](src/oiticica-hiatus/SKILL.md): Hiatus is collision of vowel sounds in adjacent syllables or words.
- [`oiticica-meter`](src/oiticica-meter/SKILL.md): Meter is measured language; Oiticica uses scansion to train the ear for rhythm.
- [`oiticica-prose-rhythm`](src/oiticica-prose-rhythm/SKILL.md): Harmony in prose comes from varied rhythmic groups arranged to fit sense.
- [`oiticica-originality`](src/oiticica-originality/SKILL.md): Originality presents aspects, facts, or opinions personally, without imitating another's processes or mannerisms.
- [`oiticica-image`](src/oiticica-image/SKILL.md): An image is an aesthetic relation between objects, phenomena, or actions.
- [`oiticica-vigor`](src/oiticica-vigor/SKILL.md): Vigor is energy of expression in aspects, episodes, or conceptions.
- [`oiticica-inversion`](src/oiticica-inversion/SKILL.md): Inversion alters logical word order to give relief, rhythm, or emphasis.
- [`oiticica-antithesis`](src/oiticica-antithesis/SKILL.md): Antithesis is the opposition of two truths that clarify each other.

## Validation

Static checks:

```bash
python3 -m py_compile scripts/generate_skills.py
python3 scripts/generate_skills.py --check
bash -n scripts/link_skills.sh
```
