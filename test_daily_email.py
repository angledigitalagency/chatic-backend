import os
import sys
import argparse
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
load_dotenv()

from agents.storage import Storage
from agents.deliverer import Deliverer
from agents.content_manager import ContentManager

def main(target_day, target_email):
    print(f"=== Sending Day {target_day} Email to {target_email} ===\n")
    
    storage = Storage(product="fluency")
    deliverer = Deliverer(identity="fluency")
    content_mgr = ContentManager()
    
    # 1. Fetch Song Data
    all_songs = storage.get_all_songs()
    if not all_songs:
        print("No songs found.")
        return
        
    # Use "La Camisa Negra" if available, else "Despacito", else last one
    target_song = None
    for song in all_songs:
        title = song.get('Title', '').lower()
        if "camisa negra" in title or "juanes" in song.get('Artist', '').lower():
            target_song = song
            break
            
    if not target_song:
        for song in all_songs:
            if "despacito" in song.get('Title', '').lower():
                 target_song = song
                 break
    
    if not target_song:
        target_song = all_songs[-1]
        
    print(f"Song: {target_song.get('Title')} ({target_song.get('Artist')})")
    
    # Fetch Verbs (Q&A)
    verb_details = storage.get_song_verbs(target_song.get('Title'))
    target_song['verb_details'] = verb_details
    
    # 2. Generate Content
    track_info = {'Title': target_song.get('Title'), 'Artist': target_song.get('Artist'), 'Link': target_song.get('Link')}
    
    subject, body_html, body_text = content_mgr.get_day_content(int(target_day), track_info, target_song)
    
    if not subject:
        print(f"No content for Day {target_day}")
        return

    print(f"Subject: {subject}")
    print("Sending...")
    
    # 3. Send
    success = deliverer.send_email(target_email, subject, body_html, body_text)
    if success:
        print("✅ Email Sent!")
    else:
        print("❌ Failed to send.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", required=True, help="Day number (1-7)")
    parser.add_argument("--email", required=True, help="Target email address")
    args = parser.parse_args()
    
    main(args.day, args.email)
