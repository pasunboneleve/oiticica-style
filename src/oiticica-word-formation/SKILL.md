---
name: oiticica-word-formation
description: Apply Oiticica's word formation concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Word Formation

Use this skill when reviewing or rewriting English prose where word formation is the controlling issue.

Source concept: Deformation is an error in the form of a word.

## Rules

- Find wrong inflections, malformed derivatives, false stems, and invented forms that violate English morphology.
- Prefer the established English form unless a technical coinage is needed and well formed.
- Do not call a dialect form wrong when dialect is part of the assignment.
- Explain the stem, suffix, or inflection that fixes the word.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-word-formation: one sentence naming the concept>

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
<oiticica-word-formation: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-word-formation`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- The faulty form is identified.
- The replacement is a real or defensible English word.
- The explanation names the morphological pattern.
- The sentence keeps its intended meaning.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Source notes live in `references/notes.md`.
Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
