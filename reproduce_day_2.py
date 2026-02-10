import os
from agents.content_manager import ContentManager

def reproduce_day_2():
    print("Generating Day 2 Preview...")
    
    # Mock Data matching La Camisa Negra
    track_info = {
        'Title': 'La Camisa Negra',
        'Artist': 'Juanes',
        'Link': 'https://open.spotify.com/track/27L8sESb3KR79asDUBu8nW',
        'Image_URL': 'https://i.scdn.co/image/ab67616d0000b273e04e76811442c5521404116c'
    }
    
    song_data = {
        "Title": "La Camisa Negra",
        "Spanish_Lyrics": """
Tengo la camisa negra
Hoy mi amor está de luto
Hoy tengo en el alma una pena
Y es por culpa de tu embrujo
Hoy sé que tú ya no me quieres
Y eso es lo que más me hiere
Que tengo la camisa negra
Y una pena que me duele
""",
        "Full_Lyrics": """
Tengo la camisa negra
Hoy mi amor está de luto
Hoy tengo en el alma una pena
Y es por culpa de tu embrujo
Hoy sé que tú ya no me quieres
Y eso es lo que más me hiere
Que tengo la camisa negra
Y una pena que me duele
"""
    }

    cm = ContentManager()
    subject, body_html, body_text = cm.get_day_content(2, track_info, song_data)
    
    filename = "reproduce_day_2.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(body_html)
        
    print(f"Generated {filename}")

if __name__ == "__main__":
    reproduce_day_2()
