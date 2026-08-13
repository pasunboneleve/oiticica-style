---
name: oiticica-clarity-faults
description: Audit a single English passage or compare parallel drafts using the seven component skills in Oiticica's faults-of-clarity section.
---

# Oiticica Clarity Faults

Audit every supplied passage. When the user supplies parallel drafts, audit each independently before comparing them.

Source concept: Clarity requires avoiding ambiguity, anacoluthon, accumulation, and brachylogy; choosing precise words; and using semicolons and commas to expose relations.

## Component Skills

Load and apply all seven component skills for every audit. These `$` handles are explicit skill invocations, not labels:

- `$oiticica-ambiguity`
- `$oiticica-anacoluthon`
- `$oiticica-accumulation`
- `$oiticica-brachylogy`
- `$oiticica-precision`
- `$oiticica-semicolon`
- `$oiticica-comma`

Use each component skill's rules and objective rubric. Do not substitute an unaided general definition of the fault. If the runtime cannot resolve nested skill invocations, use the decision boundaries below rather than omitting a row.

## Decisions

Apply all seven. A matching test requires at least `Minor`, even when the prose remains intelligible.
The tests below are controlling: once quoted evidence satisfies a test, assign at least `Minor`. Do not reverse a matched result merely because the passage is famous, readable, coherent as a whole, rhetorically parallel, or effective in another respect.

- **Ambiguity**: a word, pronoun, modifier, attachment, or clause relation permits two contextually coherent readings. Name both.
- **Anacoluthon**: the sentence announces one subject or construction and accidentally completes another.
- **Accumulation**: excess or crossing of aspects, facts, or opinions forces one period to hold competing main relations.
- **Brachylogy**: short, disconnected sentences or fragments conceal relations that should be joined. Deliberate dramatic interruption or emphasis is `None` only when each punctuated unit is grammatically independent or the interruption does not borrow a required construction from another sentence.
- **Imprecision**: a word or construction fails to name the exact object, action, degree, or relation, or an image's literal terms conflict.
- **Semicolon**: a semicolon falsely groups unrelated units, splits a grammatical dependency, or is too weak or strong for the relation.
- **Comma**: a missing, misplaced, or needless comma hides structure, creates a false grouping, or breaks a direct grammatical bond.

Grade `None` for no evidence, `Minor` for a local fault, and `Major` for a repeated or controlling fault. Quote the evidence and explain the broken relation. Assign one textual cause to its most specific row and grade derivative symptoms `None` unless separate textual evidence independently satisfies another row.

