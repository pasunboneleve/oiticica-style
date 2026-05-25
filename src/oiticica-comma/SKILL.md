---
name: oiticica-comma
description: Apply Oiticica's comma concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Comma

Use this skill when reviewing or rewriting English prose where comma is the controlling issue.

Source concept: The comma marks coordination, interpolation, parenthesis, apposition, enumeration, ellipsis, inversion, and similar local relations.

## Rules

- Use commas to show sentence structure, not breathing alone.
- Separate introductory conditions, parenthetic material, appositives, coordinate items, and displaced adverbials when needed.
- Do not separate a subject from its verb or a verb from its object without an intervening structure.
- Use commas to prevent misreading.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-comma: one sentence naming the concept>

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
<oiticica-comma: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-comma`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- Each comma has a named structural job.
- No comma interrupts a direct grammatical bond.
- Parenthetic and restrictive material are distinguished.
- The punctuation removes ambiguity.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Source notes live in `references/notes.md`.
Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
