import sys
from agents.storage import Storage
from agents.linguist import Linguist
from agents.data_fetcher import DataFetcher

def ingest_song(query):
    print(f"🎤 Starting Ingestion for: {query}")
    
    # 1. Fetch Song Data
    print("--- Phase 1: Data Fetching ---")
    data_fetcher = DataFetcher()
    
    # Use genius directly if just a title
    # Assume query is "Title Artist"
    # Simple split heuristic for now
    parts = query.split(' by ')
    if len(parts) == 1:
        parts = query.split(' ') # Rough split if no 'by'
    
    # This part is a bit tricky without robust parsing, 
    # but let's assume "La Camisa Negra Juanes" -> "La Camisa Negra" (Track), "Juanes" (Artist)
    # Actually, let's just use the query as "track" and hope Genius finds it.
    
    # Better: Use DataFetcher.fetch_lyrics(track_name, artist_name)
    # Let's try to extract artist if possible.
    if "juanes" in query.lower():
        artist = "Juanes"
        title = query.lower().replace("juanes", "").strip()
    else:
        artist = "Unknown"
        title = query
        
    print(f"Searching for Title: '{title}', Artist: '{artist}'")
    lyrics = data_fetcher.fetch_lyrics(title, artist)
    
    if not lyrics:
        print("❌ No lyrics found via DataFetcher. Checking Storage backup...")
        # Fallback: Check if we already have it in DB
        storage = Storage()
        songs = storage.get_all_songs()
        for s in songs:
             if title.lower() in str(s.get("Title", "")).lower():
                 lyrics = s.get("Full_Lyrics")
                 print(f"✅ Found lyrics in Storage backup for {s.get('Title')}")
                 break
    
    if not lyrics:
        print("❌ Failed to get lyrics.")
        return

    # 2. Analyze with Linguist
    print("--- Phase 2: Linguistic Analysis ---")
    linguist = Linguist()
    analysis = linguist.analyze_lyrics(lyrics)
    
    if not analysis:
        print("❌ Linguist analysis failed.")
        return

    print("✅ Analysis Complete.")
    
    # 3. Prepare CMS Rows
    print("--- Phase 3: CMS Preparation ---")
    rows_to_add = []
    
    # A. Verbs -> ACTION (Day 3)
    verb_map = analysis.get("verb_sentence_map", {})
    all_verbs = list(verb_map.keys())
    
    # Pick Top 5 Verbs
    for v in all_verbs[:5]:
        entries = verb_map[v]
        entries.sort(key=lambda x: len(x['sentence']))
        best = entries[0]
        
        rows_to_add.append([
            title.title(),
            best['sentence'],
            "", 
            best.get('question_en', ""), 
            f"category:Action | verb:{v} | form:{best['conjugated']}", 
            "Medium",
            "FALSE", 
            "linguist_parse"
        ])
        
    # B. Prepositions -> CONNECTOR (Day 4)
    prep_map = analysis.get("prep_sentence_map", {})
    for p, entries in prep_map.items():
        if len(entries) > 0:
            best = entries[0]
            rows_to_add.append([
                title.title(),
                best['sentence'],
                "",
                f"Connector: {p}",
                f"category:Connector | word:{p}",
                "Easy",
                "FALSE",
                "linguist_parse"
            ])

    # C. Melody Sentences (Day 2) -> General Candidates
    top_sents = analysis.get("top_sentences", [])
    for item in top_sents:
        if ":" in item:
            verb, s = item.split(":", 1)
            rows_to_add.append([
                title.title(),
                s.strip(),
                "", 
                f"Focus: {verb}", 
                f"category:Melody | verb:{verb}", 
                "Easy", 
                "FALSE", 
                "linguist_parse"
            ])
            
    print(f"Generated {len(rows_to_add)} candidate rows.")

    # 4. Push to Sheet
    print("--- Phase 4: Push to Drive ---")
    storage = Storage()
    sheet = storage.get_or_create_sheet()
    
    cms_tab_name = "CMS_Library"
    try:
        ws = sheet.worksheet(cms_tab_name)
    except:
        print(f"Creating new tab: {cms_tab_name}")
        ws = sheet.add_worksheet(cms_tab_name, 1000, 10)
        ws.append_row(["Song_Title", "Original_Sentence", "Translation", "Meaning", "Notes/Tags", "Difficulty", "Approved?", "Origin"])
        
    # Append
    ws.append_rows(rows_to_add)
    print(f"✅ Successfully appended rows to '{cms_tab_name}'")
    print(f"👉 Go review them here: {sheet.url}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ingest_song(sys.argv[1])
    else:
        # Default test
        ingest_song("La Camisa Negra Juanes")
