import os
from agents.content_manager import ContentManager

print("--- Simulating Day 7 Content Generation (Session Invite) ---")

# Mock dependencies
class MockLinguist:
    def get_analysis(self, lyrics):
        return {}

class MockSpotify:
    def get_track_info(self, song_name):
        return {
            'title': 'La Camisa Negra',
            'artist': 'Juanes',
            'cover_url': 'https://i.scdn.co/image/ab67616d0000b273a040b257545938f32269a838', 
            'spotify_url': 'https://open.spotify.com/track/2NG8e71887e55353549641'
        }

try:
    content_manager = ContentManager()
    # Inject mocks
    content_manager.linguist = MockLinguist()
    content_manager.spotify = MockSpotify()

    print("\n--- Generating Day 7 (Session Invite) ---")
    
    # We can pass mock track info directly if _day_7_session_invite accepts it
    track_info = {
        'title': 'La Camisa Negra',
        'artist': 'Juanes'
    }

    # Call the specific method (or get_day_content with day_index=7)
    # Using get_day_content to test the full flow
    subject, body_html, body_text = content_manager.get_day_content(
        day_index=7,
        track_info=track_info,
        song_data={}
    )
    
    print(f"Subject: {subject}")
    print(f"Body Snippet:\n{body_text}")
    
    if body_html:
        with open("reproduce_day_7.html", "w") as f:
            f.write(body_html)
        print("Saved to reproduce_day_7.html")
    else:
        print("Error: No HTML body returned")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
