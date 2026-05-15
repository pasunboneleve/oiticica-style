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
        "positive": "A public-domain source model from Dickens's Bleak House, chapter 1: a fog passage that gives visible city details.",
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
        "positive": "A public-domain source model from Stevenson's Treasure Island, chapter 1: Billy Bones arrives and the danger begins in sequence.",
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
        "positive": "A public-domain source model from Federalist No. 10: a claim about faction is tested by cause and consequence.",
        "negative": "Liberty is noble, sacred, splendid, and bright; tyranny is base, dark, hateful, and low.",
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
        "positive": "A public-domain source model from Austen's Pride and Prejudice, chapter 1: balanced social irony with grammar, economy, clarity, rhythm, point of view, and force.",
        "negative": "The meeting was, in every possible respect, a very excellent and successful occasion of general improvement.",
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
        "positive": "A public-domain source model from Eliot's Middlemarch, chapter 1: a long sentence whose agreement and reference stay intact.",
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
        "positive": "A public-domain source model from Austen's Pride and Prejudice: standard syntax preserves social tone; no source wording is supplied.",
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
        "positive": "A public-domain source model from Charlotte Bronte's Jane Eyre, chapter 1: source spelling is preserved while commentary uses modern spelling.",
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
        "positive": "A public-domain source model from Milton's Paradise Lost, book 1: the coined place-name Pandemonium follows recognizable English and Latin-derived morphology.",
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
        "positive": "A public-domain source model from Conan Doyle's Sherlock Holmes stories: observation and inference are kept as distinct mental acts.",
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
        "positive": "A public-domain source model from Conrad's Heart of Darkness, chapter 1: nautical terms name exact things aboard the Nellie.",
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
        "positive": "A public-domain source model from Federalist No. 51: Latinate constitutional terms remain useful because they name exact political relations.",
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
        "positive": "A public-domain source model from Thackeray's Vanity Fair: a French social term is kept when it names a specific social institution.",
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
        "positive": "A public-domain source model from Shakespeare's Hamlet, act 1, scene 3: archaic wording is kept because the wording is the source.",
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
        "positive": "A public-domain source model from Wells's The Time Machine, chapter 1: Time Traveller names a newly imagined role.",
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
        "positive": "A public-domain source model from Lincoln's Gettysburg Address: selected words carry civic argument without surplus explanation.",
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
        "positive": "A public-domain source model from Lincoln's Second Inaugural Address: actors, causes, and consequences remain plain.",
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
        "positive": "A public-domain source model from Henry James's The Turn of the Screw: ambiguity is preserved when uncertainty is the point of view.",
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
        "positive": "A public-domain source model from Shakespeare's King Lear, act 2, scene 4: broken speech is kept when emotion causes the break.",
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
        "positive": "A public-domain source model from Austen's Pride and Prejudice, chapter 1: a periodic sentence whose insertions bear on the final judgment.",
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
        "positive": "A public-domain source model from Stevenson's Treasure Island: short and longer sentences vary during action.",
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
        "positive": "A public-domain source model from Hardy's The Return of the Native: rural nouns name exact landscape features and relations.",
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
        "positive": "A public-domain source model from Federalist No. 10: semicolons keep related political clauses in sequence.",
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
        "positive": "A public-domain source model from Austen's Pride and Prejudice: commas mark parenthetic turns without losing the main clause.",
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
        "positive": "A public-domain source model from Melville's Moby-Dick, chapter 1: sea prose uses cadence without obscuring action.",
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
        "positive": "A public-domain source model from Tennyson's The Princess: a line where sound pattern is deliberate music.",
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
        "positive": "A public-domain source model from Poe's The Raven: vowel echo sustains the poem's sound design.",
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
        "positive": "A public-domain source model from Coleridge's The Rime of the Ancient Mariner: consonant repetition imitates motion.",
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
        "positive": "A public-domain source model from Shakespeare's Hamlet: blank verse uses vowel contact deliberately in its meter.",
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
        "positive": "A public-domain source model from Shakespeare's Sonnet 18: iambic pentameter can be scanned by stress to explain emphasis.",
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
        "positive": "A public-domain source model from the King James Bible, Ecclesiastes 3: balanced clauses make sound and sense reinforce each other.",
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
        "positive": "A public-domain source model from Austen's Emma, chapter 1: exact social observation belongs to that character and household.",
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
        "positive": "A public-domain source model from Dickens's Bleak House, chapter 1: legal fog and actual fog meet in one image.",
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
        "positive": "A public-domain source model from Melville's Moby-Dick: ship, sea, force, and action are carried by strong verbs.",
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
        "positive": "A public-domain source model from Wordsworth's Composed upon Westminster Bridge: inversion places the landscape under stress.",
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
        "positive": "A public-domain source model from Federalist No. 51: the angels/men antithesis sharpens the political judgment.",
        "negative": "We are not merely shipping code; we are deciding destiny.",
    },
]


