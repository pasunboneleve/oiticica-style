---
name: oiticica-latinism
description: Apply Oiticica's latinism concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Latinism

Use this skill when reviewing or rewriting English prose where latinism is the controlling issue.

Source concept: Latinism is foreignness drawn from Latin diction or syntax.

## Rules

- Use Latinate terms when they are the exact English words for law, science, theology, or rhetoric.
- Prefer plain English when Latinate abstraction hides the actor or action.
- Avoid Latin word order that strains modern English.
- Do not replace a precise technical Latinism with a vague Anglo-Saxon word.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-latinism: one sentence naming the concept>

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
<oiticica-latinism: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-latinism`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- The review separates exact term from pretentious abstraction.
- The revision names the actor and action.
- Technical meaning survives.
- The sentence sounds like modern English, not translated Latin.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
