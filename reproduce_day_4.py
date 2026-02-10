
import sys
import os
import json

# Add project root to path
sys.path.append('/Users/gatomac/Documents/ifeelsochatty/chatic')

from agents.content_manager import ContentManager

def reproduce_day_4():
    cm = ContentManager()
    
    # Mock data for a song
    track_info = {
        "title": "La Camisa Negra",
        "artist": "Juanes",
        "link": "https://open.spotify.com/track/..."
    }
    
    # Mock lyrics that contain prepositions
    lyrics = """
    Tengo la camisa negra
    hoy mi amor está de luto
    Hoy tengo en el alma una pena
    y es por culpa de tu embrujo
    
    Te voy a decir una cosa
    que no te va a gustar
    pero tengo que ser sincero
    y no puedo callar
    
    Mal de amores
    con la mentira
    sin ti no puedo vivir
    para que te mueras de amor
    """
    
    print("--- Simulating Day 4 Content Generation (Prepositions) ---")
    
    # Analyze Lyrics (Day 0 Step)
    print("Analyzing lyrics...")
    if cm.linguist:
        analysis = cm.linguist.analyze_lyrics(lyrics)
        cm.current_analysis = analysis
        print("Analysis complete.")
        print("Found Prepositions:", list(analysis.get("prep_sentence_map", {}).keys()))
    else:
        print("Error: Liquist not loaded.")
        return
    
    # Generate Day 4 (Prepositions)
    print("\n--- Generating Day 4 (Prepositions) ---")
    subject, body, text = cm._day_4_prepositions(track_info, analysis)
    print(f"Subject: {subject}")
    print("Body Snippet:")
    print(text[:500])
    
    # Save to file for review
    with open("reproduce_day_4_output.html", "w") as f:
        f.write(body)
    print("Saved to reproduce_day_4_output.html")


if __name__ == "__main__":
    reproduce_day_4()
