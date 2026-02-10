# Email Templates: Static vs Dynamic

This document maps out which parts of the emails are **Standard** (Static) and which parts come from the **CMS Library** (Dynamic).

## Global Variables (All Emails)
- **Static**:
    - Logo / Brand Name (Fluency Radio)
    - Footer Links (Unsubscribe, Website)
    - Colors & Fonts
- **Dynamic (User)**:
    - User First Name (`{{ user_name }}`)
    - Weekly Schedule Status (`{{ week_num }}`)

---

## Day 1: The Hook (Song Intro)
**Goal**: Get them to listen to the song.

- **Static**:
    - "Welcome to Week {{ week_num }}"
    - "Your Song of the Week is..."
    - "Here is why we chose it..." (Generic intro text?)
- **Dynamic (Song Metadata)**:
    - Song Title (`{{ song_title }}`)
    - Artist (`{{ artist }}`)
    - Spotify Link (`{{ spotify_link }}`)
    - Album Art (`{{ art_url }}`)
    - **"The Why"**: A specific paragraph explaining the *grammatical focus* of this song (e.g., "This song uses the Present Perfect tense..."). *Needs a column in Metadata Sheet?*

---

## Day 2: The Melody (Vocabulary & Structure)
**Goal**: Break down 3 key sentences.

- **Static**:
    - "Let's look at the lyrics..."
    - "Notice the pattern..."
- **Dynamic (CMS Rows)**:
    - **Sentence 1**:
        - Original (`{{ sentence_1_es }}`)
        - Translation (`{{ sentence_1_en }}`)
        - Meaning/Context (`{{ note_1 }}`)
        - Audio Clip? (Future)
    - **Sentence 2**: ...
    - **Sentence 3**: ...
    - **Mini-Game Link**: `{{ game_link }}` (with song parameter)

---

## Day 3: Action Verbs
**Goal**: Focus on the *actions* in the song.

- **Static**:
    - "Verbs drive the story..."
- **Dynamic (CMS Rows - Filtered by 'Verb' tag?)**:
    - **Verb 1**:
        - Infinitive (`{{ verb_1 }}`)
        - Conjugated in Song (`{{ verb_1_conj }}`)
        - Meaning (`{{ verb_1_meaning }}`)
        - Example Sentence from Song (`{{ verb_1_sentence }}`)
    - **Verb 2**: ...
    - **Verb 3**: ...

---

## Day 4: Connectors / Prepositions
**Goal**: The "glue" words.

- **Static**:
    - "Little words make a big difference..."
- **Dynamic (CMS Rows - Filtered by 'Connector' tag?)**:
    - **Word 1**: (`{{ connector_1 }}`)
    - Usage Example (`{{ connector_1_example }}`)

---

## Day 5: Conjugation Challenge
- **Static**:
    - "Now it's your turn..."
- **Dynamic**:
    - Quiz Question based on the song verbs?
    - Or just a link to the **Mini-Game** with specific instructions.

---

## Day 6: Review (Deep Dive)
- **Static**:
    - "You've heard it all week..."
- **Dynamic**:
    - Full Lyrics with **Bolded** vocabulary from previous days?
    - "Did you notice..." (Callback to specific lines).

---

## Day 7: Live Session
- **Static**:
    - "Join us live..."
    - Zoom Link.
- **Dynamic**:
    - Time/Date (if variable).
