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
        "positive": "A Dickens street passage that names shop signs, fog, mud, and lamps so the reader can place the scene.",
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
        "positive": "The opening pursuit in Stevenson where the black spot, flight, and search advance in order.",
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
        "positive": "A Johnson essay paragraph that states a moral claim, tests it with example, then turns the consequence.",
        "negative": "An essay that stacks admirable nouns about liberty without saying what should be done.",
    },
    {
        "name": "style-qualities",
        "concept": "Style has six essential qualities: correctness, concision, clarity, harmony, originality, and vigor.",
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
        "positive": "Austen's balanced free indirect prose where grammar, economy, clarity, rhythm, personal angle, and force work together.",
        "negative": "A grammatically correct paragraph that is vague, wordy, flat, and borrowed in every phrase.",
    },
    {
        "name": "correctness",
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
        "positive": "A George Eliot sentence whose long structure still keeps agreement and reference intact.",
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
        "positive": "Austen dialogue that uses standard syntax while preserving social tone.",
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
        "positive": "A Bronte passage quoted with edition spelling preserved and surrounding analysis in modern spelling.",
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
        "positive": "Miltonic coinage that follows recognizable English and Latin-derived morphology.",
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
        "positive": "A Conan Doyle sentence that uses inference and observation in their distinct senses.",
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
        "positive": "A Conrad sentence that keeps nautical loanwords because they name exact things.",
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
        "positive": "Newman's prose using Latinate terms where theological distinctions require them.",
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
        "positive": "Thackeray keeping salon where the social institution, not a generic room, is meant.",
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
        "positive": "A Shakespeare quotation kept archaic because the wording is the source.",
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
        "positive": "Wells using scientific terms to name newly imagined machinery and social forms.",
        "negative": "We solutionized the problem through ideational futureproofment.",
    },
    {
        "name": "concision",
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
        "positive": "Hemingway's early story prose where selected details carry the scene without explanation.",
        "negative": "The celestial orb of daytime commenced its ascent above the eastern horizon.",
    },
    {
        "name": "clarity",
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
        "positive": "Orwell's expository prose where actors and consequences are plain.",
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
        "positive": "A Henry James ambiguity preserved when the uncertainty is the point of view.",
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
        "positive": "A Dickens character's broken speech kept because panic causes the break.",
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
        "positive": "Austen's periodic sentence where every insertion bears on the final judgment.",
        "negative": "A one-sentence room description that includes windows, history, furniture, weather, ancestry, and moral commentary.",
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
        "positive": "Stevenson varying short and long sentences during action.",
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
        "positive": "Hardy's rural nouns naming exact tools, plants, and relations.",
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
        "positive": "A Gibbon sentence whose semicolons keep balanced historical clauses in relation.",
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
        "positive": "A Woolf sentence whose commas mark parenthetic turns without losing the main clause.",
        "negative": "The captain, ordered, the sailors, to wait.",
    },
    {
        "name": "harmony",
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
        "positive": "Melville's sea prose when cadence carries swell and pause without obscuring action.",
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
        "positive": "A Tennyson line where sound pattern is deliberate music.",
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
        "positive": "Poe using vowel echo to sustain a poem's sound design.",
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
        "positive": "Coleridge using consonant repetition to imitate motion or pressure.",
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
        "positive": "Blank verse that uses vowel contact deliberately in its meter.",
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
        "positive": "A Shakespeare pentameter line scanned by stress to explain emphasis.",
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
        "positive": "The King James translators balancing clauses so sound and sense reinforce each other.",
        "negative": "A paragraph where every sentence has the same length and syntactic pattern.",
    },
    {
        "name": "originality",
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
        "positive": "Austen's exact social observation that could belong only to that character and room.",
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
        "positive": "Dickens comparing a legal fog to the actual fog around Chancery so image and institution meet.",
        "negative": "Hope was a lighthouse, a sword, a garden, and a river in his heart.",
    },
    {
        "name": "vigor",
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
        "positive": "Conrad naming ship, sea, wind, and action with strong verbs.",
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
        "positive": "A poetic inversion in Wordsworth that places the landscape word under stress.",
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
        "positive": "A Johnson antithesis where opposing clauses sharpen the moral judgment.",
        "negative": "We are not building software; we are creating destiny.",
    },
]


