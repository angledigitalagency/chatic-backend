import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
load_dotenv()

from agents.storage import Storage
from agents.deliverer import Deliverer
from agents.activity_manager import ActivityManager

def main():
    print("\n=== Chatic: Daily Interactions ===\n")
    
    storage = Storage()
    deliverer = Deliverer()
    activity_mgr = ActivityManager()
    
    # 1. Get Active Users
    users = storage.get_active_users()
    if not users:
        print("No active users found in 'Users' tab.")
        return
        
    print(f"Found {len(users)} active users.")
    
    # 2. Generate Content (For now, generate same content for everyone, or randomize per user)
    # Let's simple toggle: 50% quiz, 50% reminder, or based on user pref (not fully implemented yet)
    
    for user in users:
        name = user.get("Name", "Friend")
        email = user.get("Email")
        phone = str(user.get("Phone", ""))
        pref = user.get("Preferences", "both").lower()
        
        print(f"\nProcessing user: {name} ({email})")
        
        # Determine Activity Type (Random for now)
        import random
        is_quiz = random.choice([True, False])
        
        body_text = ""
        subject = ""
        
        if is_quiz:
            q_text, answer = activity_mgr.generate_verb_quiz()
            subject = "Chatic Daily Quiz!"
            body_text = q_text
            print(f"Generated Quiz: {answer}")
        else:
            msg, song = activity_mgr.generate_song_reminder()
            subject = "Chatic Song Reminder"
            body_text = msg
            print("Generated Reminder.")
            
        # Send based on Preference
        
        # EMAIL
        if "email" in pref or "both" in pref:
            if email:
                # Wrap text in simple HTML
                body_html = f"<html><body><pre style='font-family: sans-serif; font-size: 14px;'>{body_text}</pre></body></html>"
                deliverer.send_email(email, subject, body_html, body_text)
                print(f"Email sent to {email}")
        
        # SMS
        if "sms" in pref or "both" in pref or "phone" in pref:
            if phone:
                # Format phone number if needed (basic check)
                if not phone.startswith("+"):
                    # Assume US/local default? For now, user must provide E.164
                    pass 
                
                success = deliverer.send_sms(phone, body_text)
                if success:
                    print(f"SMS sent to {phone}")
                else:
                    print(f"Failed to send SMS to {phone}")

if __name__ == "__main__":
    main()
