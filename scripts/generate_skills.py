#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"


SKILLS = [
    {
        "name": "description",
        "concept": "Description is a sequence of aspects.",
        "rules": [
            "Choose aspects that let the reader see this object, place, or person rather than a generic member of its class.",
            "Separate interior, landscape, type, still-life, and scene work by the kind of aspect being selected.",
            "Omit inventory items that do not distinguish the subject.",
            "Prefer concrete nouns, visible actions, local names, and sensory facts over mood labels.",
        ],
        "rubric": [
            "Every sentence adds a visible or audible aspect.",
            "At least one detail distinguishes this subject from a stock example.",
            "Generic labels such as beautiful, gloomy, splendid, or picturesque are supported by particulars.",
            "The order lets the reader locate the parts without rereading.",
        ],
        "positive": "",
        "negative": "A sunset described only as golden, majestic, beautiful, and beyond words.",
    },
    {
        "name": "narration",
        "concept": "Narration is a sequence of facts or episodes.",
        "rules": [
            "Keep events in causal or temporal order unless a deliberate reversal clarifies cause.",
            "Name the actor, action, obstacle, and result for each episode.",
            "Do not stop the movement for decoration that neither changes the episode nor prepares the next one.",
            "Use summary for routine links and scene for decisive turns.",
        ],
        "rubric": [
            "A reader can list what happened first, next, and last.",
            "Each episode changes the situation.",
            "Motives and consequences are close to the actions they explain.",
            "No descriptive pause hides the main action.",
        ],
        "positive": "",
        "negative": "A battle report that pauses for costumes, weather, and moral reflections before saying who attacked.",
    },
    {
        "name": "dissertation",
        "concept": "Dissertation is a sequence of opinions.",
        "rules": [
            "State the opinion before decorating it.",
            "Give each paragraph one claim and the reason or example that tests it.",
            "Distinguish personal judgment from borrowed authority.",
            "Move from premise to contrast to conclusion, not from conclusion to afterthought.",
        ],
        "rubric": [
            "The main claim is explicit.",
            "Each supporting opinion has evidence or an example.",
            "Transitions name the relation: cause, contrast, concession, or result.",
            "The conclusion follows from the stated sequence.",
        ],
        "positive": "",
        "negative": "Liberty is noble, sacred, splendid, and bright; tyranny is base, dark, hateful, and low.",
    },
    {
        "name": "style-qualities",
        "kind": "quality-audit",
        "concept": "Style has six essential qualities: correctness, concision, clarity, harmony, originality, and vigor.",
        "interface": {
            "display_name": "Oiticica Style Qualities",
            "short_description": "Audit one passage or compare drafts across six style qualities",
            "default_prompt": "Use $oiticica-style-qualities to audit each passage across all six qualities with evidence; compare only parallel drafts or when comparison is requested.",
        },
        "rules": [
            "Judge a passage by all six qualities; do not let one excuse failure in another.",
            "Treat correctness as the floor, not the finish.",
            "Treat concision as minimum effort for maximum expression, not mere shortness.",
            "Treat originality as personal exactness, not novelty for its own sake.",
        ],
        "rubric": [
            "No grammar, spelling, or usage fault blocks comprehension.",
            "No removable word, clause, or example remains.",
            "The thought is easy to grasp on first reading.",
            "Sound, order, specificity, and energy support the meaning.",
        ],
        "positive": "",
        "negative": "The sorrel nag offered me a root … I took it in my hand, and, having smelt it, returned it to him again as civilly as I could.",
        "negative_source": {
            "author": "Jonathan Swift",
            "work": "Gulliver’s Travels",
            "location": "part 4, chapter 2",
            "reference": "Jonathan Swift, Gulliver’s Travels, part 4, chapter 2.",
            "boundary": "Verbatim public-domain excerpt with an editorial ellipsis marking the omitted relative clause.",
        },
        "evals": [
            {
                "id": "style-qualities-positive-single-passage",
                "name": "style qualities positive single passage",
                "prompt": (
                    "Audit this strong public-domain quotation as one passage. Do not rewrite it.\n\n"
                    "<example>It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.</example>"
                ),
                "expected_output": "The response gives one evidenced passing decision for each of the six style qualities and preserves the quotation.",
                "assertions": [
                    "The output gives correctness, concision, clarity, harmony, originality, and vigor one explicit evidenced decision each.",
                    "The output grades all six qualities Pass and does not invent a fault in the supplied strong model.",
                    "The output does not present a revised version of the quotation and explicitly says revision was not requested.",
                ],
            },
            {
                "id": "style-qualities-negative-single-passage",
                "name": "style qualities negative single passage",
                "prompt": (
                    "Audit this public-domain quotation as one passage. Do not rewrite it.\n\n"
                    "<example>The sorrel nag offered me a root … I took it in my hand, and, having smelt it, returned it to him again as civilly as I could.</example>"
                ),
                "expected_output": "The response finds the concision failure and its required vigor consequence, gives evidenced decisions for the other four qualities, and preserves the quotation.",
                "assertions": [
                    "The output gives correctness, concision, clarity, harmony, originality, and vigor one explicit evidenced decision each.",
                    "The output grades concision Fail because 'again' is removable after 'returned it to him', grades vigor Fail because the same redundancy weakens force, and grades the other four qualities Pass.",
                    "The output does not present a revised version of the quotation and explicitly says revision was not requested.",
                ],
            },
            {
                "id": "style-qualities-circumlocution-single-passage",
                "name": "style qualities circumlocution single passage",
                "prompt": (
                    "Audit this public-domain quotation as one passage. Do not rewrite it.\n\n"
                    "<example>I made my preparations with the most studious care.</example>"
                ),
                "expected_output": "The response applies the component skill's direct-verb rule rather than limiting concision to deletion-only evidence.",
                "assertions": [
                    "The output gives correctness, concision, clarity, harmony, originality, and vigor one explicit evidenced decision each.",
                    "The output grades concision Fail and contrasts 'made my preparations' with the shorter direct verb 'prepared'.",
                    "The output grades vigor Fail because 'made my preparations' weakens the main action or verb, and after the diagnostic local contrast it explicitly says revision was not requested.",
                ],
            },
            {
                "id": "style-qualities-parallel-source-comparison",
                "name": "style qualities parallel source comparison",
                "prompt": (
                    "Compare these parallel modern public-domain English renderings across all six style qualities. Do not rewrite either.\n\n"
                    "<draft-a>\n"
                    "3:1 For this cause I, Paul, am the prisoner of Christ Jesus on behalf of you Gentiles,\n"
                    "3:2 if it is so that you have heard of the administration of that grace of God which was given me toward you,\n"
                    "3:3 how that by revelation the mystery was made known to me, as I wrote before in few words,\n"
                    "</draft-a>\n\n"
                    "<draft-b>\n"
                    "3:1 For this reason I, Paul, the prisoner of Christ Jesus for the sake of you Gentiles...\n"
                    "3:2 Surely you have heard about the stewardship of God’s grace that was given to me for you,\n"
                    "3:3 that is, the mystery made known to me by revelation, as I have already written briefly.\n"
                    "</draft-b>"
                ),
                "expected_output": "The response audits both sourced renderings across all six qualities and recommends the rendering that marks the interruption and separates later relations.",
                "assertions": [
                    "The output gives Draft A and Draft B separate decisions for correctness, concision, clarity, harmony, originality, and vigor.",
                    "The output recommends Draft B and supports the comparison with at least one concrete difference in how it marks the interrupted opening or separates the following relations.",
                    "The output does not present a revised version of either quotation and explicitly says revision was not requested.",
                ],
            },
        ],
        "additional_examples": [
            {
                "title": "Circumlocution: Robert Louis Stevenson, Strange Case of Dr Jekyll and Mr Hyde",
                "text": "I made my preparations with the most studious care.",
                "boundary": "Exact public-domain quotation from Henry Jekyll’s Full Statement of the Case.",
            },
            {
                "title": "Parallel Comparison: World English Bible",
                "text": "3:1 For this cause I, Paul, am the prisoner of Christ Jesus on behalf of you Gentiles,\n3:2 if it is so that you have heard of the administration of that grace of God which was given me toward you,\n3:3 how that by revelation the mystery was made known to me, as I wrote before in few words,",
                "boundary": "Exact modern public-domain quotation from Ephesians 3:1–3, with verse numbers and divisions retained and translation footnotes omitted.",
            },
            {
                "title": "Parallel Comparison: Berean Standard Bible",
                "text": "3:1 For this reason I, Paul, the prisoner of Christ Jesus for the sake of you Gentiles...\n3:2 Surely you have heard about the stewardship of God’s grace that was given to me for you,\n3:3 that is, the mystery made known to me by revelation, as I have already written briefly.",
                "boundary": "Exact modern public-domain quotation from Ephesians 3:1–3, with verse numbers and divisions retained.",
            },
        ],
    },
    {
        "name": "style-defects",
        "kind": "defect-audit",
        "concept": "Style has six essential defects corresponding to its six qualities: impurity, prolixity, obscurity, disharmony, banality, and weakness.",
        "interface": {
            "display_name": "Oiticica Style Defects",
            "short_description": "Audit one passage or compare drafts across six style defects",
            "default_prompt": "Use $oiticica-style-defects to audit each passage for six defects with evidence; compare only parallel drafts or when comparison is requested.",
        },
        "rules": [
            "Inspect all six defects for every passage or draft, using the same evidence threshold when comparing parallel work.",
            "Do not presume that sourced, famous, literary, civic, sacred, quoted, grammatical, or intelligible prose is defect-free; preservation forbids silent rewriting, not diagnosis.",
            "Judge a literal translation by English grammar and style unless the task explicitly requires preserving source-language structure.",
            "Assign one textual cause to one primary defect; grade another defect above None only when separate evidence supports it.",
            "Support every non-None grade with a quoted word, relation, or audible pattern; do not rewrite unless asked.",
        ],
        "rubric": [
            "All six defects receive an explicit grade.",
            "Every non-None grade cites concrete textual evidence.",
            "The comparison applies one standard to every draft and explains the verdict.",
            "No rewrite appears unless the user requests one.",
        ],
        "positive": "between you and I",
        "negative": "We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.",
        "examples": [
            {
                "title": "Positive Eval: Impurity",
                "polarity": "Positive: the target defect is present.",
                "source": "William Shakespeare",
                "work": "The Merchant of Venice",
                "location": "act 3, scene 2, Antonio’s letter",
                "text": "between you and I",
                "boundary": "Verbatim public-domain excerpt. The nonstandard pronoun case supplies the impurity without the source sentence’s separate passive construction or sound pattern.",
            },
            {
                "title": "Positive Eval: Prolixity",
                "polarity": "Positive: the target defect is present.",
                "source": "Jonathan Swift",
                "work": "Gulliver’s Travels",
                "location": "part 4, chapter 2",
                "text": "The sorrel nag offered me a root … I took it in my hand, and, having smelt it, returned it to him again as civilly as I could.",
                "boundary": "Verbatim public-domain excerpt with an editorial ellipsis marking the omitted relative clause. ‘Again’ can be deleted after ‘returned it to him’ without changing the event; the retained first clause supplies the pronoun referent without a competing modifier attachment.",
            },
            {
                "title": "Positive Eval: Obscurity",
                "polarity": "Positive: the target defect is present.",
                "source": "Berean Literal Bible",
                "work": "The Gospel According to John",
                "location": "21:15",
                "text": "15 Therefore when they had dined, Jesus says to Simon Peter, “Simon son of John, do you love Me more than these?”",
                "boundary": "Verbatim modern public-domain excerpt with its verse number retained. The excerpt ends after the question; the unresolved comparison supplies the obscurity.",
            },
            {
                "title": "Positive Eval: Disharmony",
                "polarity": "Positive: the target defect is present.",
                "source": "Jonathan Swift",
                "work": "Gulliver’s Travels",
                "location": "part 2, chapter 4",
                "text": "if I had had proper instruments",
                "boundary": "Verbatim public-domain excerpt. The grammatically valid adjacent repeated words supply the disharmony without removable meaning.",
            },
            {
                "title": "Positive Eval: Banality",
                "polarity": "Positive: the target defect is present.",
                "source": "Edward Bulwer-Lytton",
                "work": "Paul Clifford",
                "location": "chapter 1, opening sentence",
                "text": "It was a dark and stormy night",
                "boundary": "Verbatim public-domain excerpt from the opening sentence. Its stock scene-setting supplies the banality.",
            },
            {
                "title": "Positive Eval: Weakness",
                "polarity": "Positive: the target defect is present.",
                "source": "Jonathan Swift",
                "work": "Gulliver’s Travels",
                "location": "part 1, chapter 3",
                "text": "my hat was dragged",
                "boundary": "Verbatim public-domain excerpt. The concise agentless passive motion supplies the weakness without separate removable wording.",
            },
            {
                "title": "Negative Eval: No Defect",
                "polarity": "Negative: none of the six target defects is present.",
                "source": "United States Constitution",
                "work": "Preamble",
                "location": "National Archives transcription",
                "text": "We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.",
                "boundary": "Exact public-domain civic quotation. Its long purpose series, historical spelling and capitalization, repeated verb, and active infinitives give the audit substantial opportunities to overdiagnose.",
            },
            {
                "title": "Parallel Comparison: World English Bible",
                "polarity": "Comparison case: the interrupted construction is left syntactically continuous.",
                "source": "World English Bible",
                "work": "Ephesians",
                "location": "3:1–7",
                "text": "3:1 For this cause I, Paul, am the prisoner of Christ Jesus on behalf of you Gentiles,\n3:2 if it is so that you have heard of the administration of that grace of God which was given me toward you,\n3:3 how that by revelation the mystery was made known to me, as I wrote before in few words,\n3:4 by which, when you read, you can perceive my understanding in the mystery of Christ,\n3:5 which in other generations was not made known to the children of men, as it has now been revealed to his holy apostles and prophets in the Spirit,\n3:6 that the Gentiles are fellow heirs and fellow members of the body, and fellow partakers of his promise in Christ Jesus through the Good News,\n3:7 of which I was made a servant according to the gift of that grace of God which was given me according to the working of his power.",
                "boundary": "Exact modern public-domain quotation with verse numbers and divisions retained and translation footnotes omitted.",
            },
            {
                "title": "Parallel Comparison: Berean Standard Bible",
                "polarity": "Comparison case: the interruption is marked and the following relations are separated.",
                "source": "Berean Standard Bible",
                "work": "Ephesians",
                "location": "3:1–7",
                "text": "3:1 For this reason I, Paul, the prisoner of Christ Jesus for the sake of you Gentiles...\n3:2 Surely you have heard about the stewardship of God’s grace that was given to me for you,\n3:3 that is, the mystery made known to me by revelation, as I have already written briefly.\n3:4 In reading this, then, you will be able to understand my insight into the mystery of Christ,\n3:5 which was not made known to men in other generations as it has now been revealed by the Spirit to God’s holy apostles and prophets.\n3:6 This mystery is that through the gospel the Gentiles are fellow heirs, fellow members of the body, and fellow partakers of the promise in Christ Jesus.\n3:7 I became a servant of this gospel by the gift of God’s grace, given me through the working of His power.",
                "boundary": "Exact modern public-domain quotation with verse numbers and divisions retained.",
            },
        ],
        "evals": [
            {
                "id": "style-defects-positive-impurity",
                "name": "style defects positive impurity",
                "prompt": (
                    "Audit this public-domain quotation for defects of style. Do not rewrite it.\n\n"
                    "<example>between you and I</example>"
                ),
                "expected_output": "The response isolates the nonstandard pronoun case as impurity and does not invent another defect.",
                "assertions": [
                    "The output grades impurity above None with evidence from 'between you and I', while grading the other five defects None.",
                    "The output does not present a revised version of the quotation and explicitly says revision was not requested.",
                ],
            },
            {
                "id": "style-defects-positive-prolixity",
                "name": "style defects positive prolixity",
                "prompt": (
                    "Audit this public-domain quotation for defects of style. Do not rewrite it.\n\n"
                    "<example>The sorrel nag offered me a root … I took it in my hand, and, having smelt it, returned it to him again as civilly as I could.</example>"
                ),
                "expected_output": "The response isolates ‘again’ after ‘returned it to him’ as deletable prolixity.",
                "assertions": [
                    "The output grades prolixity above None with concrete evidence of wording that can be removed or compressed without losing the sentence’s event, while grading the other five defects None.",
                    "The output does not present a revised version of the quotation and explicitly says revision was not requested.",
                ],
            },
            {
                "id": "style-defects-positive-obscurity",
                "name": "style defects positive obscurity",
                "prompt": (
                    "Audit this public-domain quotation from the Berean Literal Bible, John 21:15, for defects of style. Do not rewrite it.\n\n"
                    "<example>15 Therefore when they had dined, Jesus says to Simon Peter, “Simon son of John, do you love Me more than these?”</example>"
                ),
                "expected_output": "The response isolates the unresolved comparison in 'more than these' as obscurity without treating literal-translation notation as defective.",
                "assertions": [
                    "The output grades obscurity above None because 'these' permits more than one plausible referent or comparison, while grading the other five defects None.",
                    "The output does not present a revised version of the quotation and explicitly says revision was not requested.",
                ],
            },
            {
                "id": "style-defects-positive-disharmony",
                "name": "style defects positive disharmony",
                "prompt": (
                    "Audit this public-domain quotation for defects of style. Do not rewrite it.\n\n"
                    "<example>if I had had proper instruments</example>"
                ),
                "expected_output": "The response isolates the audible collision between adjacent repeated words as disharmony.",
                "assertions": [
                    "The output grades disharmony above None with evidence from the audible 'had had' collision, while grading the other five defects None.",
                    "The output does not present a revised version of the quotation and explicitly says revision was not requested.",
                ],
            },
            {
                "id": "style-defects-positive-banality",
                "name": "style defects positive banality",
                "prompt": (
                    "Audit this public-domain quotation for defects of style. Do not rewrite it.\n\n"
                    "<example>It was a dark and stormy night</example>"
                ),
                "expected_output": "The response isolates the stock scene-setting as banality.",
                "assertions": [
                    "The output grades banality above None with evidence from the stock phrase 'dark and stormy night', while grading the other five defects None.",
                    "The output does not present a revised version of the quotation and explicitly says revision was not requested.",
                ],
            },
            {
                "id": "style-defects-positive-weakness",
                "name": "style defects positive weakness",
                "prompt": (
                    "Audit this public-domain quotation for defects of style. Do not rewrite it.\n\n"
                    "<example>my hat was dragged</example>"
                ),
                "expected_output": "The response isolates the concise agentless passive motion as weakness.",
                "assertions": [
                    "The output grades weakness above None because 'was dragged' makes the motion passive without naming its actor, while grading the other five defects None.",
                    "The output does not present a revised version of the quotation and explicitly says revision was not requested.",
                ],
            },
            {
                "id": "style-defects-negative-control",
                "name": "style defects negative control",
                "prompt": (
                    "Audit this public-domain literary quotation for defects of style. Do not rewrite it.\n\n"
                    "<example>We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.</example>"
                ),
                "expected_output": "The response finds no supported defect in a substantial, complex passage and resists shortening or modernizing it.",
                "assertions": [
                    "The output grades all six defects None; in particular, it does not turn the passage's purpose series, historical spelling or capitalization, repeated 'establish', or active infinitives into a non-None grade.",
                    "The output does not present a revised version of the quotation and explicitly says revision was not requested.",
                ],
            },
            {
                "id": "style-defects-parallel-source-comparison",
                "name": "style defects parallel source comparison",
                "prompt": (
                    "Compare these modern public-domain English renderings for defects of style and recommend the clearer rendering. Do not rewrite either.\n\n"
                    "<draft-a>\n"
                    "3:1 For this cause I, Paul, am the prisoner of Christ Jesus on behalf of you Gentiles,\n"
                    "3:2 if it is so that you have heard of the administration of that grace of God which was given me toward you,\n"
                    "3:3 how that by revelation the mystery was made known to me, as I wrote before in few words,\n"
                    "3:4 by which, when you read, you can perceive my understanding in the mystery of Christ,\n"
                    "3:5 which in other generations was not made known to the children of men, as it has now been revealed to his holy apostles and prophets in the Spirit,\n"
                    "3:6 that the Gentiles are fellow heirs and fellow members of the body, and fellow partakers of his promise in Christ Jesus through the Good News,\n"
                    "3:7 of which I was made a servant according to the gift of that grace of God which was given me according to the working of his power.\n"
                    "</draft-a>\n\n"
                    "<draft-b>\n"
                    "3:1 For this reason I, Paul, the prisoner of Christ Jesus for the sake of you Gentiles...\n"
                    "3:2 Surely you have heard about the stewardship of God’s grace that was given to me for you,\n"
                    "3:3 that is, the mystery made known to me by revelation, as I have already written briefly.\n"
                    "3:4 In reading this, then, you will be able to understand my insight into the mystery of Christ,\n"
                    "3:5 which was not made known to men in other generations as it has now been revealed by the Spirit to God’s holy apostles and prophets.\n"
                    "3:6 This mystery is that through the gospel the Gentiles are fellow heirs, fellow members of the body, and fellow partakers of the promise in Christ Jesus.\n"
                    "3:7 I became a servant of this gospel by the gift of God’s grace, given me through the working of His power.\n"
                    "</draft-b>"
                ),
                "expected_output": "The response applies the same audit to both modern sourced renderings and prefers the one that marks the interrupted thought and separates later relations.",
                "assertions": [
                    "The output gives each supplied rendering its own complete six-defect audit.",
                    "The output identifies at least one concrete attachment or dependency problem in Draft A and explains which corresponding relation Draft B makes more explicit.",
                    "The output recommends Draft B as clearer and supports the verdict with at least one evidenced difference between the renderings.",
                    "The output does not present a revised version of either quotation and explicitly says revision was not requested.",
                ],
            },
        ],
    },
    {
        "name": "correctness",
        "quality_component": True,
        "concept": "Correctness observes the grammatical tradition of the language being used.",
        "rules": [
            "Apply modern standard English grammar, spelling, idiom, and punctuation unless the task requires dialect or historical form.",
            "Preserve quoted historical language as quotation; modernize only the surrounding instruction.",
            "Fix correctness faults before judging elegance.",
            "Do not import Portuguese grammar rules into English.",
        ],
        "rubric": [
            "Subject, verb, pronoun, modifier, and punctuation choices conform to the intended English register.",
            "Dialect, archaism, or nonstandard form is marked by character, quotation, or purpose.",
            "No correction changes the facts or voice without reason.",
            "The revised sentence remains idiomatic English.",
        ],
        "positive": "",
        "negative": "Between you and I, the committee were unable to decide who they should appoint.",
    },
    {
        "name": "solecism",
        "concept": "Solecism is an error of syntax.",
        "rules": [
            "Find broken agreement, case, government, comparison, modifier attachment, and clause relation.",
            "Name the syntactic relation that fails.",
            "Correct by restoring the relation, not by rewriting the whole passage.",
            "Keep deliberate character speech when the task asks for dialogue or dialect.",
        ],
        "rubric": [
            "The review identifies the exact syntactic fault.",
            "The repair changes only the words needed to restore syntax.",
            "The actor and object remain the same.",
            "The result reads as current standard English.",
        ],
        "positive": "",
        "negative": "Him and me was going to the market when the letters arrived.",
    },
    {
        "name": "spelling",
        "concept": "Cacography is an error of writing; in English practice, treat it as spelling and orthographic error.",
        "rules": [
            "Use the spelling system requested by the user: American, British, or project-local.",
            "Correct misspellings, malformed compounds, capitalization, and apostrophes.",
            "Do not modernize proper names or quoted editions unless asked.",
            "Separate spelling faults from word-choice faults.",
        ],
        "rubric": [
            "The chosen English spelling convention is explicit when relevant.",
            "Every changed word has an orthographic reason.",
            "No proper noun is normalized accidentally.",
            "The correction does not mask a grammar or meaning issue.",
        ],
        "positive": "",
        "negative": "The goverment recieved seperate accomodations for it's officers.",
    },
    {
        "name": "word-formation",
        "concept": "Deformation is an error in the form of a word.",
        "rules": [
            "Find wrong inflections, malformed derivatives, false stems, and invented forms that violate English morphology.",
            "Prefer the established English form unless a technical coinage is needed and well formed.",
            "Do not call a dialect form wrong when dialect is part of the assignment.",
            "Explain the stem, suffix, or inflection that fixes the word.",
        ],
        "rubric": [
            "The faulty form is identified.",
            "The replacement is a real or defensible English word.",
            "The explanation names the morphological pattern.",
            "The sentence keeps its intended meaning.",
        ],
        "positive": "",
        "negative": "The speaker misunderestimated the danger and unpossible results.",
    },
    {
        "name": "confused-words",
        "concept": "Crossing is the exchange of similar words.",
        "rules": [
            "Check near-homophones, lookalikes, and etymological neighbors by meaning in context.",
            "Correct the word that fits the sentence's relation, not the prettier word.",
            "Flag pairs such as affect/effect, imply/infer, flaunt/flout, tortuous/torturous, and disinterested/uninterested.",
            "Explain the contrast in one sentence.",
        ],
        "rubric": [
            "The confused pair is named.",
            "The chosen word matches the sentence's action or relation.",
            "The correction does not introduce a new register mismatch.",
            "The reason would let a reader choose correctly next time.",
        ],
        "positive": "",
        "negative": "The witness inferred that the detective implied the clue from the ash.",
    },
    {
        "name": "foreignism",
        "concept": "Barbarism is abusive use of foreign words or constructions.",
        "rules": [
            "Keep necessary foreign terms when English lacks an exact equivalent or the domain owns the term.",
            "Naturalize or translate needless foreign words that only display learning.",
            "Reject foreign syntax that makes English stiff or unclear.",
            "Do not purge useful loanwords that are established English.",
        ],
        "rubric": [
            "Each foreign term has necessity, domain value, or quotation value.",
            "English idiom governs the sentence.",
            "The review distinguishes loanword from needless display.",
            "The correction improves clarity without narrowing meaning.",
        ],
        "positive": "",
        "negative": "We made a rendezvous for the personnel to assist at the conference.",
    },
    {
        "name": "latinism",
        "concept": "Latinism is foreignness drawn from Latin diction or syntax.",
        "rules": [
            "Use Latinate terms when they are the exact English words for law, science, theology, or rhetoric.",
            "Prefer plain English when Latinate abstraction hides the actor or action.",
            "Avoid Latin word order that strains modern English.",
            "Do not replace a precise technical Latinism with a vague Anglo-Saxon word.",
        ],
        "rubric": [
            "The review separates exact term from pretentious abstraction.",
            "The revision names the actor and action.",
            "Technical meaning survives.",
            "The sentence sounds like modern English, not translated Latin.",
        ],
        "positive": "",
        "negative": "The committee effectuated the termination of the utilization of the facility.",
    },
    {
        "name": "gallicism",
        "concept": "Gallicism is foreignness drawn from French diction or syntax; in English, treat any imported construction by English idiom.",
        "rules": [
            "Keep established French loanwords when they are natural English or exact cultural terms.",
            "Replace French-calqued syntax with idiomatic English order and prepositions.",
            "Do not condemn a loanword merely because it began outside English.",
            "Judge by current English use, clarity, and necessity.",
        ],
        "rubric": [
            "The foreign source is not the sole objection.",
            "The sentence follows English idiom after revision.",
            "Necessary cultural terms remain.",
            "The correction is shorter or clearer than the calque.",
        ],
        "positive": "",
        "negative": "He demanded to his friend if she would assist at the lecture.",
    },
    {
        "name": "archaism",
        "concept": "Archaism is use of an old word or construction now out of use.",
        "rules": [
            "Use archaism only for quotation, historical voice, liturgy, parody, or a precise inherited term.",
            "Replace accidental archaism with current English.",
            "Do not mix archaic grammar with modern diction unless the mixture has a clear purpose.",
            "Preserve archaic classics when quoted; modernize your analysis, not the source.",
        ],
        "rubric": [
            "The archaic form is identified.",
            "Its purpose is stated or rejected.",
            "Modern replacement keeps the meaning.",
            "The passage's register is consistent after revision.",
        ],
        "positive": "",
        "negative": "The product team hath shipped the dashboard unto customers.",
    },
    {
        "name": "neologism",
        "concept": "Neologism is a recently created or introduced word or expression.",
        "rules": [
            "Accept a new word when a new thing, role, process, or distinction needs a name.",
            "Reject novelty that displaces a good existing English word without adding meaning.",
            "Check formation: stem, prefix, suffix, stress, and likely pronunciation.",
            "Prefer the least surprising word that names the new distinction.",
        ],
        "rubric": [
            "The need for the new word is explicit.",
            "The word follows English formation patterns.",
            "No established word would serve as well.",
            "The sentence tells the reader what the new term denotes.",
        ],
        "positive": "",
        "negative": "We solutionized the problem through ideational futureproofment.",
    },
    {
        "name": "concision",
        "quality_component": True,
        "concept": "Concision expresses aspects, facts, or opinions with the fewest words compatible with the other qualities.",
        "rules": [
            "Remove superfluous aspects, episodes, opinions, adjectives, periphrases, redundant clauses, and avoidable subordination.",
            "Do not cut words that carry correctness, clarity, harmony, originality, or vigor.",
            "Prefer the direct noun or verb over a circumlocution.",
            "Keep only details that affect the total impression, action, or argument.",
        ],
        "rubric": [
            "Every retained word changes meaning, rhythm, emphasis, or relation.",
            "No stock adjective repeats what the noun already implies.",
            "Long subordinate clauses are reduced or coordinated when clarity improves.",
            "The shorter version preserves all necessary facts.",
        ],
        "positive": "",
        "negative": "The celestial orb of daytime commenced its ascent above the eastern horizon.",
    },
    {
        "name": "clarity",
        "quality_component": True,
        "concept": "Clarity transmits thought in the form most easily understood.",
        "rules": [
            "Make subject, action, object, condition, and consequence visible.",
            "Separate crowded aspects, facts, or opinions into readable units.",
            "Put conditions before effects when the condition governs the effect.",
            "Repair ambiguity and anacoluthon before polishing sound.",
        ],
        "rubric": [
            "A reader can paraphrase the sentence once, correctly.",
            "Pronouns have single antecedents.",
            "Modifiers attach to the intended words.",
            "Cause, condition, concession, and result are in logical order.",
        ],
        "positive": "",
        "negative": "After reviewing the file, the error was obvious and it was fixed.",
    },
    {
        "name": "ambiguity",
        "concept": "Ambiguity is a structure that allows more than one meaning when only one is intended.",
        "rules": [
            "Find the word, pronoun, modifier, punctuation mark, or clause relation that permits two readings.",
            "State both possible readings.",
            "Revise so only the intended reading remains.",
            "Keep useful literary ambiguity only when the task asks for it.",
        ],
        "rubric": [
            "At least two readings are named.",
            "The intended reading is selected.",
            "The fix removes the unintended reading.",
            "The revision does not flatten deliberate irony or double meaning.",
        ],
        "positive": "",
        "negative": "She saw the man with the telescope and waved.",
    },
    {
        "name": "anacoluthon",
        "concept": "Anacoluthon is a break in logical order, usually by changing the expected subject or construction.",
        "rules": [
            "Track the sentence's announced subject or construction to its grammatical completion.",
            "Flag a break when the sentence starts one structure and finishes another by accident.",
            "Repair by restoring the promised subject, adding the missing link, or splitting the sentence.",
            "Keep deliberate anacoluthon in dramatic speech when it expresses interruption or emotion.",
        ],
        "rubric": [
            "The announced construction is identified.",
            "The point of break is identified.",
            "The repair completes one coherent construction.",
            "Deliberate speech effects are not overcorrected.",
        ],
        "positive": "",
        "negative": "The report, when the auditors finished reading it, they rejected the figures.",
    },
    {
        "name": "accumulation",
        "concept": "Accumulation is excess and crossing of aspects, facts, or opinions in one period.",
        "rules": [
            "Split a period when several independent aspects compete for attention.",
            "Do not make the reader hold an unfinished main clause while unrelated matter intervenes.",
            "Group details by object, action, or relation.",
            "Use one sentence for one main perception, event, or claim unless coordination is the point.",
        ],
        "rubric": [
            "No sentence forces the reader to retain more than one unresolved main relation.",
            "Details are grouped under the thing they describe.",
            "Inserted clauses are necessary and local.",
            "The revision improves clarity without deleting significant facts.",
        ],
        "positive": "",
        "negative": "It was a dark and stormy night; the rain fell in torrents, except at occasional intervals, when it was checked by a violent gust of wind which swept up the streets (for it is in London that our scene lies), rattling along the house-tops, and fiercely agitating the scanty flame of the lamps that struggled against the darkness.",
        "negative_source": {
            "author": "Edward Bulwer-Lytton",
            "work": "Paul Clifford",
            "location": "chapter 1, opening sentence",
            "reference": "Project Gutenberg, Paul Clifford, volume 1, chapter 1.",
            "boundary": "Exact public-domain quotation.",
        },
    },
    {
        "name": "brachylogy",
        "concept": "Brachylogy is the opposite vice of accumulation: too many short, disconnected phrases with forced pauses.",
        "rules": [
            "Join short fragments when they belong to one movement or relation.",
            "Keep short sentences for shock, turn, or emphasis, not as a default texture.",
            "Restore conjunctions or subordination when relation is otherwise unclear.",
            "Do not sacrifice grammar for brevity.",
        ],
        "rubric": [
            "Short units have a reason.",
            "Related actions are connected.",
            "The rhythm varies.",
            "No fragment hides a needed subject, verb, or relation.",
        ],
        "positive": "",
        "negative": "The crowd moved. Shouts. Blades. Blood. Panic. A fall. More shouts.",
    },
    {
        "name": "precision",
        "concept": "Precision uses the exact word or construction for an idea or emotion.",
        "rules": [
            "Choose the word that names the exact object, action, degree, or relation.",
            "Replace approximate intensifiers with measurable or visible terms.",
            "Check that images obey the literal meanings of their words.",
            "Do not trade an exact plain word for an impressive vague one.",
        ],
        "rubric": [
            "The key noun or verb is specific enough to test.",
            "No adjective contradicts the object it modifies.",
            "The word choice narrows meaning rather than inflating tone.",
            "A reader can tell what changed after revision.",
        ],
        "positive": "",
        "negative": "The fervent ice of her cold indifference burned quietly.",
    },
    {
        "name": "semicolon",
        "concept": "The semicolon separates related clauses where a comma is too weak and a period too final.",
        "rules": [
            "Use semicolons for successive conditions before a conclusion, strong adversative turns, parallel clauses with omitted words, and list items that contain internal commas.",
            "Do not use a semicolon between unrelated sentences.",
            "Do not use a comma splice where a semicolon or period is required.",
            "Prefer a comma when the clauses are short and lightly joined.",
        ],
        "rubric": [
            "Both sides of the semicolon are grammatically compatible.",
            "The relation is contrast, parallelism, sequence, or complex listing.",
            "A comma would be ambiguous or too weak.",
            "A period would break a useful relation.",
        ],
        "positive": "",
        "negative": "The moon rose; the soup was cold; sincerity is rare.",
    },
    {
        "name": "comma",
        "concept": "The comma marks coordination, interpolation, parenthesis, apposition, enumeration, ellipsis, inversion, and similar local relations.",
        "rules": [
            "Use commas to show sentence structure, not breathing alone.",
            "Separate introductory conditions, parenthetic material, appositives, coordinate items, and displaced adverbials when needed.",
            "Do not separate a subject from its verb or a verb from its object without an intervening structure.",
            "Use commas to prevent misreading.",
        ],
        "rubric": [
            "Each comma has a named structural job.",
            "No comma interrupts a direct grammatical bond.",
            "Parenthetic and restrictive material are distinguished.",
            "The punctuation removes ambiguity.",
        ],
        "positive": "",
        "negative": "The captain, ordered, the sailors, to wait.",
    },
    {
        "name": "harmony",
        "quality_component": True,
        "concept": "Harmony is the euphonic adjustment of words in the phrase and phrases in the period.",
        "rules": [
            "Read prose aloud when sound or cadence matters.",
            "Avoid accidental cacophony, heavy repetition, and awkward vowel collisions.",
            "Vary sentence length and stress pattern to fit the movement of thought.",
            "Do not improve sound at the cost of correctness or clarity.",
        ],
        "rubric": [
            "The sentence can be read aloud without stumbling.",
            "Repeated sounds are intentional or unobtrusive.",
            "Cadence supports emphasis.",
            "Sound changes do not alter meaning.",
        ],
        "positive": "",
        "negative": "The analysis is is in an area of airy irony.",
    },
    {
        "name": "cacophony",
        "concept": "Cacophony is an ugly or inconvenient sound produced by word contact.",
        "rules": [
            "Find accidental obscene, comic, or clumsy sound joins.",
            "Revise word order or choose a synonym only enough to remove the collision.",
            "Ignore harmless contact when the sentence reads naturally.",
            "Do not make the sentence less exact merely to avoid a faint sound echo.",
        ],
        "rubric": [
            "The offending sound is local and demonstrable by reading aloud.",
            "The revision removes that sound.",
            "Meaning and register remain intact.",
            "The review does not over-police ordinary English joins.",
        ],
        "positive": "",
        "negative": "Ask Ken to pass us some analysis notes.",
    },
    {
        "name": "assonance",
        "concept": "Assonance is repetition of vowel sounds.",
        "rules": [
            "Allow assonance when it is deliberate music, echo, or emphasis.",
            "Flag accidental assonance when it distracts from prose meaning.",
            "Revise by changing one nearby word, not the whole sentence.",
            "Check the sound aloud.",
        ],
        "rubric": [
            "The repeated vowel sound is identified.",
            "The review distinguishes intentional from accidental repetition.",
            "The correction reduces distraction.",
            "Meaning remains exact.",
        ],
        "positive": "",
        "negative": "The pale sale failed mainly in May.",
    },
    {
        "name": "alliteration",
        "concept": "Alliteration is repetition of consonant sounds.",
        "rules": [
            "Keep alliteration when it reinforces action, mood, or memory.",
            "Cut accidental alliteration that turns prose comic or mechanical.",
            "Avoid slogan-like consonant strings in serious exposition.",
            "Prefer exact words over sound play.",
        ],
        "rubric": [
            "The repeated consonant is local and audible.",
            "Its purpose is stated or rejected.",
            "The revision reduces noise without reducing precision.",
            "Any retained pattern serves meaning.",
        ],
        "positive": "",
        "negative": "The platform provides powerful proactive performance possibilities.",
    },
    {
        "name": "hiatus",
        "concept": "Hiatus is collision of vowel sounds in adjacent syllables or words.",
        "rules": [
            "Check vowel collisions that make English prose stumble.",
            "Repair by contraction, reordering, or a more exact word when the collision is distracting.",
            "Do not force old prosody rules onto ordinary modern English.",
            "Keep hiatus when it is natural or metrically intended.",
        ],
        "rubric": [
            "The vowel collision can be heard aloud.",
            "The correction improves ease of reading.",
            "The sentence remains idiomatic.",
            "No exact technical term is lost.",
        ],
        "positive": "",
        "negative": "We agree entirely on airy aerial areas.",
    },
    {
        "name": "meter",
        "concept": "Meter is measured language; Oiticica uses scansion to train the ear for rhythm.",
        "rules": [
            "Use English metrical terms when analyzing English: stress, foot, iamb, trochee, anapest, dactyl, line, caesura.",
            "Do not translate Portuguese syllable-count rules directly into English stress verse.",
            "Scan only when rhythm is relevant to the task.",
            "Use meter as evidence for harmony, not as decoration.",
        ],
        "rubric": [
            "The analysis uses English prosody.",
            "Stressed and unstressed beats are marked or described accurately.",
            "The metrical observation explains an effect.",
            "The review does not impose meter on prose without need.",
        ],
        "positive": "",
        "negative": "Judging an English line only by Portuguese-style syllable count.",
    },
    {
        "name": "prose-rhythm",
        "concept": "Harmony in prose comes from varied rhythmic groups arranged to fit sense.",
        "rules": [
            "Break a prose period into natural spoken groups when cadence matters.",
            "Vary group length to avoid monotony.",
            "Put the strongest word near a stress point or sentence end when possible.",
            "Do not let rhythm obscure grammar or logical order.",
        ],
        "rubric": [
            "The prose has readable groups rather than a flat chain.",
            "Cadence supports the important word.",
            "Long and short units vary with the movement of thought.",
            "The revision can be read aloud smoothly.",
        ],
        "positive": "",
        "negative": "A paragraph where every sentence has the same length and syntactic pattern.",
    },
    {
        "name": "originality",
        "quality_component": True,
        "concept": "Originality presents aspects, facts, or opinions personally, without imitating another's processes or mannerisms.",
        "rules": [
            "Reject stock phrases, borrowed images, and general aspects.",
            "Particularize place, time, object, and action.",
            "Use exact vocabulary instead of novelty hunting.",
            "Let originality arise from observation and relation, not forced strangeness.",
        ],
        "rubric": [
            "The passage contains at least one specific observed relation.",
            "No stock image carries the main effect.",
            "The vocabulary names the subject's own world.",
            "The sentence could not be moved unchanged to any subject of the same class.",
        ],
        "positive": "",
        "negative": "The queen of night spread her silver mantle over the sleeping earth.",
    },
    {
        "name": "image",
        "concept": "An image is an aesthetic relation between objects, phenomena, or actions.",
        "rules": [
            "Name both sides of the relation and the shared quality.",
            "Reject images whose relation is stale, false, or merely decorative.",
            "Prefer a precise image drawn from the subject's world.",
            "Do not mix incompatible images in one sentence.",
        ],
        "rubric": [
            "The image has two clear terms.",
            "The shared relation is concrete.",
            "The image clarifies or intensifies the subject.",
            "No dead metaphor carries the main force.",
        ],
        "positive": "",
        "negative": "Hope was a lighthouse, a sword, a garden, and a river in his heart.",
    },
    {
        "name": "vigor",
        "quality_component": True,
        "concept": "Vigor is energy of expression in aspects, episodes, or conceptions.",
        "rules": [
            "Prefer active construction for movement unless the passive makes the true focus stronger.",
            "Prefer the concrete noun over a nominalized infinitive when English has one.",
            "Use inversion and antithesis only to strengthen emphasis.",
            "Concision and clarity are required conditions for vigor.",
        ],
        "rubric": [
            "The strongest actor or force is visible.",
            "The main verb carries action.",
            "Nominalizations do not bury movement.",
            "The sentence has emphasis without inflation.",
        ],
        "positive": "",
        "negative": "The implementation of the evacuation was effected by the residents.",
    },
    {
        "name": "inversion",
        "concept": "Inversion alters logical word order to give relief, rhythm, or emphasis.",
        "rules": [
            "Use inversion only when it improves emphasis, rhythm, or image placement.",
            "Keep modern English syntax intelligible.",
            "Reject violent or archaic inversion that calls attention to itself.",
            "Compare the inverted order with the direct order before recommending it.",
        ],
        "rubric": [
            "The word moved gains useful emphasis.",
            "The sentence remains idiomatic English.",
            "The inversion does not obscure subject and verb.",
            "The direct order is worse for a named reason.",
        ],
        "positive": "",
        "negative": "Brightly the quarterly report did the manager submit.",
    },
    {
        "name": "antithesis",
        "concept": "Antithesis is the opposition of two truths that clarify each other.",
        "rules": [
            "Use antithesis to make a real contrast, not a decorative balanced phrase.",
            "Keep the two sides grammatically parallel when the contrast depends on balance.",
            "Do not set up a false opposition.",
            "Use contrast to strengthen an idea in dissertation or reflective prose.",
        ],
        "rubric": [
            "Both sides are true or defensible.",
            "The opposition clarifies the main thought.",
            "The grammar lets the reader compare like with like.",
            "The contrast adds force rather than ornament.",
        ],
        "positive": "",
        "negative": "We are not merely shipping code; we are deciding destiny.",
    },
]


