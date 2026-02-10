import os
import time
from send_daily_interactions import send_content_for_day

email = "massageslafortuna@gmail.com"

print(f"\n🧪 MANUAL TEST for {email}\n")
print("We will skip the webhook and Stripe wait. Sending Day 1-7 NOW.")
print("-" * 50)

for day in range(1, 8):
    print(f"🚀 Attempting Day {day}...")
    success = send_content_for_day(email, 1, day, dry_run=False)
    if success:
        print(f"✅ Day {day} Sent Successfully!")
    else:
        print(f"❌ Day {day} Failed.")
    
    # Small pause to avoid spam blockers
    time.sleep(2)

print("\n🏁 Test Sequence Complete.\n")
