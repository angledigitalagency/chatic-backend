import spacy
from spellchecker import SpellChecker

def debug_failures():
    nlp = spacy.load("es_core_news_sm")
    spell = SpellChecker(language='es')
    
    # Words flagged by user + suspicious ones
    problem_words = ["home", "on", "baby", "respiré", "adiós", "girls", "english", "weekenes"]
    
    print("--- Debugging Word Analysis ---")
    for word in problem_words:
        doc = nlp(word)
        token = doc[0]
        
        in_dict_exact = word in spell
        in_dict_lemma = token.lemma_ in spell
        
        print(f"Word: '{word}'")
        print(f"  Example Context: {token.pos_} (Lemma: {token.lemma_})")
        print(f"  In Spanish Dict? (Exact): {in_dict_exact}")
        print(f"  In Spanish Dict? (Lemma): {in_dict_lemma}")
        if token.pos_ == "PROPN":
            print("  Result: ACCEPTED (By PROPN Bypass)")
        elif not in_dict_exact and not in_dict_lemma:
             print("  Result: REJECTED (Correctly)")
        else:
             print("  Result: ACCEPTED (In Dict)")
        print("-" * 20)

if __name__ == "__main__":
    debug_failures()
