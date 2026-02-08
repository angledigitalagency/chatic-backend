import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
load_dotenv()

from agents.storage import Storage
from agents.deliverer import Deliverer
from agents.linguist import Linguist

def main():
    print("\n=== Chatic: Song of the Week Emailer ===\n")
    
    storage = Storage()
    deliverer = Deliverer()
    linguist = Linguist()
    
    # 1. Fetch Songs
    songs = storage.get_all_songs()
    if not songs:
        print("No songs found in Songs_DB. Process some songs first!")
        return

    # 2. Display Options
    print(f"Found {len(songs)} songs:")
    for i, song in enumerate(songs):
        title = song.get('Title', 'Unknown')
        artist = song.get('Artist', 'Unknown')
        print(f"{i+1}. {title} - {artist}")

    # 3. Select Song
    try:
        choice = input("\nEnter song number to send (or 'q' to quit): ").strip()
        if choice.lower() == 'q':
            return
        
        idx = int(choice) - 1
        if idx < 0 or idx >= len(songs):
            print("Invalid selection.")
            return
            
        selected_song = songs[idx]
    except ValueError:
        print("Invalid input.")
        return

    # 4. Prepare Data
    track_info = {
        'title': selected_song.get('Title'),
        'artist': selected_song.get('Artist'),
        'external_url': selected_song.get('Link')
    }
    
    full_lyrics = selected_song.get('Full_Lyrics', '')
    if not full_lyrics:
        print("Warning: No 'Full_Lyrics' found. Process might fail or be empty.")
        confirm = input("Send anyway? (y/n): ").lower()
        if confirm != 'y':
            return

    # 5. Generate Fluency Guide
    print("Analyzing lyrics with Linguist...")
    analysis = linguist.analyze_lyrics(full_lyrics)
    
    # Prioritize Level 1 Target Verbs found in the song
    target_verbs = list(analysis['verb_sentence_map'].keys())
    
    # Fallback to general verbs if no Level 1 verbs found
    if not target_verbs:
        target_verbs = analysis['reference_sheet'].get('Verbs', [])[:5]
        
    guide_data = {
        'target_verbs': target_verbs,
        'top_sentences': analysis['top_sentences']
    }

    # 6. Send
    recipient = input(f"Enter recipient email [default: {os.getenv('EMAIL_HOST_USER')}]: ").strip()
    if not recipient:
        recipient = os.getenv("EMAIL_HOST_USER")

    print(f"\nSending '{track_info['title']}' to {recipient}...")
    
    success = deliverer.send_welcome_email(recipient, track_info, guide_data)
    
    if success:
        print("✅ Email Sent Successfully!")
    else:
        print("❌ Failed to send email.")

if __name__ == "__main__":
    main()
