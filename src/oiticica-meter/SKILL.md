---
name: oiticica-meter
description: Apply Oiticica's meter concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Meter

Use this skill when reviewing or rewriting English prose where meter is the controlling issue.

Source concept: Meter is measured language; Oiticica uses scansion to train the ear for rhythm.

## Rules

- Use English metrical terms when analyzing English: stress, foot, iamb, trochee, anapest, dactyl, line, caesura.
- Do not translate Portuguese syllable-count rules directly into English stress verse.
- Scan only when rhythm is relevant to the task.
- Use meter as evidence for harmony, not as decoration.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-meter: one sentence naming the concept>

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
<oiticica-meter: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-meter`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- The analysis uses English prosody.
- Stressed and unstressed beats are marked or described accurately.
- The metrical observation explains an effect.
- The review does not impose meter on prose without need.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