SOURCE_NOTES = {
    "description": ("Charles Dickens", "Bleak House", "chapter 1", "Positive model is an exact public-domain quotation."),
    "narration": ("Robert Louis Stevenson", "Treasure Island", "chapter 1", "Positive model is an exact public-domain quotation."),
    "dissertation": ("James Madison", "Federalist No. 10", "", "Positive model is an exact public-domain quotation."),
    "style-qualities": ("Jane Austen", "Pride and Prejudice", "chapter 1", "Positive model is an exact public-domain quotation."),
    "style-defects": ("William Shakespeare", "The Merchant of Venice", "act 3, scene 2", "Positive defect example is an exact public-domain quotation."),
    "correctness": ("George Eliot", "Middlemarch", "chapter 1", "Positive model is an exact public-domain quotation."),
    "solecism": ("Jane Austen", "Pride and Prejudice", "", "Positive model is an exact public-domain quotation."),
    "spelling": ("Charlotte Bronte", "Jane Eyre", "chapter 1", "Positive model is about preserving source spelling in quotation while modernizing commentary."),
    "word-formation": ("John Milton", "Paradise Lost", "book 1", "Positive model refers to Milton's coined place-name Pandemonium."),
    "confused-words": ("Arthur Conan Doyle", "Sherlock Holmes stories", "", "Positive model is an exact public-domain quotation."),
    "foreignism": ("Joseph Conrad", "Heart of Darkness", "chapter 1", "Positive model is an exact public-domain quotation."),
    "latinism": ("James Madison", "Federalist No. 51", "", "Positive model is an exact public-domain quotation."),
    "gallicism": ("William Makepeace Thackeray", "Vanity Fair", "", "Positive model is an exact public-domain quotation."),
    "archaism": ("William Shakespeare", "Hamlet", "act 1, scene 3", "Positive model refers to archaic wording preserved because it is source language."),
    "neologism": ("H. G. Wells", "The Time Machine", "chapter 1", "Positive model refers to the Time Traveller naming a new imagined role."),
    "concision": ("Abraham Lincoln", "Gettysburg Address", "", "Positive model is an exact public-domain quotation."),
    "clarity": ("Abraham Lincoln", "Second Inaugural Address", "", "Positive model is an exact public-domain quotation."),
    "ambiguity": ("Henry James", "The Turn of the Screw", "", "Positive model is an exact public-domain quotation."),
    "anacoluthon": ("William Shakespeare", "King Lear", "act 2, scene 4", "Positive model is an exact public-domain quotation."),
    "accumulation": ("Jane Austen", "Pride and Prejudice", "chapter 1", "Positive model is an exact public-domain quotation."),
    "brachylogy": ("Robert Louis Stevenson", "Treasure Island", "", "Positive model is an exact public-domain quotation."),
    "precision": ("Thomas Hardy", "The Return of the Native", "", "Positive model is an exact public-domain quotation."),
    "semicolon": ("James Madison", "Federalist No. 10", "", "Positive model is an exact public-domain quotation."),
    "comma": ("James Madison", "Federalist No. 10", "", "Positive model is an exact public-domain quotation."),
    "harmony": ("Herman Melville", "Moby-Dick", "chapter 1", "Positive model is an exact public-domain quotation."),
    "cacophony": ("Alfred Tennyson", "The Princess", "", "Positive model is an exact public-domain quotation."),
    "assonance": ("Edgar Allan Poe", "The Raven", "", "Positive model is an exact public-domain quotation."),
    "alliteration": ("Samuel Taylor Coleridge", "The Rime of the Ancient Mariner", "", "Positive model is an exact public-domain quotation."),
    "hiatus": ("William Shakespeare", "Hamlet", "", "Positive model is an exact public-domain quotation."),
    "meter": ("William Shakespeare", "Sonnet 18", "", "Positive model refers to iambic pentameter scanned by stress."),
    "prose-rhythm": ("King James Bible translators", "Ecclesiastes", "chapter 3", "Positive model is an exact public-domain quotation."),
    "originality": ("Jane Austen", "Emma", "chapter 1", "Positive model is an exact public-domain quotation."),
    "image": ("Charles Dickens", "Bleak House", "chapter 1", "Positive model is an exact public-domain quotation."),
    "vigor": ("Herman Melville", "Moby-Dick", "", "Positive model is an exact public-domain quotation."),
    "inversion": ("William Wordsworth", "Composed upon Westminster Bridge", "", "Positive model is an exact public-domain quotation."),
    "antithesis": ("James Madison", "Federalist No. 51", "", "Positive model refers to the men/angels antithesis."),
}

