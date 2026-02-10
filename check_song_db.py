from agents.storage import Storage

def check_la_camisa_negra():
    storage = Storage()
    print("Connecting to Storage...")
    try:
        songs = storage.get_all_songs()
        print(f"Total songs in DB: {len(songs)}")
        
        target = None
        for song in songs:
            if "camisa" in str(song.get("Title", "")).lower():
                target = song
                break
        
        if target:
            print(f"Found La Camisa Negra: {target.get('Title')}")
            print(f"Has Extracted Sentences? {'Yes' if target.get('Extracted_Sentences') else 'No'}")
            print(f"Extracted Sentences: {target.get('Extracted_Sentences')[:100]}...") # Preview
            print(f"Has Word Analysis? {'Yes' if target.get('Word_Analysis') else 'No'}")
        else:
            print("La Camisa Negra NOT found in Songs_DB.")
            
    except Exception as e:
        print(f"Error checking DB: {e}")

if __name__ == "__main__":
    check_la_camisa_negra()
