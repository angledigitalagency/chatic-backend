
from agents.storage import Storage

s = Storage()
songs = s.get_all_songs()

print("\n--- Verifying Songs_DB Column H (Level_1_Verbs) ---")
for song in songs:
    title = song.get("Title", "Unknown")
    l1_verbs = song.get("Level_1_Verbs", "")
    print(f"Song: {title} | Lev1 Verbs: {l1_verbs}")

print("\n--- Verifying Verb_Index Tenses ---")
sheet = s.get_or_create_sheet()
ws = sheet.worksheet("Verb_Index")
rows = ws.get_all_records()

# Check Tense distribution
tenses = {}
for row in rows:
    t = row.get('Tense', 'Missing')
    tenses[t] = tenses.get(t, 0) + 1

print("\n--- Tense Distribution ---")
for t, count in tenses.items():
    print(f"{t}: {count}")

# Show an example of an Infinitive if found
infinitives = [r for r in rows if r.get('Tense') == 'Infinitive']
if infinitives:
    print(f"\nExample Infinitive: {infinitives[0]}")
# Check Safety
print("\n--- Safety Check ---")
unsafe_rows = [r for r in rows if "UNSAFE" in str(r.get('Safety', ''))]
print(f"Total Unsafe Rows: {len(unsafe_rows)}")
if unsafe_rows:
    print(f"Sample Unsafe: {unsafe_rows[0]}")
else:
    print("No unsafe rows found (Check patterns if expected).")

# Check Extracted Sentences
print("\n--- Extracted Sentences (Count & Samples) ---")
for song in songs:
    title = song.get("Title", "Unknown")
    sentences = song.get("Extracted_Sentences", "").split(" | ")
    print(f"Song: {title} (Count: {len(sentences)})")
    for s in sentences:
        print(f"  - {s}")
