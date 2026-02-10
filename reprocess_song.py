import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
load_dotenv()

from agents.data_fetcher import DataFetcher
from agents.linguist import Linguist
from agents.storage import Storage

def main():
    print("=== Reprocessing Song (Despacito) ===\n")
    
    # 1. Fetch Lyrics
    print("Fetching lyrics for La Camisa Negra...")
    fetcher = DataFetcher()
    # Using explicit title and artist
    lyrics = fetcher.fetch_lyrics("La Camisa Negra", "Juanes")
    
    if not lyrics:
        print("Failed to fetch lyrics.")
        return
        
    print(f"Lyrics fetched ({len(lyrics)} chars).\n")
    
    # 2. Analyze with NEW Linguist
    print("Analyzing...")
    linguist = Linguist()
    analysis = linguist.analyze_lyrics(lyrics)
    
    # Mock Track Info for Storage
    track_info = {
        'title': 'La Camisa Negra',
        'artist': 'Juanes',
        'external_url': 'https://open.spotify.com/track/27L8sESb3KR79asDUBu8nW', # Real Spotify ID for Juanes
        'image_url': 'https://i.scdn.co/image/ab67616d0000b273e04e76811442c5521404116c' # Real Album Art URL for La Camisa Negra
    }
    
    # Clean up old verbs? 
    # For now, we just append. ContentManager limits to top 3 so duplicates aren't fatal, 
    # but we might see mixed results (some with Q, some without).
    # Ideally Storage.log_song should clear old verbs for this song.
    
    # 4. Update Storage?
    # confirm user wants to overwrite? 
    # Let's just do it for dev.
    
    storage = Storage(product="fluency")
    
    print("\nSelectively updating Storage (Songs_DB)...")
    # We call log_song which updates Songs_DB and appends to Verb_Index
    try:
        storage.log_song(
            track_info,
            analysis['top_sentences'],
            analysis['reference_sheet'],
            analysis['verb_sentence_map'],
            full_lyrics=lyrics
        )
        print("Storage updated.")
    except Exception as e:
        print(f"Storage update failed: {e}")

if __name__ == "__main__":
    main()
