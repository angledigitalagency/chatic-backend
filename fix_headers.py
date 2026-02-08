from agents.storage import Storage
import gspread

def fix_headers():
    print("Fixing Songs_DB Headers...")
    storage = Storage()
    sheet = storage.get_or_create_sheet()
    if not sheet: return

    try:
        ws = sheet.worksheet("Songs_DB")
        # Correct Headers matching the data structure in log_song
        headers = ["Spotify_ID", "Artist", "Title", "Link", "Extracted_Sentences", "Word_Analysis", "Word_Analysis_print", "Level_1_Verbs", "Full_Lyrics", "Last_Updated"]
        
        print(f"Updating Row 1 to: {headers}")
        # update_cell is slow loop, use resize or simple update if available, but for 1 row it's fine.
        # batch update is better
        cell_list = ws.range('A1:J1') # Updated range to include 10th column (J)
        for i, cell in enumerate(cell_list):
            if i < len(headers):
                cell.value = headers[i]
        ws.update_cells(cell_list)
        print("✅ Songs_DB Headers Updated.")

        # Update Verb_Index Headers as well
        try:
            ws_verb = sheet.worksheet("Verb_Index")
            verb_headers = ["Verb", "Conjugated", "Sentence", "Tense", "Difficulty", "Song_Title", "Link", "Safety"]
            print(f"Updating Verb_Index Row 1 to: {verb_headers}")
            cell_list_v = ws_verb.range('A1:H1')
            for i, cell in enumerate(cell_list_v):
                if i < len(verb_headers):
                    cell.value = verb_headers[i]
            ws_verb.update_cells(cell_list_v)
            print("✅ Verb_Index Headers Updated (with Safety).")
        except gspread.WorksheetNotFound:
            print("Verb_Index tab not found, skipping.")
        
    except Exception as e:
        print(f"Error updating headers: {e}")

if __name__ == "__main__":
    fix_headers()
