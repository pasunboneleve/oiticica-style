---
name: oiticica-correctness
description: Apply Oiticica's correctness concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Correctness

Use this skill when reviewing or rewriting English prose where correctness is the controlling issue.

Source concept: Correctness observes the grammatical tradition of the language being used.

## Rules

- Apply modern standard English grammar, spelling, idiom, and punctuation unless the task requires dialect or historical form.
- Preserve quoted historical language as quotation; modernize only the surrounding instruction.
- Fix correctness faults before judging elegance.
- Do not import Portuguese grammar rules into English.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-correctness: one sentence naming the concept>

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
<oiticica-correctness: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-correctness`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- Subject, verb, pronoun, modifier, and punctuation choices conform to the intended English register.
- Dialect, archaism, or nonstandard form is marked by character, quotation, or purpose.
- No correction changes the facts or voice without reason.
- The revised sentence remains idiomatic English.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Source notes live in `references/notes.md`.
Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
