import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
load_dotenv()

from agents.storage import Storage
from agents.content_manager import ContentManager

def main():
    print("=== Debug: Content Generation (Days 1-7) ===\n")
    
    storage = Storage(product="fluency")
    content_mgr = ContentManager()
    
    # 1. Fetch Song Data
    all_songs = storage.get_all_songs()
    if not all_songs:
        print("No songs found.")
        return
        
    # Use "Despacito" if available, else last one
    target_song = None
    for song in all_songs:
        if "despacito" in song.get('Title', '').lower():
            target_song = song
            break
    
    if not target_song:
        target_song = all_songs[-1]
        
    print(f"Target Song: {target_song.get('Title')} ({target_song.get('Artist')})")
    
    # Fetch Verbs (Q&A)
    verb_details = storage.get_song_verbs(target_song.get('Title'))
    target_song['verb_details'] = verb_details
    print(f"Loaded {len(verb_details)} verb entries from Verb_Index.")
    
    track_info = {'Title': target_song.get('Title'), 'Artist': target_song.get('Artist'), 'Link': target_song.get('Link')}

    # 2. Iterate Days
    for day in range(1, 8):
        print(f"\n--- DAY {day} ---")
        subj, html, text = content_mgr.get_day_content(day, track_info, target_song)
        
        print(f"Subject: {subj}")
        print("Body Preview (Text):")
        print(text)
        print("-" * 20)

if __name__ == "__main__":
    main()
