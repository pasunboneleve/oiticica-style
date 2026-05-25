---
name: oiticica-originality
description: Apply Oiticica's originality concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Originality

Use this skill when reviewing or rewriting English prose where originality is the controlling issue.

Source concept: Originality presents aspects, facts, or opinions personally, without imitating another's processes or mannerisms.

## Rules

- Reject stock phrases, borrowed images, and general aspects.
- Particularize place, time, object, and action.
- Use exact vocabulary instead of novelty hunting.
- Let originality arise from observation and relation, not forced strangeness.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-originality: one sentence naming the concept>

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
<oiticica-originality: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-originality`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- The passage contains at least one specific observed relation.
- No stock image carries the main effect.
- The vocabulary names the subject's own world.
- The sentence could not be moved unchanged to any subject of the same class.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Source notes live in `references/notes.md`.
Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
