import os
import sys
import json
import argparse
from dotenv import load_dotenv
from agents.data_fetcher import DataFetcher
from agents.linguist import Linguist
from agents.content_manager import ContentManager

# Load environment variables (Genius Token, etc)
load_dotenv()

def slugify(text):
    """Simple slugify for folder names."""
    return "".join(c if c.isalnum() else "_" for c in text).lower().strip("_")

def generate_week_content(spotify_url, week_number):
    print(f"\n=== Generating Content for Week {week_number} ===")
    print(f"URL: {spotify_url}")
    
    # 1. Fetch Metadata (Spotify/Genius)
    fetcher = DataFetcher()
    print("Fetching Track Info...")
    track_info = fetcher.get_track_info(spotify_url)
    
    if not track_info:
        print("Error: Could not fetch track info. Check URL.")
        return

    print(f"Track: {track_info['title']} by {track_info['artist']}")
    print(f"Image: {track_info.get('image_url')}")
    
    # 2. Fetch Lyrics
    print("Fetching Lyrics...")
    lyrics = fetcher.fetch_lyrics(track_info['title'], track_info['artist'])
    
    if not lyrics:
        print("Error: Could not fetch lyrics from Genius.")
        return
        
    print(f"Lyrics fetched ({len(lyrics)} chars).")
    
    # 3. Analyze Lyrics (Linguist)
    print("Analyzing Lyrics...")
    linguist = Linguist()
    analysis = linguist.analyze_lyrics(lyrics)
    
    # Prepare Song Data for ContentManager
    song_data = {
        'Full_Lyrics': lyrics,
        'Analysis': analysis # ContentManager uses self.current_analysis, but also looks at song_data.get('Full_Lyrics')
    }
    
    # 4. Generate Content (Day 1-7)
    cm = ContentManager()
    # Pre-load analysis into CM to avoid re-analysis
    cm.current_analysis = analysis 
    
    # Create Output Folder
    # e.g., content/week_01_la_camisa_negra
    song_slug = slugify(track_info['title'])
    folder_name = f"week_{week_number:02d}_{song_slug}"
    output_dir = os.path.join("content", folder_name)
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output Directory: {output_dir}")
    
    # Prepare Metadata for ContentManager & Storage
    # ContentManager expects both 'title'/'artist' (lowercase) and 'track_name'/'Artist' (mixed) in some places
    track_info['track_name'] = track_info['title']
    track_info['Title'] = track_info['title']
    track_info['Artist'] = track_info['artist']
    track_info['Link'] = track_info['external_url']
    
    # Metadata for the week
    metadata = {
        "week": week_number,
        "track_info": track_info,
        "analysis_summary": {
            "top_verbs": [v['lemma'] for v in analysis.get('top_verbs', [])[:5]],
            "sentence_count": len(analysis.get('top_sentences', []))
        }
    }
    
    # Save Metadata
    with open(os.path.join(output_dir, "metadata.json"), "w") as f:
        json.dump(metadata, f, indent=4)
    
    # Generate Days
    for day in range(1, 8):
        print(f"Generating Day {day}...")
        try:
            subject, body_html, body_text = cm.get_day_content(day, track_info, song_data)
            
            if not body_html:
                print(f"Warning: Day {day} returned empty content.")
                continue
                
            # Save HTML
            filename = f"day_{day}.html"
            with open(os.path.join(output_dir, filename), "w") as f:
                f.write(body_html)
            
            # Save Text/Subject for reference (optional, maybe in json?)
            # Let's verify by just printing subject
            print(f"  Saved {filename} | Subject: {subject}")
            
        except Exception as e:
            print(f"Error generating Day {day}: {e}")
            import traceback
            traceback.print_exc()

    print("\n=== Generation Complete ===")
    print(f"Files saved in: {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Weekly Content")
    parser.add_argument("url", help="Spotify Track URL")
    parser.add_argument("week", type=int, help="Week Number (e.g. 1)")
    
    args = parser.parse_args()
    
    generate_week_content(args.url, args.week)
