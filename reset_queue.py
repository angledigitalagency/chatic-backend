from agents.storage import Storage

def reset_queue():
    print("Resetting Queue Status...")
    storage = Storage()
    sheet = storage.get_or_create_sheet()
    if not sheet: return

    ws = sheet.worksheet("Queue")
    # Get all values to look for links
    rows = ws.get_all_values()
    
    # Iterate and clear status (Col 2) for any row with a link
    updates = []
    for i, row in enumerate(rows):
        if i == 0: continue # Skip header
        if row and row[0].startswith("http"):
            # Mark Row i+1, Col 2 as ""
            print(f"Reseting row {i+1}...")
            ws.update_cell(i+1, 2, "") 

    print("Queue Reset Complete.")

if __name__ == "__main__":
    reset_queue()