POSITIVE_QUOTES = {
    "description": (
        "Fog up the river, where it flows among green aits and meadows; fog down the river, where it rolls defiled among the tiers of shipping.",
        "Charles Dickens, Bleak House, chapter 1, opening fog sequence.",
    ),
    "narration": (
        "I remember him as if it were yesterday, as he came plodding to the inn door,",
        "Robert Louis Stevenson, Treasure Island, chapter 1.",
    ),
    "dissertation": (
        "The latent causes of faction are thus sown in the nature of man;",
        "Federalist No. 10, paragraph beginning \"The latent causes of faction\".",
    ),
    "style-qualities": (
        "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.",
        "Jane Austen, Pride and Prejudice, chapter 1, opening sentence.",
    ),
    "style-defects": (
        "between you and I",
        "William Shakespeare, The Merchant of Venice, act 3, scene 2, Antonio’s letter, verbatim excerpt.",
    ),
    "correctness": (
        "Miss Brooke had that kind of beauty which seems to be thrown into relief by poor dress.",
        "George Eliot, Middlemarch, book 1, chapter 1, opening sentence.",
    ),
    "solecism": (
        "\"My dear Mr. Bennet,\" said his lady to him one day, \"have you heard that Netherfield Park is let at last?\"",
        "Jane Austen, Pride and Prejudice, chapter 1.",
    ),
    "spelling": (
        "There was no possibility of taking a walk that day.",
        "Charlotte Bronte, Jane Eyre, chapter 1, opening sentence.",
    ),
    "word-formation": (
        "Pandemonium, the high Capital Of Satan and his Peers:",
        "John Milton, Paradise Lost, book 1, lines 756-757.",
    ),
    "confused-words": (
        "You see, but you do not observe.",
        "Arthur Conan Doyle, \"A Scandal in Bohemia\", section 1.",
    ),
    "foreignism": (
        "The Nellie, a cruising yawl, swung to her anchor without a flutter of the sails,",
        "Joseph Conrad, Heart of Darkness, chapter 1, opening sentence.",
    ),
    "latinism": (
        "Ambition must be made to counteract ambition.",
        "Federalist No. 51, paragraph beginning \"But the great security against a gradual concentration\".",
    ),
    "gallicism": (
        "here was George already suffering ennui, and eager for others' society!",
        "William Makepeace Thackeray, Vanity Fair, chapter 25.",
    ),
    "archaism": (
        "Neither a borrower nor a lender be;",
        "William Shakespeare, Hamlet, act 1, scene 3.",
    ),
    "neologism": (
        "The Time Traveller (for so it will be convenient to speak of him)",
        "H. G. Wells, The Time Machine, chapter 1, opening paragraph.",
    ),
    "concision": (
        "government of the people, by the people, for the people, shall not perish from the earth.",
        "Abraham Lincoln, Gettysburg Address, Bliss copy, closing sentence.",
    ),
    "clarity": (
        "Both parties deprecated war; but one of them would make war rather than let the nation survive; and the other would accept war rather than let it perish.",
        "Abraham Lincoln, Second Inaugural Address, paragraph 3.",
    ),
    "ambiguity": (
        "What did it mean? Could it mean anything?",
        "Henry James, The Turn of the Screw, chapter 3.",
    ),
    "anacoluthon": (
        "I will have such revenges on you both, That all the world shall—I will do such things,—",
        "William Shakespeare, King Lear, act 2, scene 4.",
    ),
    "accumulation": (
        "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.",
        "Jane Austen, Pride and Prejudice, chapter 1, opening sentence.",
    ),
    "brachylogy": (
        "I remember him as if it were yesterday, as he came plodding to the inn door, his sea-chest following behind him in a hand-barrow;",
        "Robert Louis Stevenson, Treasure Island, chapter 1.",
    ),
    "precision": (
        "The face of the heath by its mere complexion added half an hour to evening;",
        "Thomas Hardy, The Return of the Native, book 1, chapter 1.",
    ),
    "semicolon": (
        "There are two methods of curing the mischiefs of faction: the one, by removing its causes; the other, by controlling its effects.",
        "Federalist No. 10, paragraph beginning \"There are two methods of curing the mischiefs of faction\".",
    ),
    "comma": (
        "Among the numerous advantages promised by a well constructed union, none deserves to be more accurately developed than its tendency to break and control the violence of faction.",
        "Federalist No. 10, opening sentence.",
    ),
    "harmony": (
        "Whenever I find myself growing grim about the mouth;",
        "Herman Melville, Moby-Dick, chapter 1, paragraph 1.",
    ),
    "cacophony": (
        "The moan of doves in immemorial elms, And murmuring of innumerable bees.",
        "Alfred, Lord Tennyson, The Princess, part VII, song \"Now sleeps the crimson petal\".",
    ),
    "assonance": (
        "Once upon a midnight dreary, while I pondered, weak and weary,",
        "Edgar Allan Poe, \"The Raven\", line 1.",
    ),
    "alliteration": (
        "The fair breeze blew, the white foam flew,",
        "Samuel Taylor Coleridge, The Rime of the Ancient Mariner, part 2.",
    ),
    "hiatus": (
        "To be, or not to be, that is the question:",
        "William Shakespeare, Hamlet, act 3, scene 1.",
    ),
    "meter": (
        "Shall I compare thee to a summer's day?",
        "Shakespeare, Sonnets, Sonnet 18, line 1.",
    ),
    "prose-rhythm": (
        "To every thing there is a season, and a time to every purpose under the heaven:",
        "King James Bible, Ecclesiastes 3:1.",
    ),
    "originality": (
        "Emma Woodhouse, handsome, clever, and rich, with a comfortable home and happy disposition,",
        "Jane Austen, Emma, chapter 1, opening sentence.",
    ),
    "image": (
        "Fog everywhere.",
        "Charles Dickens, Bleak House, chapter 1, opening paragraph.",
    ),
    "vigor": (
        "Call me Ishmael.",
        "Herman Melville, Moby-Dick, chapter 1, opening sentence.",
    ),
    "inversion": (
        "Earth has not anything to show more fair:",
        "William Wordsworth, \"Composed upon Westminster Bridge, September 3, 1802\", line 1.",
    ),
    "antithesis": (
        "If men were angels, no government would be necessary.",
        "Federalist No. 51, paragraph beginning \"It may be a reflection on human nature\".",
    ),
}