def title(name: str) -> str:
    return " ".join(part.capitalize() for part in name.split("-"))


def skill_md(spec: dict[str, object]) -> str:
    name = spec["name"]
    skill_name = f"oiticica-{name}"
    title_name = title(str(name))
    description = str(spec["concept"]).rstrip(".")
    rules = "\n".join(f"- {rule}" for rule in spec["rules"])
    rubric = "\n".join(f"- {item}" for item in spec["rubric"])
    labels = ", ".join(str(rule).split()[0].strip(".,").lower() for rule in spec["rules"][:3])
    return f"""---
name: {skill_name}
description: Apply Oiticica's {title_name.lower()} concept in modern English with concise rules, objective rubrics, and concrete contrast.
---

# Oiticica {title_name}

Use this skill when reviewing or rewriting English prose where {title_name.lower()} is the controlling issue.

Source concept: {description}.

## Rules

{rules}

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

{rubric}

Pass only when every applicable check passes. If correctness fails, fix or name that failure before judging style.

## English Rule

Apply modern English grammar, punctuation, morphology, idiom, and prosody. Do not transfer Portuguese orthography or grammar into English.

## Eval Hooks

- Positive model: {spec["positive"]}
- Negative model: {spec["negative"]}
- Required labels should be concrete, such as `{labels}` or a more exact local relation.
"""


def evals_json(spec: dict[str, object]) -> str:
    name = spec["name"]
    skill = f"oiticica-{name}"
    positive = str(spec["positive"]).rstrip(".")
    negative = str(spec["negative"]).rstrip(".")
    data = {
        "skill_name": skill,
        "evals": [
            {
                "id": f"{name}-positive-classic-model",
                "name": f"{name} positive classic model",
                "prompt": (
                    f"Use the {skill} skill. Review this English-classic model: {positive}. "
                    "Explain why the passage should be preserved rather than flattened."
                ),
                "expected_output": "The response preserves a strong classic model and judges it by the skill's objective rubric.",
                "assertions": [
                    "The output identifies the relevant Oiticica concept.",
                    "The output says the model should be preserved or treated as strong.",
                    "The output applies at least two objective rubric checks instead of generic praise.",
                ],
            },
            {
                "id": f"{name}-negative-classic-contrast",
                "name": f"{name} negative classic contrast",
                "prompt": (
                    f"Use the {skill} skill. Review this weak English-classic-style passage: {negative}. "
                    "Give one concrete contrast with Weak, Fault, Better, Why, and Rubric."
                ),
                "expected_output": "The response gives a concrete Oiticica contrast and fixes the named fault.",
                "assertions": [
                    "The output includes Weak, Fault, Better, Why, and Rubric sections.",
                    "The output names a concrete broken relation rather than saying only unclear, awkward, or verbose.",
                    "The Better version repairs the fault while preserving the intended meaning.",
                ],
            },
        ],
    }
    return json.dumps(data, indent=2) + "\n"


def readme() -> str:
    entries = "\n".join(
        f"- [`oiticica-{spec['name']}`](src/oiticica-{spec['name']}/SKILL.md): {spec['concept']}"
        for spec in SKILLS
    )
    return f"""# Oiticica style skills

Modern English Codex skills derived from the first part of Jose Oiticica's `Manual de Estilo`.

Each skill isolates one concept, gives shallow rules, applies English grammar and orthography, and includes positive and negative eval cases drawn from English-classic models or imitations.

## Use

Run:

```bash
bash scripts/link_skills.sh
```

The script links only skill directories. It does not install `AGENTS.md` or `CLAUDE.md`.

## Skills

{entries}

## Validation

Static checks:

```bash
python3 -m py_compile scripts/generate_skills.py
python3 scripts/generate_skills.py --check
bash -n scripts/link_skills.sh
```
"""


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
        ok &= write(skill_dir / "SKILL.md", skill_md(spec), args.check)
        ok &= write(skill_dir / "evals" / "evals.json", evals_json(spec), args.check)
    ok &= write(ROOT / "README.md", readme(), args.check)

    if args.check and not ok:
        print("generated files are out of date")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
