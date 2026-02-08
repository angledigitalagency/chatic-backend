from agents.linguist import Linguist

def main():
    print("--- Test Linguist Agent ---")
    
    # Sample Lyrics (Rick Astley - Never Gonna Give You Up)
    # Including some structure markers to test cleaning
    lyrics = """
    [Intro]
    (Ooh)
    
    [Verse 1]
    We're no strangers to love
    You know the rules and so do I
    A full commitment's what I'm thinking of
    You wouldn't get this from any other guy
    
    [Pre-Chorus]
    I just wanna tell you how I'm feeling
    Gotta make you understand
    
    [Chorus]
    Never gonna give you up
    Never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry
    Never gonna say goodbye
    Never gonna tell a lie and hurt you
    """

    linguist = Linguist()
    result = linguist.analyze_lyrics(lyrics)
    
    if not result:
        print("Analysis failed.")
        return

    print("\n--- Reference Sheet ---")
    for category, words in result['reference_sheet'].items():
        print(f"{category}: {', '.join(words)}")

    print("\n--- Top 3 Sentences ---")
    for i, sent in enumerate(result['top_sentences'], 1):
        print(f"{i}. {sent}")

if __name__ == "__main__":
    main()
