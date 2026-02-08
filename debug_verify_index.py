
from agents.storage import Storage

s = Storage()
sheet = s.get_or_create_sheet()
ws = sheet.worksheet("Verb_Index")
headers = ws.row_values(1)
print(f"Headers: {headers}")

rows = ws.get_all_records()
if rows:
    first = rows[0]
    print(f"First Entry Keys: {first.keys()}")
    print(f"Sample Conjugated: {first.get('Conjugated')}")
else:
    print("No rows in Verb_Index.")
