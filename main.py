import os
import sys
import time
from dotenv import load_dotenv

# Add the project root to the python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables
load_dotenv()

# Check env vars
required_vars = ["SPOTIPY_CLIENT_ID", "SPOTIPY_CLIENT_SECRET", "GENIUS_ACCESS_TOKEN", "EMAIL_HOST_PASSWORD"]
missing = [var for var in required_vars if not os.getenv(var)]
if missing:
    print(f"Error: Missing environment variables: {', '.join(missing)}")
    print("Please check your .env file.")
    sys.exit(1)

# Import Agents
from agents.link_handler import LinkHandler
from agents.data_fetcher import DataFetcher
from agents.linguist import Linguist
from agents.deliverer import Deliverer
from agents.storage import Storage

def main():
    print("\n=== Chatic: Spotify Lyric Linguist (Batch Mode) ===\n")
    
    # Initialize Agents
    try:
        print("Initializing Agents...")
        # LinkHandler used internally if needed, but we trust scraping logic more for now
        data_fetcher = DataFetcher()
        linguist = Linguist()
        # deliverer = Deliverer() # Skipped for batch mode
        storage = Storage()
        print("Agents ready.\n")
    except Exception as e:
        print(f"Error initializing agents: {e}")
        return

    # 1. Fetch Queue
    print("Reading 'Queue' from Google Sheets...")
    queue_items = storage.get_queue_links()
    
    if not queue_items:
        print("No pending links found in Queue. (Make sure you have a 'Queue' tab with links in Column A)")
        return
        
    print(f"Found {len(queue_items)} songs in queue. Processing...\n")

    for i, (row_idx, spotify_link) in enumerate(queue_items, 1):
        print(f"--- Processing {i}/{len(queue_items)}: {spotify_link} ---")
        
        # 2. Fetch Data (Scraping)
        track_info = data_fetcher.get_track_info(spotify_link)
        if not track_info:
            print("Failed to scrape track info. Skipping.")
            storage.update_queue_status(row_idx, "Failed: Scrape Error")
            continue
        
        print(f"Found: {track_info['artist']} - {track_info['title']}")
        
        # 3. Fetch Lyrics
        lyrics = data_fetcher.fetch_lyrics(track_info['title'], track_info['artist'])
        if not lyrics:
            print("Lyrics not found on Genius. Skipping.")
            storage.update_queue_status(row_idx, "Failed: No Lyrics")
            continue

        # 4. Analysis
        analysis_result = linguist.analyze_lyrics(lyrics)
        if not analysis_result:
            print("Linguist analysis failed. Skipping.")
            storage.update_queue_status(row_idx, "Failed: Analysis Error")
            continue
            
        # 5. Storage
        try:
            success = storage.log_song(
                track_info, 
                analysis_result['top_sentences'], 
                analysis_result['reference_sheet'],
                analysis_result['verb_sentence_map'],
                full_lyrics=lyrics # Pass full lyrics
            )
            if success:
                print(f"Logged song: {track_info.get('title')}")
                
                # Highlight Found Verbs (User Request)
                found_verbs = list(analysis_result['verb_sentence_map'].keys())
                if found_verbs:
                    print(f"🔥 Found {len(found_verbs)} Level 1 Verbs: {', '.join(found_verbs)}")
                else:
                    print("⚠️ No Level 1 Verbs found.")
                    
                print("✅ Logged to DB.")
                storage.update_queue_status(row_idx, "Done")
            else:
                 # Even if already exists, mark as Done so we don't process again
                 print("ℹ️  Already in DB.")
                 storage.update_queue_status(row_idx, "Done")
                 
        except Exception as e:
            print(f"❌ Storage Error: {e}")
            storage.update_queue_status(row_idx, f"Error: {str(e)}")
            
            # Rate Limit Handling (Backoff)
            if "429" in str(e):
                print("⚠️ Rate Limit hit. Waiting 60s...")
                time.sleep(60)

        # Rate Limiting (Be gentle with the Free Tier API)
        time.sleep(3) 

    print("\nBatch Processing Complete!")

if __name__ == "__main__":
    main()