for spec in SKILLS:
    spec["positive"] = POSITIVE_QUOTES[str(spec["name"])][0]


def title(name: str) -> str:
    return " ".join(part.capitalize() for part in name.split("-"))


def yaml_string(value: str) -> str:
    return json.dumps(value)


def skill_md(spec: dict[str, object]) -> str:
    name = spec["name"]
    if spec.get("kind") == "quality-audit":
        return style_qualities_skill_md(spec)
    if spec.get("kind") == "defect-audit":
        return style_defects_skill_md(spec)

    skill_name = f"oiticica-{name}"
    title_name = title(str(name))
    description = str(spec["concept"]).rstrip(".")
    rules = "\n".join(f"- {rule}" for rule in spec["rules"])
    rubric = "\n".join(f"- {item}" for item in spec["rubric"])
    aggregate_mode = ""
    if spec.get("quality_component"):
        aggregate_mode = """

## Aggregate Mode

When `$oiticica-style-qualities` invokes this skill as one component of a six-quality audit, apply this skill's Rules and Objective Rubric but defer response shape, length, comparison, and revision decisions to the aggregate skill. Do not emit this skill's standalone `Principle`, `Preserve`, `Weak`, `Fault`, `Better`, `Why`, or `Rubric` sections in aggregate mode."""
    return f"""---
name: {skill_name}
description: Apply Oiticica's {title_name.lower()} concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica {title_name}

Use this skill when reviewing or rewriting English prose where {title_name.lower()} is the controlling issue.

Source concept: {description}.{aggregate_mode}

## Rules

{rules}

## Review Shape

Use the source-model shape for strong models:

```markdown
Principle:
<{skill_name}: one sentence naming the concept>

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
<{skill_name}: one sentence naming the concept>

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

Start `Principle` with the exact skill name `{skill_name}`.
If the prompt says source-model or source-model paraphrase, copy the supplied example in `Preserve` and do not use repair headings.

## Objective Rubric

{rubric}

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Source Boundary

Source notes live in `references/notes.md`.
Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
"""


