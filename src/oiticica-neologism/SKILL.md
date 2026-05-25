---
name: oiticica-neologism
description: Apply Oiticica's neologism concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Neologism

Use this skill when reviewing or rewriting English prose where neologism is the controlling issue.

Source concept: Neologism is a recently created or introduced word or expression.

## Rules

- Accept a new word when a new thing, role, process, or distinction needs a name.
- Reject novelty that displaces a good existing English word without adding meaning.
- Check formation: stem, prefix, suffix, stress, and likely pronunciation.
- Prefer the least surprising word that names the new distinction.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-neologism: one sentence naming the concept>

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
<oiticica-neologism: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-neologism`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- The need for the new word is explicit.
- The word follows English formation patterns.
- No established word would serve as well.
- The sentence tells the reader what the new term denotes.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Source notes live in `references/notes.md`.
Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
