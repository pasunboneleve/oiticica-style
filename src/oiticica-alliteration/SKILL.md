---
name: oiticica-alliteration
description: Apply Oiticica's alliteration concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Alliteration

Use this skill when reviewing or rewriting English prose where alliteration is the controlling issue.

Source concept: Alliteration is repetition of consonant sounds.

## Rules

- Keep alliteration when it reinforces action, mood, or memory.
- Cut accidental alliteration that turns prose comic or mechanical.
- Avoid slogan-like consonant strings in serious exposition.
- Prefer exact words over sound play.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-alliteration: one sentence naming the concept>

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
<oiticica-alliteration: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-alliteration`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- The repeated consonant is local and audible.
- Its purpose is stated or rejected.
- The revision reduces noise without reducing precision.
- Any retained pattern serves meaning.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Source notes live in `references/notes.md`.
Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
