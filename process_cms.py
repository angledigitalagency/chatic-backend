import sys
from agents.storage import Storage
from agents.linguist import Linguist

def process_cms():
    print(f"🔄 Starting CMS Processing...")
    
    storage = Storage()
    sheet = storage.get_or_create_sheet()
    
    cms_tab_name = "CMS_Library"
    try:
        ws = sheet.worksheet(cms_tab_name)
    except:
        print("❌ CMS_Library tab not found.")
        return

    # Fetch all records
    data = ws.get_all_records()
    print(f"Found {len(data)} rows.")
    
    linguist = Linguist()
    
    # Header Mapping
    if not data:
         print("No data in sheet.")
         return
         
    # gspread returns list of dicts. Keys are header names.
    headers = list(data[0].keys())
    
    # Case-Insensitive Header Map
    header_row = ws.row_values(1)
    col_map = {name.lower(): i+1 for i, name in enumerate(header_row)}
    print(f"Columns (Lower): {col_map.keys()}")

    # Helper to get col index
    def get_col_index(name):
        return col_map.get(name.lower())

    updates_made = 0
    
    for i, row in enumerate(data):
        row_idx = i + 2 # 1-based, +1 for header
        
        # Get values safely (keys in row dict match header case from gspread)
        # We need to find the key in row matching 'upload_sentence' ignoring case
        upload_key = next((k for k in row.keys() if k.lower() == 'upload_sentence'), None)
        original_key = next((k for k in row.keys() if k.lower() == 'original_sentence'), None)
        origin_key = next((k for k in row.keys() if k.lower() == 'origin'), None)
        context_key = next((k for k in row.keys() if k.lower() == 'context/meaning'), None)
        tag_key = next((k for k in row.keys() if k.lower() == 'notes/tags'), None)
        diff_key = next((k for k in row.keys() if k.lower() == 'difficulty'), None)
        # Column D is "flag" - check if it exists in keys
        flag_key = next((k for k in row.keys() if k.lower() == 'flag'), None)
        
        upload_text = str(row.get(upload_key, '')).strip() if upload_key else ""
        original_text = str(row.get(original_key, '')).strip() if original_key else ""
        current_origin = str(row.get(origin_key, '')).strip() if origin_key else ""
        current_tags = str(row.get(tag_key, '')).strip() if tag_key else ""
        current_difficulty = str(row.get(diff_key, '')).strip() if diff_key else ""
        current_flag = str(row.get(flag_key, '')).strip() if flag_key else ""

        # Logic: If Flag (D) is PRESENT, skip processing (it's marked 18+ or unsafe)
        if current_flag:
            # print(f"  Row {row_idx}: Skipped due to Flag: {current_flag}")
            continue

        # Logic: Treat upload_Sentence as Master if present
        if upload_text:
            target_text = upload_text
            new_origin = "user_parse"
        else:
            target_text = original_text
            new_origin = current_origin # Keep unless empty?

        if not target_text: continue
        
        # 1. Update Origin Column
        if new_origin != current_origin and new_origin == "user_parse":
            idx = get_col_index('Origin')
            if idx:
                ws.update_cell(row_idx, idx, new_origin)
                print(f"  Row {row_idx}: Origin -> {new_origin}")
                updates_made += 1
        
        # 2. Add 'category:Melody' to Tags if Origin is user_parse
        if new_origin == "user_parse":
            if "melody" not in current_tags.lower():
                new_tags = (current_tags + " | category:Melody").strip(" |")
                idx = get_col_index('Notes/Tags')
                if idx:
                    ws.update_cell(row_idx, idx, new_tags)
                    print(f"  Row {row_idx}: Tags -> {new_tags}")
                    updates_made += 1


        if not target_text: continue
        
        # 1. Update Origin Column
        if new_origin != current_origin:
            idx = get_col_index('Origin')
            if idx:
                ws.update_cell(row_idx, idx, new_origin)
                print(f"  Row {row_idx}: Origin -> {new_origin}")
                updates_made += 1
        
        # 2. Recalculate Difficulty (if missing or user_parse)
        # Simple word count check
        wc = len(target_text.split())
        calc_difficulty = "Easy" if wc < 6 else ("Medium" if wc < 12 else "Hard")
        
        if not current_difficulty or (new_origin == "user_parse" and current_difficulty != calc_difficulty):
             idx = get_col_index('Difficulty')
             if idx:
                ws.update_cell(row_idx, idx, calc_difficulty)
                print(f"  Row {row_idx}: Difficulty -> {calc_difficulty}")
                updates_made += 1
        


    print(f"✅ Processing Complete. {updates_made} updates applied.")

if __name__ == "__main__":
    process_cms()
