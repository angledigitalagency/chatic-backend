import requests
from bs4 import BeautifulSoup

def scrape_spotify(url):
    print(f"Scraping: {url}")
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to load page: {response.status_code}")
            return

        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Spotify titles are usually: "Song Name - song and lyrics by Artist | Spotify"
        # or og:title / og:description
        og_title = soup.find("meta", property="og:title")
        og_desc = soup.find("meta", property="og:description")
        
        title = og_title["content"] if og_title else "Unknown Title"
        artist_desc = og_desc["content"] if og_desc else "Unknown Artist"
        
        print(f"OG Title: {title}")
        print(f"OG Desc: {artist_desc}") # Often contains "Stream X by Artist..." or similar
        
        # Parse them out (Heuristic)
        # Often title is just the Song Name
        # Description might be "Listen to Song Name on Spotify. Artist · Song · 2024"
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scrape_spotify("https://open.spotify.com/track/4uLU6hMCjMI75M1A2tKUQC")
