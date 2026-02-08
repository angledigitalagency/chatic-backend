import spacy
from spellchecker import SpellChecker
import json

def test_words():
    print("Loading resources...")
    nlp = spacy.load("es_core_news_sm")
    spell = SpellChecker(language='es')
    
    words = ["adiós", "respiré", "seña", "girls", "english"]
    
    print(f"\nDictionary Check (pyspellchecker):")
    for w in words:
        in_dict = w in spell
        print(f"  '{w}': {in_dict}")

    print(f"\nSpaCy POS Tagging:")
    doc = nlp(" ".join(words))
    for token in doc:
        print(f"  '{token.text}' -> Lemma: '{token.lemma_}', POS: {token.pos_}")

    print(f"\nJSON Encoding Test:")
    data = {"test": ["adiós", "respiré"]}
    print("  Default (ascii):", json.dumps(data))
    print("  No-Ascii:", json.dumps(data, ensure_ascii=False))

if __name__ == "__main__":
    test_words()
