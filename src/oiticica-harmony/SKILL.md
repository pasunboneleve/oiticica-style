---
name: oiticica-harmony
description: Apply Oiticica's harmony concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Harmony

Use this skill when reviewing or rewriting English prose where harmony is the controlling issue.

Source concept: Harmony is the euphonic adjustment of words in the phrase and phrases in the period.

## Rules

- Read prose aloud when sound or cadence matters.
- Avoid accidental cacophony, heavy repetition, and awkward vowel collisions.
- Vary sentence length and stress pattern to fit the movement of thought.
- Do not improve sound at the cost of correctness or clarity.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-harmony: one sentence naming the concept>

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
<oiticica-harmony: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-harmony`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- The sentence can be read aloud without stumbling.
- Repeated sounds are intentional or unobtrusive.
- Cadence supports emphasis.
- Sound changes do not alter meaning.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Source notes live in `references/notes.md`.
Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
