---
name: oiticica-assonance
description: Apply Oiticica's assonance concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica Assonance

Use this skill when reviewing or rewriting English prose where assonance is the controlling issue.

Source concept: Assonance is repetition of vowel sounds.

## Rules

- Allow assonance when it is deliberate music, echo, or emphasis.
- Flag accidental assonance when it distracts from prose meaning.
- Revise by changing one nearby word, not the whole sentence.
- Check the sound aloud.

## Review Shape

Use a concrete contrast:

```markdown
Principle:
<one sentence naming the concept>

Weak:
<small passage or paraphrase>

Fault:
<name the exact broken relation>

Better:
<corrected version>

Why:
<explain how the revision restores the relation>

Rubric:
<pass/fail against the objective checks>
```

## Objective Rubric

- The repeated vowel sound is identified.
- The review distinguishes intentional from accidental repetition.
- The correction reduces distraction.
- Meaning remains exact.

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Eval Hooks

- Positive model: Poe using vowel echo to sustain a poem's sound design.
- Negative model: The pale sale failed mainly in May.
- Required labels should be concrete, such as `allow, flag, revise` or a more exact local relation.
