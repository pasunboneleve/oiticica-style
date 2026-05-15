---
name: oiticica-narration
description: Apply Oiticica's narration concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Narration

Use this skill when reviewing or rewriting English prose where narration is the controlling issue.

Source concept: Narration is a sequence of facts or episodes.

## Rules

- Keep events in causal or temporal order unless a deliberate reversal clarifies cause.
- Name the actor, action, obstacle, and result for each episode.
- Do not stop the movement for decoration that neither changes the episode nor prepares the next one.
- Use summary for routine links and scene for decisive turns.

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<oiticica-narration: one sentence naming the concept>

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
<oiticica-narration: one sentence naming the concept>

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

Start `Principle` with the exact skill name `oiticica-narration`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

- A reader can list what happened first, next, and last.
- Each episode changes the situation.
- Motives and consequences are close to the actions they explain.
- No descriptive pause hides the main action.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
