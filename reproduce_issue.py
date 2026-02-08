from agents.link_handler import LinkHandler

def main():
    handler = LinkHandler()
    link = "https://open.spotify.com/track/18pWcEUcUJpBFs7eNBsBht?si=622852e2c82748b8"
    
    print(f"Testing Link: {link}")
    track_id = handler.extract_track_id(link)
    print(f"Extracted ID: '{track_id}'")
    
    if track_id == "18pWcEUcUJpBFs7eNBsBht":
        print("SUCCESS: ID matches expected.")
    else:
        print("FAILURE: ID mismatch or None.")

if __name__ == "__main__":
    main()