SOURCE_NOTES = {
    "description": ("Charles Dickens", "Bleak House", "chapter 1", "Positive model is a paraphrase of the fog description, not a quotation."),
    "narration": ("Robert Louis Stevenson", "Treasure Island", "chapter 1", "Positive model is a paraphrase of Billy Bones's arrival and the first threat sequence."),
    "dissertation": ("James Madison", "Federalist No. 10", "", "Positive model is a paraphrase of the faction argument, not a quotation."),
    "style-qualities": ("Jane Austen", "Pride and Prejudice", "chapter 1", "Positive model is a paraphrase of Austen's balanced social irony, not a quotation."),
    "correctness": ("George Eliot", "Middlemarch", "chapter 1", "Positive model is a paraphrase of Eliot's controlled long syntax, not a quotation."),
    "solecism": ("Jane Austen", "Pride and Prejudice", "", "Positive model is a paraphrase of Austen dialogue, not a quotation."),
    "spelling": ("Charlotte Bronte", "Jane Eyre", "chapter 1", "Positive model is about preserving source spelling in quotation while modernizing commentary."),
    "word-formation": ("John Milton", "Paradise Lost", "book 1", "Positive model refers to Milton's coined place-name Pandemonium."),
    "confused-words": ("Arthur Conan Doyle", "Sherlock Holmes stories", "", "Positive model is a paraphrase of Holmes's distinction between observation and inference."),
    "foreignism": ("Joseph Conrad", "Heart of Darkness", "chapter 1", "Positive model is a paraphrase of nautical diction aboard the Nellie, not a quotation."),
    "latinism": ("James Madison", "Federalist No. 51", "", "Positive model is a paraphrase of constitutional diction, not a quotation."),
    "gallicism": ("William Makepeace Thackeray", "Vanity Fair", "", "Positive model is a paraphrase of social French loanword use, not a quotation."),
    "archaism": ("William Shakespeare", "Hamlet", "act 1, scene 3", "Positive model refers to archaic wording preserved because it is source language."),
    "neologism": ("H. G. Wells", "The Time Machine", "chapter 1", "Positive model refers to the Time Traveller naming a new imagined role."),
    "concision": ("Abraham Lincoln", "Gettysburg Address", "", "Positive model is a paraphrase of Lincoln's compressed civic argument, not a quotation."),
    "clarity": ("Abraham Lincoln", "Second Inaugural Address", "", "Positive model is a paraphrase of Lincoln's plain cause-and-consequence structure."),
    "ambiguity": ("Henry James", "The Turn of the Screw", "", "Positive model is a paraphrase of point-of-view uncertainty, not a quotation."),
    "anacoluthon": ("William Shakespeare", "King Lear", "act 2, scene 4", "Positive model is a paraphrase of broken syntax caused by emotion."),
    "accumulation": ("Jane Austen", "Pride and Prejudice", "chapter 1", "Positive model is a paraphrase of Austen's controlled periodic syntax."),
    "brachylogy": ("Robert Louis Stevenson", "Treasure Island", "", "Positive model is a paraphrase of sentence-length variation in action scenes."),
    "precision": ("Thomas Hardy", "The Return of the Native", "", "Positive model is a paraphrase of Hardy's exact rural nouns, not a quotation."),
    "semicolon": ("James Madison", "Federalist No. 10", "", "Positive model is a paraphrase of related political clauses, not a quotation."),
    "comma": ("Jane Austen", "Pride and Prejudice", "", "Positive model is a paraphrase of comma-managed parenthesis, not a quotation."),
    "harmony": ("Herman Melville", "Moby-Dick", "chapter 1", "Positive model is a paraphrase of cadence in sea prose, not a quotation."),
    "cacophony": ("Alfred Tennyson", "The Princess", "", "Positive model is a paraphrase of deliberate musical sound patterning."),
    "assonance": ("Edgar Allan Poe", "The Raven", "", "Positive model is a paraphrase of vowel echo, not a quotation."),
    "alliteration": ("Samuel Taylor Coleridge", "The Rime of the Ancient Mariner", "", "Positive model is a paraphrase of consonant repetition used for motion."),
    "hiatus": ("William Shakespeare", "Hamlet", "", "Positive model is a paraphrase of deliberate vowel contact in blank verse."),
    "meter": ("William Shakespeare", "Sonnet 18", "", "Positive model refers to iambic pentameter scanned by stress."),
    "prose-rhythm": ("King James Bible translators", "Ecclesiastes", "chapter 3", "Positive model is a paraphrase of balanced clause rhythm, not a quotation."),
    "originality": ("Jane Austen", "Emma", "chapter 1", "Positive model is a paraphrase of exact social observation, not a quotation."),
    "image": ("Charles Dickens", "Bleak House", "chapter 1", "Positive model is a paraphrase of the Chancery fog image, not a quotation."),
    "vigor": ("Herman Melville", "Moby-Dick", "", "Positive model is a paraphrase of strong sea-action verbs, not a quotation."),
    "inversion": ("William Wordsworth", "Composed upon Westminster Bridge", "", "Positive model is a paraphrase of poetic inversion used for emphasis."),
    "antithesis": ("James Madison", "Federalist No. 51", "", "Positive model refers to the men/angels antithesis."),
}


