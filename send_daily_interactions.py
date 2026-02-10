import os
import sys
import argparse
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
load_dotenv()

from agents.storage import Storage
from agents.deliverer import Deliverer
from agents.content_manager import ContentManager

def main(dry_run=False):
    print("\n=== Fluency Radio: Daily Interactions ===\n")
    if dry_run:
        print("🔍 DRY RUN MODE: No emails will be sent.\n")
    
    # Initialize Agents
    storage = Storage(product="fluency") # Ensure we focus on Fluency DB if split, though user list might be in chatic
    # If users are in shared sheet, Storage handles it. active_users fetches from 'Users' tab.
    
    # We need a fallback to 'ifeelsochatty' for Chatic users if we want to run both?
    # For now, let's focus on logic that works for the "Fluency" source users.
    
    # Check for correct Deliverer identity
    deliverer = Deliverer(identity="fluency")
    content_mgr = ContentManager()
    
    # 1. Get Active Users
    users = storage.get_active_users()
    if not users:
        print("No active users found.")
        return
        
    print(f"Found {len(users)} active users.")
    
    # 2. Process Each User
    for user in users:
        email = user.get("Email")
        name = user.get("Name", "Student")
        
        # Calculate Progress
        total_days = storage.get_user_progress(user)
        
        if total_days == 0:
            print(f"⏩ {email}: Day 0 (Welcome already sent). Skipping.")
            continue
            
        # Determine Current Week & Day
        # Week 1 starts at Day 1. Week 2 at Day 8.
        # Week Index (1-based) = ((total_days - 1) // 7) + 1
        week_num = ((total_days - 1) // 7) + 1
        day_num = ((total_days - 1) % 7) + 1
        
        print(f"👤 {email} (Day {total_days} -> Week {week_num}, Day {day_num})")
        

def send_content_for_day(email, week_num, day_num, dry_run=False):
    """
    Sends the pre-generated content for a specific Week & Day to the user.
    Returns True if successful (or skipped responsibly), False if failed.
    """
    deliverer = Deliverer(identity="fluency")
    
    # Locate Content
    base_dir = os.path.dirname(os.path.abspath(__file__))
    content_dir = os.path.join(base_dir, "content")
    
    # DEBUG LOGGING (To be removed later, but critical now)
    print(f"   [DEBUG] Executing from: {base_dir}")
    print(f"   [DEBUG] Looking for content in: {content_dir}")
    if deliverer.username:
         print(f"   [DEBUG] Email Configured: {deliverer.display_name} ({deliverer.username})")
    else:
         print(f"   [ERROR] Email Configured: FALSE (Missing Env Vars?)")

    week_folder = None
    
    if os.path.exists(content_dir):
        for entry in os.listdir(content_dir):
            if entry.startswith(f"week_{week_num:02d}_"):
                week_folder = os.path.join(content_dir, entry)
                print(f"   [DEBUG] Found Week Folder: {entry}")
                break

    
    if not week_folder:
        print(f"   ⚠️ No content found for Week {week_num}. Checking Week 1 fallback...")
        for entry in os.listdir(content_dir):
            if entry.startswith("week_01_"):
                week_folder = os.path.join(content_dir, entry)
                print(f"   🔄 Falling back to Week 1 content: {entry}")
                break
        
        if not week_folder:
             print("   ❌ Critical: No content folders found at all.")
             return False

    # Read Day Content
    day_file = os.path.join(week_folder, f"day_{day_num}.html")
    metadata_file = os.path.join(week_folder, "metadata.json")
    
    if not os.path.exists(day_file):
         print(f"   ⚠️ File not found: {day_file}")
         return False
         
    # Read HTML
    with open(day_file, "r") as f:
        body_html = f.read()
    
    # Read Metadata for Title
    song_title = "Song"
    if os.path.exists(metadata_file):
        import json
        with open(metadata_file, "r") as f:
            meta = json.load(f)
            song_title = meta.get('track_info', {}).get('title', 'Song')
    
    # Reconstruct Subject
    subjects = {
        1: f"🎵 Day 1: Song of the Week - {song_title}",
        2: f"🎵 Day 2: Fluency Verbs ({song_title})",
        3: f"Day 3: Action & Melody in {song_title}",
        4: f"Day 4: Connecting the Dots in {song_title}",
        5: f"🗣️ Day 5: Speech Engineering ({song_title})",
        6: f"💀 Day 6: Review ({song_title})",
        7: f"🎟️ Day 7: Your VIP Pass"
    }
    subject = subjects.get(day_num, f"Day {day_num} Content")
    
    # Body Text (Plain)
    body_text = f"Day {day_num} Content for {song_title}. Please enable HTML to view."

    # Send
    print(f"   📧 Sending to {email}: {subject}")
    
    if not dry_run:
        success = deliverer.send_email(email, subject, body_html, body_text)
        return success
    else:
        print("   (Dry Run: Email suppressed)")
        return True

        
        # Determine Current Week & Day
        week_num = ((total_days - 1) // 7) + 1
        day_num = ((total_days - 1) % 7) + 1
        
        print(f"👤 {email} (Day {total_days} -> Week {week_num}, Day {day_num})")
        
        send_content_for_day(email, week_num, day_num, dry_run=dry_run)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Run without sending emails")
    args = parser.parse_args()
    
    main(dry_run=args.dry_run)
