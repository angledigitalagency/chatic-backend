import os
import sys
from datetime import datetime
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
load_dotenv()

from storage import Storage
from deliverer import Deliverer
from activity_manager import ActivityManager

def main():
    print("\n=== Chatic: Daily Schedule Engine ===\n")
    
    storage = Storage()
    deliverer = Deliverer()
    activity_mgr = ActivityManager()
    
    # 1. Get Active Users
    users = storage.get_active_users()
    if not users:
        print("No active users found.")
        return
        
    print(f"Found {len(users)} active users.")
    current_date = datetime.now().date()
    
    # Global Cycle Calculation: Monday is 0, so Day 1. Sunday is 6, so Day 7.
    global_day = datetime.now().weekday() + 1
    print(f"🌍 Global Schedule: Today is Day {global_day} of the week.")

    for user in users:
        name = user.get("Name", "Friend")
        email = user.get("Email")
        phone = str(user.get("Phone", ""))
        pref = user.get("Preferences", "both").lower()
        
        print(f"\nProcessing {name} ({email}) -> Sending Global Day {global_day}")
        
        # 2. Get Content (Always Global Day)
        subject, body_html, body_text = activity_mgr.get_content_for_day(global_day, name)
        
        # 3. Deliver
        
        # EMAIL
        if "email" in pref or "both" in pref:
            if email:
                deliverer.send_email(email, subject, body_html, body_text)
        
        # SMS (Short Text only)
        if "sms" in pref or "both" in pref or "phone" in pref:
            if phone:
                # Send just the body_text (or a summary if too long)
                # Twilio has char limits, but for now sending full text
                deliverer.send_sms(phone, body_text)

if __name__ == "__main__":
    main()
