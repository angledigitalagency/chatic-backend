import os
import sys
from dotenv import load_dotenv
from agents.deliverer import Deliverer

# Load env vars
load_dotenv()

def main():
    print("--- Test Email Deliverer ---")
    
    # Check for email in args or prompt
    if len(sys.argv) > 1:
        recipient = sys.argv[1]
    else:
        recipient = input("Enter recipient email address: ").strip()

    if not recipient:
        print("No recipient provided. Exiting.")
        return

    # Dummy Data
    track_info = {
        "title": "Never Gonna Give You Up",
        "artist": "Rick Astley",
        "external_url": "https://open.spotify.com/track/4uLU6hMCjMI75M1A2tKUQC"
    }
    
    lyrics = """
    We're no strangers to love
    You know the rules and so do I
    A full commitment's what I'm thinking of
    You wouldn't get this from any other guy
    
    I just wanna tell you how I'm feeling
    Gotta make you understand
    
    Never gonna give you up
    Never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry
    Never gonna say goodbye
    Never gonna tell a lie and hurt you
    """

    print(f"Sending test email to: {recipient}...")
    
    deliverer = Deliverer()
    success = deliverer.send_welcome_email(recipient, track_info, lyrics)
    
    if success:
        print("Test passed! Email sent.")
    else:
        print("Test failed. Check your configuration.")

if __name__ == "__main__":
    main()