def style_qualities_skill_md(spec: dict[str, object]) -> str:
    return f"""---
name: oiticica-style-qualities
description: Audit a single English passage or compare parallel drafts using Oiticica's six essential style qualities and their component skills.
---

# Oiticica Style Qualities

Audit every supplied passage. When the user supplies parallel drafts, audit each independently before comparing them.

Source concept: {spec["concept"]}

## Component Skills

Load and apply all six component skills for every audit. These `$` handles are explicit skill invocations, not labels:

- `$oiticica-correctness`
- `$oiticica-concision`
- `$oiticica-clarity`
- `$oiticica-harmony`
- `$oiticica-originality`
- `$oiticica-vigor`

Use each component skill's rules and objective rubric. Do not substitute an unaided general definition of the quality. If the runtime cannot resolve nested skill invocations, use the decision boundaries below rather than omitting a quality.

## Router Mode

When the general `oiticica-style` router invokes this skill as a pipeline stage, apply all six component skills but defer final response shape, total length, and revision decisions to the router. Return the six evidenced decisions to the router; do not emit this skill's standalone audit format.

## Decisions

Give every quality a final `Pass` or `Fail` decision with quoted or otherwise concrete evidence.

- **Correctness**: grammar, spelling, usage, idiom, and punctuation fit the intended English register.
- **Concision**: no word, clause, or example can be removed, and no circumlocution can be replaced by a shorter direct noun or verb, without harming another quality.
- **Clarity**: actor, action, object, attachment, order, and consequence permit one intended reading.
- **Harmony**: sound and cadence support meaning without an accidental collision or stumble.
- **Originality**: exact observation and relation, rather than stock phrasing or borrowed effect, carry the passage.
- **Vigor**: concision and clarity pass, and the strongest actor, force, and main verb remain visible without inflation.

Judge all six; do not let one excuse failure in another. Correctness is the floor, not the finish. Shortness alone does not establish concision, novelty does not establish originality, and an active voice alone does not establish vigor.

Keep the decisions specific. Preserve historically accepted punctuation and usage in a sourced historical quotation; do not fail correctness merely because current convention differs. A grammatical construction does not fail correctness merely because it is awkward; judge its sound under harmony. For concision, require deletion or a shorter direct substitution to preserve logic, tense, necessary emphasis, and voice. When Concision fails, state the exact deletion or substitution and the resulting local phrase. A light verb plus an action noun fails concision when the direct cognate verb preserves the relation: for example, `make preparations` becomes `prepare`. The same construction fails vigor when it moves the main action out of the verb. A modifier that only repeats meaning already entailed by its governing verb fails concision unless the passage supplies evidence of deliberate emphasis. Vigor must `Fail` whenever Concision or Clarity fails, even when the actors and verbs are otherwise strong.

## Response

Keep each audit under 220 words. For each passage or draft, use exactly one line per quality in this form: `Name — Pass/Fail: evidence.` List Correctness, Concision, Clarity, Harmony, Originality, and Vigor in that order. State the final decision directly; do not narrate deliberation or retract a decision.

For one passage, give a one-sentence quality-based `Verdict`. For parallel drafts, complete the same six-quality audit for each draft, then recommend the stronger draft with at least one explicit paired difference: name the corresponding construction or relation in both drafts and explain the changed effect. Do not present a rewrite unless asked.

If revision was not requested, write `Revision: Not requested.` If the prompt says `revise only if needed` and all six qualities pass, write `Revision: No revision needed.`

Source boundaries and quotation locations are recorded in `references/notes.md`.
"""


