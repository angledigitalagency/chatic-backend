
from agents.storage import Storage

s = Storage()
songs = s.get_all_songs()

for song in songs:
    if "Despacito" in song.get("Title", ""):
        print(f"--- Analysis for: {song.get('Title')} ---")
        print(f"Level 1 Verbs: {song.get('Level_1_Verbs')}")
        lyrics = song.get("Full_Lyrics", "")
        print(f"Lyrics Length: {len(lyrics)}")
        print(f"Lyrics Snippet: {lyrics[:200]}...")
