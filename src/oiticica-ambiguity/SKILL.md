---
name: oiticica-ambiguity
description: Apply Oiticica's ambiguity concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Ambiguity

Use this skill when reviewing or rewriting English prose where ambiguity is the controlling issue.

Source concept: Ambiguity is a structure that allows more than one meaning when only one is intended.

## Rules

- Find the word, pronoun, modifier, punctuation mark, or clause relation that permits two readings.
- State both possible readings.
- Revise so only the intended reading remains.
- Keep useful literary ambiguity only when the task asks for it.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-ambiguity: one sentence naming the concept>

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
<oiticica-ambiguity: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-ambiguity`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- At least two readings are named.
- The intended reading is selected.
- The fix removes the unintended reading.
- The revision does not flatten deliberate irony or double meaning.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
