
import sys
import os
import json

# Add project root to path
sys.path.append('/Users/gatomac/Documents/ifeelsochatty/chatic')

from agents.content_manager import ContentManager

def reproduce_day_3():
    cm = ContentManager()
    
    # Mock data for a song
    track_info = {
        "title": "La Camisa Negra",
        "artist": "Juanes"
    }
    
    # Mock lyrics that contain target verbs
    lyrics = """
    Voy a hacerte una brujería
    para que te mueras de amor por mí
    y quiero que me trates como a ti
    te da la gana
    
    Te voy a decir una cosa
    que no te va a gustar
    pero tengo que ser sincero
    y no puedo callar
    
    Mañana me voy de viaje
    y no sé cuándo volveré
    pero te prometo que siempre
    te recordaré
    
    Estoy muy triste hoy
    porque no tengo tu amor
    quiero estar contigo siempre
    sin ti no puedo vivir
    """
    
    print("--- Simulating Content Generation ---")
    
    # Analyze Lyrics (Day 0 Step)
    print("Analyzing lyrics...")
    # Simulate the flow: ContentManager uses self.linguist to analyze
    # and stores result in self.current_analysis
    if cm.linguist:
        analysis = cm.linguist.analyze_lyrics(lyrics)
        cm.current_analysis = analysis
        print("Analysis complete. Found verbs:", list(analysis.get("verb_sentence_map", {}).keys()))
    else:
        print("Error: Liquist not loaded.")
        return
    
    # Generate Day 3 (Action)
    print("\n--- Generating Day 3 (Action Verbs) ---")
    subject, body, text = cm.get_day_content(3, track_info, {})
    print(f"Subject: {subject}")
    print("Body Snippet (Action):")
    print(text[:500])
    
    # Save to file for review
    with open("reproduce_day_3_output.html", "w") as f:
        f.write(body)


if __name__ == "__main__":
    reproduce_day_3()
