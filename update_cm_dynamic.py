
import sys
import os

# Add parent directory to path to import agents
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.linguist import Linguist

def test_dynamic_extraction():
    print("--- Dynamic Content Extraction Test ---")
    
    # 1. Initialize Linguist
    linguist = Linguist()
    
    # 2. Sample Lyrics (La Camisa Negra)
    lyrics = """
Tengo la camisa negra
Hoy mi amor está de luto
Hoy tengo en el alma una pena
Y es por culpa de tu embrujo
Hoy sé que tú ya no me quieres
Y eso es lo que más me hiere
Que tengo la camisa negra
Y una pena que me duele
"""
    print(f"\nAnalyzing Lyrics ({len(lyrics)} chars)...")
    
    # 3. Analyze
    analysis = linguist.analyze_lyrics(lyrics)
    
    if not analysis:
        print("Analysis failed.")
        return

    # 4. Extract Article Game Data
    print("\n--- Article Game Data (Nouns + Gender) ---")
    game_data = analysis.get("reference_sheet", {}).get("article_game_data", {})
    if game_data:
        for noun, article in game_data.items():
            print(f"{article} {noun}")
    else:
        print("No game data found.")

    # 5. Extract Day 2 Questions
    print("\n--- Day 2 Melody Questions ---")
    verb_map = analysis.get("verb_sentence_map", {})
    
    # Check specifically for Tener and Estar
    target_melodies = ["tener", "estar"]
    
    for verb in target_melodies:
        if verb in verb_map:
            print(f"\nVerb: {verb.upper()}")
            entries = verb_map[verb]
            for entry in entries:
                print(f"  Sentence: {entry['sentence']}")
                print(f"  Q (ES): {entry.get('question_es')}")
                # print(f"  Q (EN): {entry.get('question_en')}") # Currently None
        else:
            print(f"\nVerb: {verb.upper()} - Not found in lyrics (or not identified)")

if __name__ == "__main__":
    test_dynamic_extraction()
