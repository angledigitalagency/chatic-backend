import os
import sys
from dotenv import load_dotenv

# Ensure we can import agents/storage
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from agents.storage import Storage

def verify_user(email="agenciaesencial@gmail.com"):
    # Load Environment Variables for Google API Auth
    load_dotenv()
    
    print(f"🔍 Checking Database for: {email}")
    try:
        storage = Storage(product="fluency")
        users = storage.get_active_users()
        
        found = False
        for user in users:
            if user.get("Email") == email:
                print(f"✅ FOUND! User {email} is in the Database.")
                print(f"   Name: {user.get('Name')}")
                print(f"   Start Date: {user.get('Start Date')}")
                found = True
                break
        
        if not found:
            print(f"❌ User {email} NOT FOUND in Database.")
            print(f"   (There are {len(users)} users total)")
            
    except Exception as e:
        print(f"❌ Error checking database: {e}")

if __name__ == "__main__":
    verify_user()
