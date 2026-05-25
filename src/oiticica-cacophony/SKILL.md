---
name: oiticica-cacophony
description: Apply Oiticica's cacophony concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Cacophony

Use this skill when reviewing or rewriting English prose where cacophony is the controlling issue.

Source concept: Cacophony is an ugly or inconvenient sound produced by word contact.

## Rules

- Find accidental obscene, comic, or clumsy sound joins.
- Revise word order or choose a synonym only enough to remove the collision.
- Ignore harmless contact when the sentence reads naturally.
- Do not make the sentence less exact merely to avoid a faint sound echo.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-cacophony: one sentence naming the concept>

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
<oiticica-cacophony: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-cacophony`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- The offending sound is local and demonstrable by reading aloud.
- The revision removes that sound.
- Meaning and register remain intact.
- The review does not over-police ordinary English joins.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Source notes live in `references/notes.md`.
Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
