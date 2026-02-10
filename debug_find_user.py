
from agents.storage import Storage

def check_users():
    print("--- Searching for Users ---")
    targets = ["feelsochatty@gmail.com", "yogasurftribe@gmail.com"]
    
    for product in ["fluency", "ifeelsochatty"]:
        print(f"\nChecking {product} DB...")
        try:
            s = Storage(product=product)
            users = s.get_active_users()
            found = False
            for u in users:
                if u.get('Email') in targets:
                    print(f"FOUND in {product}: {u}")
                    found = True
            if not found:
                print(f"No targets found in {product}")
        except Exception as e:
            print(f"Error checking {product}: {e}")

if __name__ == "__main__":
    check_users()
