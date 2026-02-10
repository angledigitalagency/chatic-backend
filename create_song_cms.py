from agents.storage import Storage

def create_cms():
    storage = Storage()
    print("Connecting to Storage...")
    
    # 1. Get existing song data from Master DB
    songs = storage.get_all_songs()
    if not songs:
        print("No songs found in master DB.")
        return

    # Find La Camisa Negra
    camisa = None
    for s in songs:
        if "camisa" in str(s.get("Title", "")).lower():
            camisa = s
            break
    
    if not camisa:
        print("La Camisa Negra (original data) not found.")
        return

    print(f"Found Original Data: {camisa.get('Title')}")

    # 2. Prepare Data for CMS
    # The 'Extracted_Sentences' column format is: "verb:sentence | verb:sentence"
    raw_sentences = camisa.get('Extracted_Sentences', '')
    parts = raw_sentences.split('|')
    
    rows = []
    # Header: Song_Title, Original, Translation, Context/Meaning, Notes/Tags, Difficulty, Approved?, Origin
    for part in parts:
        if ':' in part:
            verb, sentence = part.split(':', 1)
            # Create a row ready for human input
            rows.append([
                camisa.get('Title'),
                sentence.strip(),
                "", # Translation
                "", # Context/Meaning
                f"Verb: {verb.strip()}",
                "Easy",
                "FALSE",
                "original_parse"
            ])
        else:
            if part.strip():
                rows.append([
                    camisa.get('Title'),
                    part.strip(),
                    "",
                    "",
                    "Unknown Context",
                    "Easy",
                    "FALSE",
                    "original_parse"
                ])
    
    # 3. Add to Single CMS Tab (Database Style)
    sheet = storage.get_or_create_sheet()
    if not sheet:
        print("Could not access Master Sheet.")
        return
        
    cms_tab_name = "CMS_Library"
    
    try:
        # Check if tab exists, if not create
        try:
            ws = sheet.worksheet(cms_tab_name)
            print(f"Found existing '{cms_tab_name}'.")
        except:
            header = ["Song_Title", "Original_Sentence", "Translation (ES->EN)", "Context/Meaning", "Notes/Tags", "Difficulty", "Approved?", "Origin"]
            ws = sheet.add_worksheet(title=cms_tab_name, rows=1000, cols=10)
            ws.append_row(header)
            ws.format('A1:H1', {'textFormat': {'bold': True}})
            print(f"Created new tab: '{cms_tab_name}'")

        # Check existing entries to avoid duplicates (naive check)
        existing_rows = ws.get_all_values()
        existing_sentences = set()
        if len(existing_rows) > 1:
            # Assuming Col B is Original_Sentence (idx 1)
            for r in existing_rows[1:]:
                if len(r) > 1: existing_sentences.add(r[1].lower().strip())
        
        new_rows = []
        for r in rows:
            if r[1].lower().strip() not in existing_sentences:
                new_rows.append(r)
        
        if new_rows:
            ws.append_rows(new_rows)
            print(f"Appended {len(new_rows)} new rows to '{cms_tab_name}'.")
        else:
            print(f"No new rows to add (all duplicates).")
            
        print(f"\n✅ CMS Library Updated Successfully!")
        print(f"Check the tab: '{cms_tab_name}'")
        
    except Exception as e:
        print(f"Error updating CMS Library: {e}")

if __name__ == "__main__":
    create_cms()
