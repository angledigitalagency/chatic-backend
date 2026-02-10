
import sys
import os
import json

# Add project root to path
sys.path.append('/Users/gatomac/Documents/ifeelsochatty/chatic')

from agents.content_manager import ContentManager

def reproduce_day_5():
    cm = ContentManager()
    
    # Mock data for a song
    track_info = {
        "title": "La Camisa Negra",
        "artist": "Juanes",
        "link": "https://open.spotify.com/track/..."
    }
    
    # Mock song_data with verb_details
    # This simulates what Linguist.analyze_lyrics eventually provides or what is aggregated
    song_data = {
        "Full_Lyrics": "Tengo la camisa negra...",
        "verb_details": [
            {'Verb': 'tener', 'Sentence': 'Tengo la camisa negra', 'Question_ES': '¿Qué tienes?'},
            {'Verb': 'estar', 'Sentence': 'hoy mi amor está de luto', 'Question_ES': '¿Cómo está tu amor?'},
            {'Verb': 'ir', 'Sentence': 'Te voy a decir una cosa', 'Question_ES': '¿Qué vas a hacer?'},
            {'Verb': 'decir', 'Sentence': 'Te voy a decir una cosa', 'Question_ES': '¿Qué vas a decir?'},
            {'Verb': 'vivir', 'Sentence': 'sin ti no puedo vivir', 'Question_ES': '¿Puedes vivir?'}
        ]
    }
    
    print("--- Simulating Day 5 Content Generation (Conjugation Timeline) ---")
    
    # Generate Day 5
    print("\n--- Generating Day 5 ---")
    # We can call get_day_content directly with index 5
    subject, body, text = cm.get_day_content(5, track_info, song_data)
    
    print(f"Subject: {subject}")
    print("Body Snippet:")
    print(text[:500])
    
    # Save to file for review
    output_filename = "reproduce_day_5.html"
    with open(output_filename, "w") as f:
        f.write(body)
    print(f"Saved to {output_filename}")


if __name__ == "__main__":
    reproduce_day_5()