def title(name: str) -> str:
    return " ".join(part.capitalize() for part in name.split("-"))


def yaml_string(value: str) -> str:
    return json.dumps(value)


def skill_md(spec: dict[str, object]) -> str:
    name = spec["name"]
    skill_name = f"oiticica-{name}"
    title_name = title(str(name))
    description = str(spec["concept"]).rstrip(".")
    rules = "\n".join(f"- {rule}" for rule in spec["rules"])
    rubric = "\n".join(f"- {item}" for item in spec["rubric"])
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

Do not invent source quotations. If an example is labeled as a paraphrase or invented passage, preserve that boundary in the review.
When a task asks for a `Preserve` section, copy the supplied example text exactly; do not replace it with imagined source prose.
"""


def openai_yaml(spec: dict[str, object]) -> str:
    name = str(spec["name"])
    skill = f"oiticica-{name}"
    title_name = title(name)
    concept = str(spec["concept"]).rstrip(".")
    return f"""interface:
  display_name: {yaml_string(f"Oiticica {title_name}")}
  short_description: {yaml_string(concept)}
  default_prompt: {yaml_string(f"Use ${skill} to review English prose with a concrete Weak/Fault/Better/Why contrast.")}
"""


def notes_md(spec: dict[str, object]) -> str:
    name = str(spec["name"])
    skill = f"oiticica-{name}"
    author, work, location, note = SOURCE_NOTES[name]
    location_line = f"\n- Location: {location}" if location else ""
    return f"""# Notes for {skill}

## Modern English Example Boundary

The positive eval example is a source-model paraphrase, not a quotation. The negative eval example is an invented weak passage used for contrast unless this file says otherwise.

## Positive Model Source

- Author or source: {author}
- Work: {work}{location_line}
- Boundary: {note}

## Positive Eval Example

{spec["positive"]}

## Negative Eval Example

{spec["negative"]}

Boundary: invented weak passage, not a public-domain quotation.
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
                    "Assess this strong public-domain source-model paraphrase.\n\n"
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
                    "Review this invented weak passage.\n\n"
                    f"<example>{negative}</example>"
                ),
                "expected_output": "The response gives a concrete Oiticica contrast and fixes the named fault.",
                "assertions": [
                    f"The output identifies the relevant Oiticica concept as {skill}.",
                    "The output includes Weak, Fault, Better, Why, and Rubric sections, with the supplied example text in Weak and a Better section that repairs the fault.",
                    "The output names a concrete fault in relation, sequence, diction, syntax, sound, or reading rather than saying only unclear, awkward, vague, or verbose.",
                ],
            },
        ],
    }
    return json.dumps(data, indent=2) + "\n"


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
        ok &= write(skill_dir / "SKILL.md", skill_md(spec), args.check)
        ok &= write(skill_dir / "evals" / "evals.json", evals_json(spec), args.check)
        ok &= write(skill_dir / "agents" / "openai.yaml", openai_yaml(spec), args.check)
        ok &= write(skill_dir / "agents" / "notes.md", notes_md(spec), args.check)
    if args.check:
        ok &= readme_has_all_skills()

    if args.check and not ok:
        print("generated files are out of date")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
