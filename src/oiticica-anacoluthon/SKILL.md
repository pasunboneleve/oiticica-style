---
name: oiticica-anacoluthon
description: Apply Oiticica's anacoluthon concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Anacoluthon

Use this skill when reviewing or rewriting English prose where anacoluthon is the controlling issue.

Source concept: Anacoluthon is a break in logical order, usually by changing the expected subject or construction.

## Rules

- Track the sentence's announced subject or construction to its grammatical completion.
- Flag a break when the sentence starts one structure and finishes another by accident.
- Repair by restoring the promised subject, adding the missing link, or splitting the sentence.
- Keep deliberate anacoluthon in dramatic speech when it expresses interruption or emotion.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-anacoluthon: one sentence naming the concept>

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
<oiticica-anacoluthon: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-anacoluthon`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- The announced construction is identified.
- The point of break is identified.
- The repair completes one coherent construction.
- Deliberate speech effects are not overcorrected.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