def style_defects_skill_md(spec: dict[str, object]) -> str:
    return f"""---
name: oiticica-style-defects
description: Audit a single English passage or compare parallel drafts using Oiticica's six essential style defects, with fixed grades and evidence.
---

# Oiticica Style Defects

Audit every supplied passage. When the user supplies parallel drafts, audit each independently before comparing them.

Source concept: {spec["concept"]}

## Decisions

Apply all six. A matching test requires at least `Minor`, even when the prose remains intelligible.

- **Impurity**: a form violates its grammatical role or governing usage. Exempt historically attested spelling, capitalization, and punctuation, deliberate dialect, and editorial notation.
- **Prolixity**: words can be deleted, without substitution, while preserving logic, tense, necessary emphasis, and voice. A shorter rewording is not evidence. An emphatic auxiliary is `None` when deleting it weakens declared emphasis, solemnity, or performative force.
- **Obscurity**: two contextually coherent referents, attachments, or comparison terms survive the whole supplied passage and materially change the relation asserted, or a deictic's discourse role is unclear. Name the readings. Ordinary contextual deixis such as `this place`, `now`, or `before` is `None` when its role is clear even if the quotation does not name the real-world place or time. A choice between a discourse span and that span's named subject is also `None` when it leaves the asserted relation unchanged. A fleeting syntactic possibility that the passage resolves, a semantically implausible referent, or a bare dictionary sense is `None`.
- **Disharmony**: immediately neighboring identical word tokens, or another accidental phonetic collision that distracts when read aloud, even if the construction is grammatical. A repeated word or phrase later in the passage is not adjacent. Repeated content words, parallel coordination, and a deliberate semantic echo are `None` unless they independently create a separate phonetic collision; describe that sound rather than calling the repetition adjacent.
- **Banality**: stock phrasing, generic praise, or borrowed imagery supplies the main effect. A conventional transition, idiom, or functional connective is `None` when it merely carries the logic, even if it is familiar or dispensable; familiarity alone does not satisfy the main-effect test.
- **Weakness**: passive construction, nominalization, abstraction, or inflation buries the main actor, movement, or force. Quote the grammatical construction and name what it buries. A finite `be` auxiliary plus a past participle can supply passive evidence when its subject receives an action, especially in an expression of movement; an absent actor strengthens but is not required for that diagnosis. A passive is `None` when attention properly belongs on its receiver and the actor is visible or immaterial. `Be` plus an `-ing` present participle is progressive, not passive. An active infinitive remains active when its agent is implicit or its recipient is explicit. A copular scene-setting frame such as `It was ...` is stative and therefore `None` when it buries no actor, action, or movement. Gentle tone, an unnamed semantic instigator alone, or the mere possibility of a stronger recast is also `None`. Do not double-count an absent actor as obscurity unless the missing identity is necessary to understand the relation or permits competing readings.

Grade `None` for no evidence, `Minor` for a local defect, and `Major` for a repeated or controlling defect. Quote the evidence and explain why it matches the decision. Assign one textual cause to one primary defect. Do not use prolixity as a fallback: deleting an unclear essential relation is obscurity, repairing sound is disharmony, and making passive action active is weakness. Do not grade a conventional functional transition as banality unless it supplies the passage's main effect.

Do not presume sourced, famous, literary, civic, sacred, quoted, grammatical, or intelligible prose is defect-free. Judge literal translations as English unless source-language structure is explicitly required. Preserve quotations; do not rewrite unless asked.

Source boundaries and quotation locations are recorded in `references/notes.md`.

## Router Mode

When the general `oiticica-style` router invokes this skill as a pipeline stage, apply all six decisions but defer final response shape, total length, follow-up selection, and revision decisions to the router. Return the six evidenced grades to the router; do not emit this skill's standalone audit format.

## Response

Keep each audit under 220 words. For each passage or draft, use exactly one line per defect in this form: `Name — Grade: evidence.` List Impurity, Prolixity, Obscurity, Disharmony, Banality, and Weakness in that order. State the final grade directly; do not narrate deliberation or retract a grade. Then give a one-sentence defect-based `Verdict`, up to three brief evidenced `Follow-up` handles, and `Revision`. A minimal local contrast may prove a diagnosis; do not present a revised passage unless asked.

Map the six defects respectively to `oiticica-correctness`, `oiticica-concision`, `oiticica-ambiguity` or `oiticica-clarity`, `oiticica-harmony`, `oiticica-originality`, and `oiticica-vigor`. Do not run them unless asked.

If revision was not requested, write `Revision: Not requested.` If the prompt says `revise only if needed` and all grades are `None`, write `Revision: No revision needed.`
"""


