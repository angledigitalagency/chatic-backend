import random
from agents.storage import Storage

class SpanishPractice:
    def __init__(self):
        self.storage = Storage()
        self.verb_index = []
        self._load_data()

    def _load_data(self):
        print("Loading game data from 'Verb_Index'...")
        sheet = self.storage.get_or_create_sheet()
        if not sheet: 
            print("Error: Could not connect to Sheet.")
            return

        try:
            ws = sheet.worksheet("Verb_Index")
            rows = ws.get_all_records() # Expects headers: Verb, Sentence, Song_Title, Link
            self.verb_index = rows
            print(f"Loaded {len(rows)} challenges!")
        except Exception as e:
            print(f"Error loading Verb_Index: {e}")
            self.verb_index = []

    def play(self):
        if not self.verb_index:
            print("No data found! Process some Spanish songs first.")
            return

        print("\n--- ¡Bienvenido a Spanish Verb Master! ---")
        print("Type 'exit' to quit.\n")

        while True:
            challenge = random.choice(self.verb_index)
            verb = challenge.get('Verb', 'Unknown')
            sentence = challenge.get('Sentence', '')
            tense = challenge.get('Tense', '')
            difficulty = challenge.get('Difficulty', '')

            print(f"🎵 Song: {challenge.get('Song_Title', 'Unknown')}")
            print(f"📖 Sentence: {sentence}")
            print(f"⚡ Target Verb: {verb.upper()}  |  🕒 Tense: {tense}  |  📊 Level: {difficulty}")
            
            guess = input("\nType the conjugated form found in the sentence (or 's' to skip): ").strip().lower()
            
            if guess == 'exit':
                break
                
            # Naive verification: check if guess matches the verb lemma OR is in the sentence
            if guess in sentence.lower():
                print("✅ Correct! (It's in the sentence)")
            elif guess == 's':
                print("Skipped.")
            else:
                print("❌ Try again.")
                
            print("-" * 30)

if __name__ == "__main__":
    game = SpanishPractice()
    game.play()
