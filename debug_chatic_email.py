import os
import sys
from dotenv import load_dotenv

# Ensure we can import agents
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
load_dotenv()

from agents.deliverer import Deliverer

def test_chatic_welcome():
    recipient = "dominicalmassages@gmail.com"
    print(f"Testing Chatic Welcome Email to {recipient}...")
    
    # Initialize standard Deliverer (defaults to 'chatic')
    deliverer = Deliverer(identity="chatic")
    
    # Verify Credentials Loaded
    print(f"Using Username: {deliverer.username}")
    print(f"Using Password Length: {len(deliverer.password) if deliverer.password else 0}")
    
    # Send
    try:
        success = deliverer.send_welcome_email(recipient, name="Test User")
        if success:
            print("✅ Email Sent Successfully!")
        else:
            print("❌ Email Failed to Send.")
    except Exception as e:
        print(f"❌ Exception during send: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_chatic_welcome()
