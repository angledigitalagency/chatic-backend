from agents.storage import Storage
import datetime

def main():
    print("--- Test Storage Agent (Google Sheets) ---")
    
    print("1. Initializing Storage (User Login may be required)...")
    storage = Storage()
    
    # Dummy Data
    track_info = {
        "title": "Never Gonna Give You Up",
        "artist": "Rick Astley",
        "external_url": "https://open.spotify.com/track/4uLU6hMCjMI75M1A2tKUQC"
    }
    
    sentences = [
        "We're no strangers to love",
        "You know the rules and so do I",
        "A full commitment's what I'm thinking of"
    ]
    
    analysis = {
        "Nouns": ["love", "rules", "commitment"],
        "Verbs": ["know", "thinking"]
    }
    
    print("2. Logging Song to 'Songs_DB'...")
    try:
        storage.log_song(track_info, sentences, analysis)
        print("Success! Check your Google Sheet 'Chatic_Master_DB'.")
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    main()
