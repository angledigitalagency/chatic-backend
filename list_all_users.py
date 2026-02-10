import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from agents.storage import Storage

def list_users():
    load_dotenv()
    print("📋 Fetching Users from Fluency DB...")
    
    try:
        storage = Storage(product="fluency")
        users = storage.get_active_users()
        
        print(f"\nFound {len(users)} Users:\n====================")
        for i, u in enumerate(users, 1):
            email = u.get("Email", "No Email")
            name = u.get("Name", "Unknown")
            source = u.get("Source", "N/A")
            start = u.get("Start Date", "No Start Date")
            print(f"{i}. {email} | {name} | {source} | Started: {start}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    list_users()