- A modifier, word, or phrase with several coherent attachments is Ambiguity, not Imprecision. Mere dictionary polysemy is not ambiguity when the surrounding predicates select one conventional sense; a merely conceivable but semantically implausible reading is `None`. If a proposed second reading exists only by treating a contextually wrong derivative as a loose synonym, grade the malaprop under Imprecision and Ambiguity `None`.
- An anaphoric pronoun is not ambiguous when grammatical agreement and the predicate's ordinary event meaning select one stated antecedent; do not invent an implied noun as a rival referent when the predicate would not coherently apply to it.
- Parallel names used as contrasting exemplars do not create Ambiguity merely because a preposition could abstractly express joint possession; require a second reading that remains coherent with the surrounding contrast.
- One announced construction that never reaches its grammatical completion is Anacoluthon, not Brachylogy. This includes coordination that asks one relative to serve incompatible grammatical roles. Do not also grade Brachylogy when the evidence is wholly inside one punctuated sentence. Brachylogy requires two or more punctuated units whose sentence boundaries break a shared relation; a fragment that omits its subject or predicate by borrowing another sentence's construction remains Brachylogy even when readable or emphatic.
- A coordinated opening of the form `A or B` loses sentence unity when the next sentence separately develops A and a third separately develops B. This test is sufficient for Brachylogy even if all three sentences are grammatical and rhetorically parallel.
- Four or more consecutive short sentences in one development, including three repeated subject-predicate starts about one subject, are sufficient for Brachylogy; parallel grammar does not by itself justify the repeated full stops.
- A dash-separated chain of four or more fragments that repeatedly omits subjects, verbs, or connective relations is sufficient for Brachylogy. Dialogue or dramatic voice does not exempt it when the reader must reconstruct those relations.
- In such a fragment chain, grade the omitted grammatical and connective relations only as Brachylogy: several fragments serving one character sketch are not Accumulation, and context-appropriate broad dramatic terms are not Imprecision or Ambiguity without separate evidence outside the omissions.
- When a later demonstrative such as `this` clearly summarizes the combined thought of two preceding sentences, its backward reference is not Ambiguity; if the full stops conceal that combined relation, grade Brachylogy.
- Accumulation requires several factual or logical aspects, facts, or opinions to cross within one period. Grade at least `Minor` when a reader must retain an unfinished main dependency across a parenthesis and successive modifiers that shift among four or more objects or actions; this test is sufficient even when all details describe one scene. A parallel enumeration whose members all perform the same grammatical function is not accumulation. Several words, examples, or figurative images serving one relation are not accumulation; incompatible terms within one image belong to Imprecision.
- As a mechanical backstop, a period longer than 50 words that contains a parenthesis and three or more subordinate or participial modifiers with different grammatical heads is at least `Minor` Accumulation. Scenic unity or grammatical correctness does not override that threshold.
- Imprecision requires a wrong or incompatible word, collocation, or image. Test near-homophones and derivatives by substituting their plain glosses; do not accept a related form that names a different property. Distinguish an adjective naming a titled or respected person, such as `reverend`, from the adjective naming the respectful quality of an act or service, `reverent`. Redundancy belongs to concision, and an idiomatic figurative verb is not imprecise merely because it is nonliteral.
- A wrong or missing semicolon belongs to Semicolon. A semicolon must not replace one of a paired set of commas around an apposition or parenthesis, or split a clause that functions as an adverbial explanation or degree complement of the first clause. If replacing or removing the semicolon restores the announced construction, grade the derivative syntactic break under Semicolon and grade Anacoluthon `None`.
- A wrong or missing comma belongs to Comma. A parenthetic participial phrase inside a subject-predicate frame requires paired commas. If an initial noun is followed by a participle and then by a finite verb with no new subject, the noun is the finite verb's subject: place the first comma after the noun, not only after the participial phrase. An optional rhetorical comma is `None` unless it creates a false grouping or hides a grammatical bond; in particular, a comma between a finite verb and an unmistakably adverbial phrase is `None` when removing it changes no attachment. When a mark is the specific cause of a false grouping, grade Ambiguity `None` unless another construction independently permits two readings.
- Do not double-count punctuation adjacent to an Anacoluthon. If removing a comma leaves the incompatible subject or construction unchanged, grade the syntactic cause under Anacoluthon and Comma `None`.

Preserve historically accepted punctuation and usage in sourced quotations; current convention alone is not a fault. Do not presume sourced, famous, literary, civic, sacred, quoted, grammatical, or intelligible prose is fault-free. Judge literal translations as English unless source-language structure is explicitly required. Preserve quotations; do not rewrite unless asked.

## Router Mode

When the general `oiticica-style` router invokes this skill as a pipeline stage, apply all seven component skills but defer final response shape, total length, follow-up selection, and revision decisions to the router. Return the seven evidenced grades to the router; do not emit this skill's standalone audit format.

## Response

Keep each audit under 260 words. For each passage or draft, use exactly one line per fault in this form: `Name — Grade: evidence.` List Ambiguity, Anacoluthon, Accumulation, Brachylogy, Imprecision, Semicolon, and Comma in that order. State the final grade directly; do not narrate deliberation or retract a grade.

For one passage, give a one-sentence clarity-based `Verdict`. For parallel drafts, complete the same seven-fault audit for each draft, then recommend the clearer draft with at least one explicit paired difference: name the corresponding construction or relation in both drafts and explain the changed effect. Do not present a rewrite unless asked.

If revision was not requested, write `Revision: Not requested.` If the prompt says `revise only if needed` and all seven grades are `None`, write `Revision: No revision needed.`

Source boundaries and quotation locations are recorded in `references/notes.md`.