def openai_yaml(spec: dict[str, object]) -> str:
    name = str(spec["name"])
    skill = f"oiticica-{name}"
    title_name = title(name)
    concept = str(spec["concept"]).rstrip(".")
    interface = spec.get("interface")
    if isinstance(interface, dict):
        display_name = str(interface["display_name"])
        short_description = str(interface["short_description"])
        default_prompt = str(interface["default_prompt"])
        return f"""interface:
  display_name: {yaml_string(display_name)}
  short_description: {yaml_string(short_description)}
  default_prompt: {yaml_string(default_prompt)}
"""

    return f"""interface:
  display_name: {yaml_string(f"Oiticica {title_name}")}
  short_description: {yaml_string(concept)}
  default_prompt: {yaml_string(f"Use ${skill} to review English prose with a concrete Weak/Fault/Better/Why contrast.")}
"""


def notes_md(spec: dict[str, object]) -> str:
    name = str(spec["name"])
    if spec.get("kind") == "defect-audit":
        return style_defects_notes_md(spec)

    skill = f"oiticica-{name}"
    author, work, location, _note = SOURCE_NOTES[name]
    _quote, reference = POSITIVE_QUOTES[name]
    location_line = f"\n- Location: {location}" if location else ""
    additional_examples = "".join(
        f'''\n\n## {example["title"]}\n\n{example["text"]}\n\nBoundary: {example["boundary"]}'''
        for example in spec.get("additional_examples", [])
    )
    negative_source = spec.get("negative_source")
    if isinstance(negative_source, dict):
        negative_boundary = "The positive eval example is a source-model quotation. The negative eval example is a public-domain quotation used for contrast."
        negative_notes = f'''## Negative Eval Source

- Author or source: {negative_source["author"]}
- Work: {negative_source["work"]}
- Location: {negative_source["location"]}
- Reference: {negative_source["reference"]}
- Boundary: {negative_source["boundary"]}

## Negative Eval Example

{spec["negative"]}

Boundary: {negative_source["boundary"]}'''
    else:
        negative_boundary = "The positive eval example is a source-model quotation. The negative eval example is an invented weak passage used for contrast unless this file says otherwise."
        negative_notes = f'''## Negative Eval Example

{spec["negative"]}

Boundary: invented weak passage, not a public-domain quotation.'''
    return f"""# Notes for {skill}

## Modern English Example Boundary

{negative_boundary}

## Positive Model Source

- Author or source: {author}
- Work: {work}{location_line}
- Reference: {reference}
- Boundary: Positive model is an exact public-domain quotation.

## Positive Eval Example

{spec["positive"]}

{negative_notes}{additional_examples}
"""


