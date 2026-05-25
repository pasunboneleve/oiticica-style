---
name: oiticica-prose-rhythm
description: Apply Oiticica's prose rhythm concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Prose Rhythm

Use this skill when reviewing or rewriting English prose where prose rhythm is the controlling issue.

Source concept: Harmony in prose comes from varied rhythmic groups arranged to fit sense.

## Rules

- Break a prose period into natural spoken groups when cadence matters.
- Vary group length to avoid monotony.
- Put the strongest word near a stress point or sentence end when possible.
- Do not let rhythm obscure grammar or logical order.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-prose-rhythm: one sentence naming the concept>

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
<oiticica-prose-rhythm: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-prose-rhythm`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- The prose has readable groups rather than a flat chain.
- Cadence supports the important word.
- Long and short units vary with the movement of thought.
- The revision can be read aloud smoothly.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Source notes live in `references/notes.md`.
Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
