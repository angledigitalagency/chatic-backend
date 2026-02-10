import os
import argparse
from agents.content_manager import ContentManager
from agents.storage import Storage

def generate_preview(day, song_title="La Camisa Negra", song_artist="Juanes"):
    print(f"=== Generating Preview for Day {day} ({song_title}) ===")
    
    # 1. Mock Data (similar to test_daily_email.py)
    track_info = {
        'Title': song_title,
        'Artist': song_artist,
        'Link': 'https://open.spotify.com/track/27L8sESb3KR79asDUBu8nW',
        'Image_URL': 'https://i.scdn.co/image/ab67616d0000b273e04e76811442c5521404116c' # Real Album Art
    }
    
    # 1. Real Data from Storage
    storage = Storage(product="fluency")
    try:
        # We need to find the song in the DB first to get its full data
        # Storage doesn't have a simple "get_song" by title exposed publicly in the snippet I saw,
        # but it likely has internal methods or we can filter.
        # Let's peek at Storage.get_queue_links or similar.
        # Actually, let's just inspect the sheet directly if needed, but better to add a get_song_data method if missing.
        # For now, let's assume we can fetch it or mock it closer to reality if fetch fails.
        
        # Actually, let's use the reprocess_song.py logic to get fresh analysis if not in DB
        # But to be fast, let's look for a `get_song_data` in Storage.
        # If not present, I'll add it to Storage.py first.
        
        # Placeholder for now until I confirm Storage has get_song_data
        song_data = {} 
        
        # Let's try to fetch from sheet if possible
        sheet = storage.get_or_create_sheet()
        if sheet:
            worksheet = sheet.worksheet("Songs_DB")
            all_records = worksheet.get_all_records()
            # Find La Camisa Negra
            for record in all_records:
                if record.get("Title") == song_title:
                    song_data = record
                    break
        
        if not song_data:
             print(f"Warning: Song '{song_title}' not found in Songs_DB. Using empty data.")
             
    except Exception as e:
        print(f"Error fetching data: {e}. Using mock data.")
        # Mock Data for La Camisa Negra
        song_data = {
            "Title": "La Camisa Negra",
            "Artist": "Juanes",
            "Spanish_Lyrics": """
Tengo la camisa negra
Hoy mi amor está de luto
Hoy tengo en el alma una pena
Y es por culpa de tu embrujo
Hoy sé que tú ya no me quieres
Y eso es lo que más me hiere
Que tengo la camisa negra
Y una pena que me duele
Mal parece que solo me quedé
Y todo fue por tu culpa
Maldita mala suerte la mía
Que aquel día te encontré
Por beber del veneno malevo de tu amor
Yo quedé moribundo y lleno de dolor
Respiré de ese humo amargo de tu adiós
Y desde que tú te fuiste yo solo tengo
Tengo la camisa negra
Porque negra tengo el alma
Yo por ti perdí la calma
Y casi pierdo hasta mi cama
Cama cama caman baby
Te digo con disimulo
Que tengo la camisa negra
Y debajo tengo el difunto
Tengo la camisa negra
Ya tu amor no me interesa
Lo que ayer me supo a gloria
Hoy me sabe a pura
Miércoles por la tarde y tú que no llegas
Ni siquiera muestras señas
Y yo con la camisa negra
Y tus maletas en la puerta
 Mal parece que solo me quedé
Y todo fue por tu culpa
Maldita mala suerte la mía
Que aquel día te encontré
Por beber del veneno malevo de tu amor
Yo quedé moribundo y lleno de dolor
Respiré de ese humo amargo de tu adiós
Y desde que tú te fuiste yo solo tengo
Tengo la camisa negra
Porque negra tengo el alma
Yo por ti perdí la calma
Y casi pierdo hasta mi cama
Cama cama caman baby
Te digo con disimulo
Que tengo la camisa negra
Y debajo tengo el difunto
""",
        "English_Lyrics": "I have the black shirt..."
    } 
    
    
    # Validation / Fallback to Mock if DB data is missing or incomplete
    if not song_data or not song_data.get("Spanish_Lyrics"):
        print("Dataset incomplete or missing. Using Mock Data for La Camisa Negra.")
        song_data = {
            "Title": "La Camisa Negra",
            "Artist": "Juanes",
            "Spanish_Lyrics": """
Tengo la camisa negra
Hoy mi amor está de luto
Hoy tengo en el alma una pena
Y es por culpa de tu embrujo
Hoy sé que tú ya no me quieres
Y eso es lo que más me hiere
Que tengo la camisa negra
Y una pena que me duele
Mal parece que solo me quedé
Y todo fue por tu culpa
Maldita mala suerte la mía
Que aquel día te encontré
Por beber del veneno malevo de tu amor
Yo quedé moribundo y lleno de dolor
Respiré de ese humo amargo de tu adiós
Y desde que tú te fuiste yo solo tengo
Tengo la camisa negra
Porque negra tengo el alma
Yo por ti perdí la calma
Y casi pierdo hasta mi cama
Cama cama caman baby
Te digo con disimulo
Que tengo la camisa negra
Y debajo tengo el difunto
Tengo la camisa negra
Ya tu amor no me interesa
Lo que ayer me supo a gloria
Hoy me sabe a pura
Miércoles por la tarde y tú que no llegas
Ni siquiera muestras señas
Y yo con la camisa negra
Y tus maletas en la puerta
 Mal parece que solo me quedé
Y todo fue por tu culpa
Maldita mala suerte la mía
Que aquel día te encontré
Por beber del veneno malevo de tu amor
Yo quedé moribundo y lleno de dolor
Respiré de ese humo amargo de tu adiós
Y desde que tú te fuiste yo solo tengo
Tengo la camisa negra
Porque negra tengo el alma
Yo por ti perdí la calma
Y casi pierdo hasta mi cama
Cama cama caman baby
Te digo con disimulo
Que tengo la camisa negra
Y debajo tengo el difunto
""",
        "English_Lyrics": "I have the black shirt..."
    }

    # 2. Render Content
    content_manager = ContentManager()
    subject, body_html, body_text = content_manager.get_day_content(day, track_info, song_data)
    
    if not body_html:
        print("Error: No content generated.")
        return

    # 3. Save to HTML File
    filename = f"preview_day_{day}.html"
    filepath = os.path.abspath(filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(body_html)
        
    print(f"\n✅ Preview generated: {filepath}")
    print("Open this file in your browser to inspect the layout.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate HTML preview for a daily email.")
    parser.add_argument("--day", type=int, default=1, help="Day index (1-7)")
    args = parser.parse_args()
    
    generate_preview(args.day)
