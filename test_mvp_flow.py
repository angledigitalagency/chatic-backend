import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from agents.storage import Storage
from agents.scheduler import main as run_scheduler

def test_mvp_flow():
    print("=== STARTING MVP VERIFICATION ===")
    
    # 1. Simulate Stripe Webhook (Adding User)
    storage = Storage()
    test_email = "mvp_test_user@example.com"
    test_name = "MVP Test User"
    
    print(f"\nStep 1: Simulating New Payment/User for {test_email}...")
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Clean up first if exists
    try:
        sheet = storage.get_or_create_sheet()
        ws = sheet.worksheet("Users")
        cell = ws.find(test_email)
        if cell:
            ws.delete_rows(cell.row)
            print("  - Removed existing test user.")
    except:
        pass
        
    # Add User
    success = storage.add_user(
        email=test_email,
        phone="+1234567890",
        name=test_name,
        preferences="email",
        start_date=today,
        stripe_id="cus_test123"
    )
    
    if success:
        print("  ✅ User added successfully with Start_Date.")
    else:
        print("  ❌ Failed to add user.")
        return

    # 2. Verify Database
    print("\nStep 2: Verifying Database Entry...")
    users = storage.get_active_users()
    found = False
    for user in users:
        if user.get("Email") == test_email:
            found = True
            s_date = user.get("Start_Date")
            print(f"  - User found. Start_Date: {s_date}")
            if s_date == today:
                print("  ✅ Start_Date matches today.")
            else:
                print(f"  ❌ Start_Date mismatch (Expected {today}).")
            break
            
    if not found:
        print("  ❌ Test user not found in DB.")
        return

    # 3. Request Schedule Content (Mocking Deliverer would be ideal, but we'll run and check stdout)
    print("\nStep 3: Running Scheduler (Day 1 for new user)...")
    
    # We expect "Day 1: Join the Group Session" logic
    run_scheduler()
    
    print("\n=== MVP VERIFICATION COMPLETE ===")
    print("Check the output above 👆. You should see 'Processing MVP Test User -> Cycle Day 1' and 'Email sent to mvp_test_user@example.com'.")

if __name__ == "__main__":
    test_mvp_flow()
