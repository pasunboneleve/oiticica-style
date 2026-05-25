---
name: oiticica-assonance
description: Apply Oiticica's assonance concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Assonance

Use this skill when reviewing or rewriting English prose where assonance is the controlling issue.

Source concept: Assonance is repetition of vowel sounds.

## Rules

- Allow assonance when it is deliberate music, echo, or emphasis.
- Flag accidental assonance when it distracts from prose meaning.
- Revise by changing one nearby word, not the whole sentence.
- Check the sound aloud.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-assonance: one sentence naming the concept>

Preserve:
<supplied example text>

Why:
<why the model satisfies the concept>

Rubric:
<at least two objective checks, each marked Pass or Fail>
```

Use the repair shape for weak passages:

```markdown
Principle:
<oiticica-assonance: one sentence naming the concept>

Weak:
<small passage or paraphrase>

Fault:
<name the exact broken relation>

Better:
<corrected version>

Why:
<explain how the revision restores the relation>

Rubric:
<at least two objective checks, each marked Pass or Fail>
```

Start `Principle` with the exact skill name `oiticica-assonance`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- The repeated vowel sound is identified.
- The review distinguishes intentional from accidental repetition.
- The correction reduces distraction.
- Meaning remains exact.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Source notes live in `references/notes.md`.
Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
