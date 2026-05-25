---
name: oiticica-inversion
description: Apply Oiticica's inversion concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Inversion

Use this skill when reviewing or rewriting English prose where inversion is the controlling issue.

Source concept: Inversion alters logical word order to give relief, rhythm, or emphasis.

## Rules

- Use inversion only when it improves emphasis, rhythm, or image placement.
- Keep modern English syntax intelligible.
- Reject violent or archaic inversion that calls attention to itself.
- Compare the inverted order with the direct order before recommending it.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-inversion: one sentence naming the concept>

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
<oiticica-inversion: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-inversion`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- The word moved gains useful emphasis.
- The sentence remains idiomatic English.
- The inversion does not obscure subject and verb.
- The direct order is worse for a named reason.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Source notes live in `references/notes.md`.
Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
