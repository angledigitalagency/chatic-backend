# Production Workflow Guide & Template Reference

This document outlines the **Standard Operating Procedure (SOP)** for creating and delivering daily email content.

## Phase 1: Ingestion (The "Parser")
**Goal**: Convert raw song data (MP3/Lyrics) into a structured Google Sheet for human review.

1.  **Run Script**: `python ingest_song.py "Song Title"` or `python ingest_song.py "Spotify URL"`
2.  **What Happens**:
    - Fetches Lyrics/Metadata (Genius/Spotify).
    - Runs `Linguist` Analysis (Verbs, Prepositions, etc.).
    - Populates `CMS_Library` Tab in Master Google Sheet.
    - **Note**: Does NOT create HTML files yet.

## Phase 2: Human Review (The "Editor")
**Goal**: Verify and Refine the Content before it goes live.

1.  **Open Master Sheet**: Tab `CMS_Library`.
2.  **Filter**: By `Song_Title`.
3.  **Review Columns**:
    - `Original_Sentence`: Is it clean? (Delete bad ones).
    - `Translation`: Is it accurate? (Edit if needed).
    - `Context/Meaning`: Add cultural notes or grammar tips.
    - `Notes/Tags`: IMPORTANT. Ensure correct category:
        - `Melody`: For Day 2 (Key verbs/structures).
        - `Action`: For Day 3 (Verbs).
        - `Connector`: For Day 4 (Prepositions).
    - `Approved?`: Mark as `TRUE`.
4.  **Save**: Just close the tab.

## Phase 3: Generation (The "Sender")
**Goal**: Create the final emails using APPROVED content.

1.  **Run Script**: `python send_daily_interactions.py` (or `generate_emails.py`).
2.  **What Happens**:
    - Reads `CMS_Library` (Approved=TRUE).
    - Fills Jinja2 Templates (`templates/day_X.html`).
    - Sends Emails (or saves drafts).

---

## Template Reference: Static vs Dynamic

### Day 1: The Hook (Song Intro)
- **Static**: "Welcome", "Song of the Week", "Why we chose it".
- **Dynamic**: `{{ song_title }}`, `{{ artist }}`, `{{ spotify_link }}`, `{{ art_url }}`.

### Day 2: The Melody (Vocabulary & Structure)
- **Static**: "Melodies of Existence", "Listen to the pattern".
- **Dynamic**:
    - `{{ melody_title }}`: The grammatical theme (e.g., "Desire").
    - `{{ melody_concept }}`: Explanation text.
    - `{{ sentences }}`: List of 3 approved rows tagged `Melody`.
        - `{{ sentence.original }}`, `{{ sentence.translation }}`, `{{ sentence.notes }}`.

### Day 3: Action Verbs
- **Static**: "Verbs drive the story".
- **Dynamic**:
    - `{{ verbs }}`: List of 3 approved rows tagged `Action`.
        - `{{ verb.infinitive }}`, `{{ verb.conjugated }}`, `{{ verb.example }}`.

### Day 4: Connectors / Prepositions
- **Static**: "Little words make a big difference".
- **Dynamic**:
    - `{{ connectors }}`: List of 3 approved rows tagged `Connector`.
        - `{{ connector.word }}`, `{{ connector.example }}`.

### Day 5: Conjugation Challenge
- **Static**: "Your turn".
- **Dynamic**: Link to Mini-Game or Quiz Question.

### Day 6: Review
- **Static**: "You've heard it all week".
- **Dynamic**: Full Lyrics + Callback to previous lessons.

### Day 7: Live Session
- **Static**: Zoom Link / Invite.
- **Dynamic**: Time/Date.
