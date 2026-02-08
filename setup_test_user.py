import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
load_dotenv()

from agents.storage import Storage

def main():
    print("=== Chatic User Setup ===")
    
    email = input("Enter Email: ").strip()
    phone = input("Enter Phone (E.164 format, e.g. +14155552671): ").strip()
    name = input("Enter Name: ").strip()
    pref = input("Preferences (email/sms/both): ").strip().lower()
    
    if not pref: pref = "both"
    
    storage = Storage()
    success = storage.add_user(email, phone, name, pref)
    
    if success:
        print("\nUser added successfully!")
        print("Now you can run 'python3 send_daily_interactions.py' to test.")
    else:
        print("\nFailed to add user.")

if __name__ == "__main__":
    main()