def style_defects_notes_md(spec: dict[str, object]) -> str:
    sections = []
    for example in spec["examples"]:
        sections.append(
            f'''## {example["title"]}

- Polarity: {example["polarity"]}
- Author or source: {example["source"]}
- Work: {example["work"]}
- Location: {example["location"]}
- Boundary: {example["boundary"]}

### Quotation

{example["text"]}'''
        )

    return """# Notes for oiticica-style-defects

## Eval Polarity

`Positive` means the named target defect is present. `Negative` means none of the six defects is present. Comparison cases test consistent grading across sourced renderings.

## Source Boundary

Every supplied eval passage is a quotation or verbatim excerpt from a public-domain, widely read English work or civic text. No eval fixture is an invented passage or source-model paraphrase.

""" + "\n\n".join(sections) + "\n"


def yaml_scalar(value: str) -> str:
    return json.dumps(value)


def yaml_block(value: str, indent: int) -> str:
    prefix = " " * indent
    return "\n".join(f"{prefix}{line}" if line else prefix.rstrip() for line in value.splitlines())


def evals_yaml(spec: dict[str, object]) -> str:
    name = spec["name"]
    skill = f"oiticica-{name}"
    positive = str(spec["positive"])
    negative_source = spec.get("negative_source")
    negative = str(spec["negative"])
    if not isinstance(negative_source, dict):
        negative = negative.rstrip(".")
    negative_prompt = (
        "Review this public-domain quotation as a weak passage."
        if isinstance(negative_source, dict)
        else "Review this invented weak passage."
    )
    default_evals = [
        {
            "id": f"{name}-positive-classic-model",
            "name": f"{name} positive classic model",
            "prompt": (
                "Assess this strong public-domain source-model quotation.\n\n"
                f"<example>{positive}</example>"
            ),
            "expected_output": "The response names the skill concept, preserves a strong classic model, and judges it by objective rubric checks.",
            "assertions": [
                f"The output identifies the relevant Oiticica concept as {skill}.",
                "The output uses Principle, Preserve, Why, and Rubric sections, and does not use Weak, Fault, or Better as repair headings.",
                "The Rubric applies at least two objective checks from the skill, with pass or fail judgments.",
            ],
        },
        {
            "id": f"{name}-negative-classic-contrast",
            "name": f"{name} negative classic contrast",
            "prompt": (
                f"{negative_prompt}\n\n"
                f"<example>{negative}</example>"
            ),
            "expected_output": "The response gives a concrete Oiticica contrast and fixes the named fault.",
            "assertions": [
                f"The output identifies the relevant Oiticica concept as {skill}.",
                "The output includes Weak, Fault, Better, Why, and Rubric sections, with the supplied example text in Weak and a Better section that repairs the fault.",
                "The output names at least one concrete, skill-relevant fault and its textual evidence rather than saying only unclear, awkward, vague, or verbose.",
            ],
        },
    ]
    evals = spec.get("evals", default_evals)

    lines = [f"skill_name: {yaml_scalar(skill)}", "evals:"]
    for item in evals:
        lines.extend(
            [
                f"  - id: {yaml_scalar(item['id'])}",
                f"    name: {yaml_scalar(item['name'])}",
                "    prompt: |",
                yaml_block(str(item["prompt"]), 6),
                f"    expected_output: {yaml_scalar(item['expected_output'])}",
                "    assertions:",
            ]
        )
        lines.extend(f"      - {yaml_scalar(assertion)}" for assertion in item["assertions"])
    return "\n".join(lines) + "\n"


def readme_has_all_skills() -> bool:
    readme = ROOT / "README.md"
    if not readme.exists():
        print("README.md is missing")
        return False

    text = readme.read_text()
    missing = [
        f"oiticica-{spec['name']}"
        for spec in SKILLS
        if f"(src/oiticica-{spec['name']}/SKILL.md)" not in text
    ]
    if missing:
        print("README.md is missing skill links:")
        for skill in missing:
            print(f"  - {skill}")
        return False
    return True


def write(path: Path, content: str, check: bool) -> bool:
    if check:
        return path.read_text() == content if path.exists() else False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return True


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    ok = True
    for spec in SKILLS:
        skill_dir = SRC / f"oiticica-{spec['name']}"
        stale_json_eval = skill_dir / "evals" / "evals.json"
        ok &= write(skill_dir / "SKILL.md", skill_md(spec), args.check)
        ok &= write(skill_dir / "evals" / "evals.yaml", evals_yaml(spec), args.check)
        ok &= write(skill_dir / "agents" / "openai.yaml", openai_yaml(spec), args.check)
        stale_agent_notes = skill_dir / "agents" / "notes.md"
        ok &= write(skill_dir / "references" / "notes.md", notes_md(spec), args.check)
        if args.check and stale_json_eval.exists():
            print(f"stale generated eval file remains: {stale_json_eval.relative_to(ROOT)}")
            ok = False
        if args.check and stale_agent_notes.exists():
            print(f"stale generated notes file remains: {stale_agent_notes.relative_to(ROOT)}")
            ok = False
        elif not args.check and stale_json_eval.exists():
            stale_json_eval.unlink()
        if not args.check and stale_agent_notes.exists():
            stale_agent_notes.unlink()
    if args.check:
        ok &= readme_has_all_skills()

    if args.check and not ok:
        print("generated files are out of date")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
