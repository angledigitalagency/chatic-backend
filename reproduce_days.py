
from agents.content_manager import ContentManager
from agents.Linguist import Linguist
import json

def reproduce_all():
    # 1. Setup Mock Data
    track_info = {
        'Title': 'La Camisa Negra',
        'Artist': 'Juanes',
        'Link': 'https://open.spotify.com/track/254bROmuoz5aJlSc2pz5Yp',
        'Image_URL': 'https://i.scdn.co/image/ab67616d0000b273e934ec7104f767852c03362a'
    }
    
    # Needs actual lyrics to find the verbs
    lyrics = """
    Tengo la camisa negra
    Hoy mi amor está de luto
    Hoy tengo en el alma una pena
    Y es por culpa de tu embrujo
    
    Hoy sé que tú ya no me quieres
    Y eso es lo que más me hiere
    Que tengo la camisa negra
    Y una pena que me duele
    
    Mal parece que solo me quedé
    Y fue pura todavía
    Tu mentira que maldita mala suerte la mía
    Que aquel día te encontré
    
    Por beber del veneno malevo de tu amor
    Yo quedé moribundo y lleno de dolor
    Respiré de ese humo amargo de tu adiós
    Y desde que tú te fuiste yo solo tengo
    
    Tengo la camisa negra
    Porque negra tengo el alma
    Yo por ti perdí la calma
    Y casi pierdo hasta mi cama
    
    Cama, cama, come on baby
    Te digo con disimulo
    Que tengo la camisa negra
    Y debajo tengo el difunto
    
    (Pa' enterrártelo cuando tú quieras, mamita)
    (Asi como lo oyes, mami)
    
    Tengo la camisa negra
    Ya tu amor no me interesa
    Lo que ayer me supo a gloria
    Hoy me sabe a pura...
    Miércoles por la tarde y tú que no llegas
    Ni siquiera muestras señas
    Y yo con la camisa negra
    Y tus maletas en la puerta
    
    Mal parece que solo me quedé
    Y fue pura todavía
    Tu mentira que maldita mala suerte la mía
    Que aquel día te encontré
    
    Por beber del veneno malevo de tu amor
    Yo quedé moribundo y lleno de dolor
    Respiré de ese humo amargo de tu adiós
    Y desde que tú te fuiste yo solo tengo
    
    Tengo la camisa negra
    Porque negra tengo el alma
    Yo por ti perdí la calma
    Y casi pierdo hasta mi cama
    
    Cama, cama, come on baby
    Te digo con disimulo
    Que tengo la camisa negra
    Y debajo tengo el difunto
    
    (Pa' enterrártelo cuando tú quieras, mamita)
    (Asi como lo oyes, mami)
    
    Tengo la camisa negra
    (Quedó claro, ¿no?)
    (Y te lo repito)
    (Pa' que te lo aprendas)
    (Juanes)
    """

    song_data = {
        'Full_Lyrics': lyrics,
        'Spanish_Lyrics': lyrics, # Fallback
        'Word_Analysis': json.dumps({
            "Nouns": ["Camisa", "Amor", "Alma", "Pena"],
            "Verbs": ["Tener", "Estar", "Querer", "Saber"],
            "Adjectives": ["Negra", "Malevo", "Amargo"]
        })
    }

    print("Initializing ContentManager...")
    cm = ContentManager()
    
    # Pre-analyze (Simulate Linguist pipeline)
    print("Running Linguistic Analysis...")
    cm.current_analysis = cm.linguist.analyze_lyrics(lyrics)
    
    # ---------------------------------------------------------
    # Generate DAY 2
    # ---------------------------------------------------------
    print("\n--- Generating Day 2 (Fluency Verbs) ---")
    subject2, body2, text2 = cm.get_day_content(2, track_info, song_data)
    
    with open("reproduce_day_2.html", "w") as f:
        f.write(body2)
    print("Saved reproduce_day_2.html")

    # ---------------------------------------------------------
    # Generate DAY 3
    # ---------------------------------------------------------
    print("\n--- Generating Day 3 (Action Verbs) ---")
    # Simulate execution context for Day 3 (sometimes expected separate analysis?)
    # get_day_content(3) handles re-analysis if needed, but we set current_analysis already.
    subject3, body3, text3 = cm.get_day_content(3, track_info, song_data)
    
    with open("reproduce_day_3_output.html", "w") as f:
        f.write(body3)
    print("Saved reproduce_day_3_output.html")


if __name__ == "__main__":
    reproduce_all()
