from agents.storage import Storage

def check_cms_updates():
    storage = Storage()
    print("Connecting to CMS...")
    
    sheet = storage.get_or_create_sheet()
    if not sheet: return

    try:
        ws = sheet.worksheet("CMS_Library")
        rows = ws.get_all_records()
        
        print(f"Total Rows in CMS: {len(rows)}")
        
        # Filter for La Camisa Negra updates
        updates = [r for r in rows if "camisa" in str(r.get("Song_Title", "")).lower()]
        
        print("\n--- User Updates (Preview) ---")
        for i, row in enumerate(updates[:5]): # Show first 5
            print(f"Row {i+1}:")
            print(f"  Start: {row.get('Original_Sentence')[:40]}...")
            print(f"  User Translation: {row.get('Translation (ES->EN)')}")
            print(f"  Notes: {row.get('Notes/Tags')}")
            print(f"  Approved: {row.get('Approved?')}")
            print("-" * 30)
            
    except Exception as e:
        print(f"Error reading CMS: {e}")

if __name__ == "__main__":
    check_cms_updates()
