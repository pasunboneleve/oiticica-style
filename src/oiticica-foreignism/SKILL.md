---
name: oiticica-foreignism
description: Apply Oiticica's foreignism concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Foreignism

Use this skill when reviewing or rewriting English prose where foreignism is the controlling issue.

Source concept: Barbarism is abusive use of foreign words or constructions.

## Rules

- Keep necessary foreign terms when English lacks an exact equivalent or the domain owns the term.
- Naturalize or translate needless foreign words that only display learning.
- Reject foreign syntax that makes English stiff or unclear.
- Do not purge useful loanwords that are established English.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-foreignism: one sentence naming the concept>

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
<oiticica-foreignism: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-foreignism`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- Each foreign term has necessity, domain value, or quotation value.
- English idiom governs the sentence.
- The review distinguishes loanword from needless display.
- The correction improves clarity without narrowing meaning.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Source notes live in `references/notes.md`.
Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
