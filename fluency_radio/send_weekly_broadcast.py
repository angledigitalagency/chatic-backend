
import os
import sys
from dotenv import load_dotenv

# Ensure we can import agents
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv()

from agents.storage import Storage
from agents.linguist import Linguist
from fluency_radio.fluency_deliverer import FluencyDeliverer

def main():
    print("\n=== 📻 Fluency Radio: Weekly Broadcast Mockup ===\n")
    
    # Initialize for Fluency Radio
    storage = Storage(product="fluency")
    deliverer = FluencyDeliverer()
    linguist = Linguist()
    
    # 1. Fetch Songs from Fluency DB
    songs = storage.get_all_songs()
    if not songs:
        print("No songs found in Fluency Radio DB. Process some songs first!")
        # For now, let's just warn, as the DB might be empty
        confirm = input("Database is empty. Continue with dummy data? (y/n): ").lower()
        if confirm != 'y':
            return
        songs = [] 
        # Dummy for testing flow if empty
    else: 
        print(f"Found {len(songs)} songs:")
        for i, song in enumerate(songs):
            title = song.get('Title', 'Unknown')
            artist = song.get('Artist', 'Unknown')
            print(f"{i+1}. {title} - {artist}")

    # 3. Select Song (or Dummy)
    selected_song = {}
    if songs:
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
    else:
        # Dummy Data for Logic Testing
        selected_song = {
            'Title': 'Despacito',
            'Artist': 'Luis Fonsi',
            'Link': 'https://open.spotify.com/track/6habFhsOp2Nvsh9m7',
            'Full_Lyrics': "Despacito, quiero respirar tu cuello despacito..."
        }

    # 4. Prepare Data
    track_info = {
        'title': selected_song.get('Title'),
        'artist': selected_song.get('Artist'),
        'external_url': selected_song.get('Link')
    }
    
    full_lyrics = selected_song.get('Full_Lyrics', '')
    
    # 5. Generate Fluency Guide
    print("Analyzing lyrics with Linguist...")
    analysis = linguist.analyze_lyrics(full_lyrics)
    
    # Prioritize Level 1 Target Verbs found in the song
    target_verbs = list(analysis.get('verb_sentence_map', {}).keys())
    
    # Fallback
    if not target_verbs:
        target_verbs = analysis.get('reference_sheet', {}).get('Verbs', [])[:5]
        
    guide_data = {
        'target_verbs': target_verbs,
        'top_sentences': analysis.get('top_sentences', [])
    }

    # 6. Send
    recipient = input(f"Enter recipient email [default: {os.getenv('EMAIL_HOST_USER')}]: ").strip()
    if not recipient:
        recipient = os.getenv("EMAIL_HOST_USER")

    print(f"\nSending '{track_info['title']}' to {recipient} (Fluency Radio Style)...")
    
    # Use FluencyDeliverer to send
    # Note: We might need to extend FluencyDeliverer to support 'send_weekly_guide'
    # For now, let's use the underlying deliverer or add the method.
    
    # Use FluencyDeliverer to send
    success = deliverer.send_weekly_guide(recipient, track_info, guide_data)
    
    if success:
        print("✅ Email Sent Successfully!")
    else:
        print("❌ Failed to send email.")

if __name__ == "__main__":
    main()
