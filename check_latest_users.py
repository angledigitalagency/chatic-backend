
from agents.storage import Storage

def check_latest():
    print("\n--- Latest Fluency Users ---")
    try:
        s = Storage(product="fluency")
        users = s.get_active_users()
        for u in users[-10:]:
            print(f"Email: {u.get('Email')} | Source: {u.get('Source')}")
    except Exception as e:
        print(e)
            
    print("\n--- Latest Chatic Users ---")
    try:
        s = Storage(product="chatic")
        users = s.get_active_users()
        for u in users[-10:]:
             print(f"Email: {u.get('Email')} | Source: {u.get('Source')}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    check_latest()
