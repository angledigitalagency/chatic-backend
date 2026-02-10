import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius

class DataFetcher:
    def __init__(self):
        # Initialize Genius
        genius_token = os.getenv("GENIUS_ACCESS_TOKEN")
        if not genius_token:
            print("Warning: GENIUS_ACCESS_TOKEN not found in environment.")
            self.genius = None
        else:
            self.genius = lyricsgenius.Genius(genius_token)
            self.genius.verbose = False # Turn off status messages
            self.genius.remove_section_headers = True # Remove [Chorus], [Verse], etc.

    def get_track_info(self, track_url):
        """
        Fetches track metadata (Artist, Title) by scraping Spotify public page.
        Bypasses API restrictions.
        """
        print(f"Scraping Spotify metadata for: {track_url}")
        try:
            response = requests.get(track_url)
            if response.status_code != 200:
                print(f"Failed to load page: {response.status_code}")
                return None

            soup = BeautifulSoup(response.content, 'html.parser')
            
            # OpenAI Graph Tags are usually reliable
            og_title_tag = soup.find("meta", property="og:title")
            og_desc_tag = soup.find("meta", property="og:description")
            og_image_tag = soup.find("meta", property="og:image")
            
            if not og_title_tag:
                print("Could not find Title in OG tags.")
                return None

            # Title often: "Song Name"
            title = og_title_tag["content"]
            
            # Desc often: "Artist · Song · Year" or "Listen to X by Artist..."
            # Let's try to extract artist from description if possible, or just use description as a fallback
            # Heuristic: Spotify web descriptions are usually "Artist · Album · Song · Year"
            artist = "Unknown Artist"
            if og_desc_tag:
                desc_content = og_desc_tag["content"]
                parts = desc_content.split('·')
                if len(parts) > 0:
                    artist = parts[0].strip()
            
            # Extract Image URL
            image_url = og_image_tag["content"] if og_image_tag else None
            
            return {
                "artist": artist,
                "title": title,
                "external_url": track_url,
                "image_url": image_url
            }

        except Exception as e:
            print(f"Error scraping Spotify: {e}")
            return None

    def fetch_lyrics(self, track_name, artist_name):
        """
        Fetches lyrics from Genius for the given track and artist.
        """
        if not self.genius:
            return None

        try:
            # 1. Try exact search
            song = self.genius.search_song(title=track_name, artist=artist_name)
            
            # Helper to validate result
            def is_valid(song, target_artist):
                if not song: return False
                
                # Title Checks
                title_lower = song.title.lower()
                bad_keywords = ["parody", "parodia", "paródia", "remix"] # Maybe exclude remix too if user wants original? Or keep remix? User sent a link that might be a remix.
                # Actually, Despacito - Remix is valid. Parody is not.
                if any(x in title_lower for x in ["parody", "parodia", "paródia"]):
                    print(f"Skipping Parody result: {song.title}")
                    return False
                
                # Artist Check
                # Genius Artist might be "Luis Fonsi" while we asked for "Luis Fonsi, Daddy Yankee"
                # We want to ensure at least partial match
                genius_artist = song.artist.lower()
                target_lower = target_artist.lower()
                
                # Heuristic: If one of them is contained in the other, it's likely fine.
                # e.g. "Luis Fonsi" in "Luis Fonsi & Daddy Yankee"
                if target_lower in genius_artist or genius_artist in target_lower:
                    return True
                
                # Check for Primary Artist match if failed
                primary = target_lower.split(",")[0].strip()
                if primary in genius_artist:
                    return True

                print(f"Skipping Artist Mismatch: Found '{song.artist}', wanted '{target_artist}'")
                return False

            # 1. Try exact search
            song = self.genius.search_song(title=track_name, artist=artist_name)
            if is_valid(song, artist_name):
                return song.lyrics
            
            # 2. Retry with Primary Artist (if multiple)
            if "," in artist_name:
                primary_artist = artist_name.split(",")[0].strip()
                print(f"Retrying with Primary Artist: {primary_artist}")
                song = self.genius.search_song(title=track_name, artist=primary_artist)
                if is_valid(song, primary_artist):
                    return song.lyrics
            
            print(f"Lyrics not found in Genius for {track_name} by {artist_name}")
            return None
        except Exception as e:
            print(f"Error fetching lyrics from Genius: {e}")
            return None
