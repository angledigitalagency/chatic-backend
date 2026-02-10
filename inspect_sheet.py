import os
import sys
import json
from dotenv import load_dotenv

# Ensure we can import agents
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
load_dotenv()

from agents.storage import Storage

def inspect():
    print("Inspecting Sheet: 1RqHrKVi_241nKOkCG2hfuTsO3vdpMpIDueiFQm5snXA")
    
    # Initialize Storage but force it to use the Chatic sheet (since that's what the ID matches)
    # or we can just access it directly via gspread if we wanted, but Storage wrapper is easier.
    storage = Storage(product="chatic") 
    
    sheet = storage.get_or_create_sheet()
    print(f"Connected to: {sheet.title}")
    
    try:
        # Check Users Tab
        print("Checking 'Users' tab for recent entries...")
        ws = sheet.worksheet("Users")
        all_values = ws.get_all_values()
        headers = all_values[0]
        rows = all_values[1:]
        
        print(f"Found {len(rows)} users.")
        if rows:
            print("Last 3 Users:")
            for row in rows[-3:]:
                print(row)
    except Exception as e:
        print(f"Error reading Users tab: {e}")

if __name__ == "__main__":
    inspect()
