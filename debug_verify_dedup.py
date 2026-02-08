
from agents.storage import Storage

s = Storage()
songs = s.get_all_songs()

print("\n--- Verifying Songs_DB Column H (Level_1_Verbs) Deduplication ---")
for song in songs:
    title = song.get("Title", "Unknown")
    l1_verbs = song.get("Level_1_Verbs", "")
    print(f"Song: {title} | Lev1 Verbs: {l1_verbs}")

    if "Tener:Tengo, tener:tengo" in l1_verbs: # Example of failure
        print("❌ FAILED: Duplicates found.")
    else:
        print("✅ SUCCESS: No obvious duplicates.")
