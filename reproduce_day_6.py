
import sys
import os
import json

# Add project root to path
sys.path.append('/Users/gatomac/Documents/ifeelsochatty/chatic')

from agents.content_manager import ContentManager

def reproduce_day_6():
    cm = ContentManager()
    
    # Mock data for a song
    track_info = {
        "title": "La Camisa Negra",
        "artist": "Juanes",
        "link": "https://open.spotify.com/track/..."
    }
    
    # Mock song_data with verb_details and lyrics
    song_data = {
        "Full_Lyrics": "Tengo la camisa negra... por la tarde... para ti... sin tu amor...",
        "verb_details": [
            {'Verb': 'tener', 'Sentence': 'Tengo la camisa negra'}, # Logic Candidate
            {'Verb': 'ir', 'Sentence': 'Voy a la playa'}, # Logic Candidate
            {'Verb': 'comer', 'Sentence': 'Quiero comer pizza'}, # Action Candidate
            {'Verb': 'beber', 'Sentence': 'Voy a beber agua'}, # Action Candidate
            {'Verb': 'vivir', 'Sentence': 'Sin ti no puedo vivir'}, # Action Candidate
            {'Verb': 'estar', 'Sentence': 'Hoy mi amor está de luto'} # Logic Candidate (Priority?)
        ]
    }
    
    print("--- Simulating Day 6 Content Generation (Final Boss) ---")
    
    # Generate Day 6
    print("\n--- Generating Day 6 ---")
    # We can call get_day_content directly with index 6
    subject, body, text = cm.get_day_content(6, track_info, song_data)
    
    print(f"Subject: {subject}")
    print("Body Snippet:")
    print(text[:500])
    
    # Save to file for review
    output_filename = "reproduce_day_6.html"
    with open(output_filename, "w") as f:
        f.write(body)
    print(f"Saved to {output_filename}")


if __name__ == "__main__":
    reproduce_day_6()
