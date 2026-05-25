---
name: oiticica-hiatus
description: Apply Oiticica's hiatus concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Hiatus

Use this skill when reviewing or rewriting English prose where hiatus is the controlling issue.

Source concept: Hiatus is collision of vowel sounds in adjacent syllables or words.

## Rules

- Check vowel collisions that make English prose stumble.
- Repair by contraction, reordering, or a more exact word when the collision is distracting.
- Do not force old prosody rules onto ordinary modern English.
- Keep hiatus when it is natural or metrically intended.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-hiatus: one sentence naming the concept>

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
<oiticica-hiatus: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-hiatus`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- The vowel collision can be heard aloud.
- The correction improves ease of reading.
- The sentence remains idiomatic.
- No exact technical term is lost.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Source notes live in `references/notes.md`.
Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
