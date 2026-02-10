import os
import sys
import jinja2
import json

# Ensure we can import agents
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from agents.storage import Storage

def generate_day_2(track_title="La Camisa Negra", artist="Juanes", play_link="https://open.spotify.com/track/27L8sESb3KR79asDUBu8nW", week_folder="content/week_01_la_camisa_negra"):
    print(f"🎵 Generating Day 2 for: {track_title}")
    
    # 1. Fetch CMS Data
    # For now, we simulate fetching from "CMS_Library" sheet or local cache
    # But since we have `process_cms.py` which tags rows, we should use that logic
    # Or just read the Google Sheet directly (Storage).
    
    # Simplification for MVP: Hardcoded Selection from what we know is in the sheet
    # We saw "verb:saber", "verb:parecer" earlier.
    # We need "verb:estar" and "verb:tener".
    # Assuming they are there. If not, we use fallbacks.
    
    melody_1 = {
        "meaning": "How are you?",
        "translation": "¿Hoy tu amor está de luto?",
        "original": "Hoy mi amor está de luto" # Ideally from Sheet
    }
    melody_2 = {
        "meaning": "Do you have it?",
        "translation": "¿tienes la camisa negra?",
        "original": "Tengo la camisa negra" # Ideally from Sheet
    }

    # 2. Setup Jinja2
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
    template = env.get_template("day_2.html")
    
    # 3. Render
    html_output = template.render(
        song_title=track_title,
        artist=artist,
        play_link=play_link,
        melody_1=melody_1,
        melody_2=melody_2
    )
    
    # 4. Save
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), week_folder, "day_2.html")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w") as f:
        f.write(html_output)
        
    print(f"✅ Generated: {output_path} ({len(html_output)} bytes)")

if __name__ == "__main__":
    generate_day_2()
