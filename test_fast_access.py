import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the handler from webhook_server
from webhook_server import handle_checkout_session
from agents.storage import Storage

def test_fast_access():
    print("=== STARTING FAST ACCESS VERIFICATION ===")
    
    test_email = "fast_access_user@example.com"
    test_name = "Fast Access Student"
    
    # 1. Clean up old test user
    storage = Storage()
    try:
        sheet = storage.get_or_create_sheet()
        ws = sheet.worksheet("Users")
        cell = ws.find(test_email)
        if cell:
            ws.delete_rows(cell.row)
            print("  - Removed existing test user.")
    except:
        pass
        
    print(f"\nStep 1: Simulating Webhook for {test_email}...")
    today_num = datetime.now().weekday() + 1
    print(f"  - Today is Weekday {today_num} (Friday is 5).")
    print(f"  - EXPECTATION: Should send emails for Days 1 through {today_num}.")

    # Mock Session Object
    mock_session = {
        'customer': 'cus_fast123',
        'customer_details': {
            'email': test_email,
            'name': test_name,
            'phone': '+1555000000'
        }
    }
    
    # CALL THE HANDLER
    handle_checkout_session(mock_session)
    
    print("\n=== VERIFICATION COMPLETE ===")
    print(f"Check the output above 👆. You should see 'Sending Day X content...' for Days 1 to {today_num}.")

if __name__ == "__main__":
    test_fast_access()
