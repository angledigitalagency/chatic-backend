
import spacy
from agents.linguist import Linguist

def debug_context():
    l = Linguist()
    
    test_sentences = [
        "sin ti no puedo vivir",
        "quiero comer",
        "voy a ir a casa",
        "tengo que ser sincero"
    ]
    
    print("--- Debugging AuX Context ---")
    
    for text in test_sentences:
        print(f"\nAnalyzing: '{text}'")
        analysis = l.analyze_lyrics(text)
        
        # Check the map
        v_map = analysis.get('verb_sentence_map', {})
        
        for verb, entries in v_map.items():
            for entry in entries:
                print(f"  Verb: {verb} | Aux Context: {entry.get('aux_context')} | Head: {entry.get('conjugated')}")

        # Also direct spacy check to see what's happening
        doc = l.nlp(text)
        print(f"  Full Tree:")
        for token in doc:
             print(f"    {token.text} ({token.pos_}/{token.dep_}) <-- {token.head.text} ({token.head.pos_})")


if __name__ == "__main__":
    debug_context()
