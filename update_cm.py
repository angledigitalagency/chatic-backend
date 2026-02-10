
import os

file_path = 'agents/content_manager.py'

new_content = r'''    def _day_2_song_lyrics(self, track_info, song_data):
        """
        Day 2: "The 5 Instruments of Fluency" (Pattern Recognition Q&A)
        Focuses on specific verbs: Ser, Estar, Tener, Querer, Poder.
        Generates contextual Q&A pairs.
        """
        title = track_info.get('Title', 'Unknown Song')
        artist = track_info.get('Artist', 'Unknown Artist')
        link = track_info.get('Link', '#')
        
        # --- 1. Thematic Definitions ---
        themes = {
            "estar": {"Title": "Present Condition", "Focus": "Current State / Location"},
            "tener": {"Title": "Possession/Feelings", "Focus": "What you have (physically or emotionally)"},
            "querer": {"Title": "Caring", "Focus": "Affection / Desire"},
            "ser": {"Title": "Essence", "Focus": "Identity / Characteristics"},
            "poder": {"Title": "Capability", "Focus": "Possibility / Ability"}
        }
        
        # --- 2. Extract Sentences ---
        full_lyrics = song_data.get('Full_Lyrics') or song_data.get('Spanish_Lyrics', '')
        
        # Helper to find sentences with a verb
        import re
        def find_sentences_with_verb(verb_root, lyrics):
            found = []
            # Split by newlines first to respect song structure
            lines = lyrics.split('\n')
            for s in lines:
                s = s.strip()
                if not s: continue
                
                # Filter out obvious metadata/noise
                if "Contributors" in s or "Embed" in s or "Translations" in s:
                    continue
                if len(s) < 10: # Skip very short snippets
                    continue
                    
                # Common forms map
                forms = []
                if verb_root == "tener": forms = ["tengo", "tienes", "tiene", "tenemos", "tienen"]
                elif verb_root == "estar": forms = ["estoy", "estás", "está", "estamos", "están"]
                elif verb_root == "querer": forms = ["quiero", "quieres", "quiere", "queremos", "quieren"]
                elif verb_root == "ser": forms = ["soy", "eres", "es", "somos", "son"]
                elif verb_root == "poder": forms = ["puedo", "puedes", "puede", "podemos", "pueden"]
                
                found_match = False
                for f in forms:
                    if re.search(r'(?i)\b' + re.escape(f) + r'\b', s):
                        found_match = True
                        break
                
                if found_match:
                    found.append(s)
            return found

        # --- 3. Build Content Stack ---
        content_stack_html = ""
        content_stack_text = ""
        
        # Order of presentation - BETA: ESTAR ONLY
        target_verbs = ["estar"]
        
        for verb in target_verbs:
            sentences = find_sentences_with_verb(verb, full_lyrics)
            if not sentences: continue
            
            # Define forms for bolding (same as finder logic)
            forms = []
            if verb == "tener": forms = ["tengo", "tienes", "tiene", "tenemos", "tienen"]
            elif verb == "estar": forms = ["estoy", "estás", "está", "estamos", "están"]
            elif verb == "querer": forms = ["quiero", "quieres", "quiere", "queremos", "quieren"]
            elif verb == "ser": forms = ["soy", "eres", "es", "somos", "son"]
            elif verb == "poder": forms = ["puedo", "puedes", "puede", "podemos", "pueden"]

            # Retrieve stored Q&A for this song
            stored_qna = []
            if getattr(self, 'storage', None):
                 stored_qna = self.storage.get_day_2_questions(track_info.get('title', 'Unknown'))

            # --- FORCE USER EXAMPLE (BETA) ---
            # "Tengo la camisa negra, hoy mi amor está de luto"
            # Ensure this specific sentence is processed FIRST if found
            user_example_key = "hoy mi amor está de luto" # Keyword matching
            # Filter manually to find the best match for the user example
            user_example_found = None
            for s in sentences:
                if user_example_key in s.lower():
                    user_example_found = s
                    break
            
            if user_example_found:
                sentences.remove(user_example_found)
                sentences.insert(0, user_example_found)
            
            # --- MELODY DEFINITIONS (HTML TEMPLATES) ---
            # Layout Order: Theory -> Example -> Formulas -> Particularity -> Prepositions
            # Minimalist Design: Transparent, Black Text, No Borders
            
            melody_templates = {
                "condition": """
                <div style="margin-bottom: 60px; padding: 0; background-color: transparent;">
                    <h3 style="margin-top: 0; color: #000; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; margin-bottom: 10px;">
                        Melody of Present Condition
                    </h3>
                    
                    <!-- Meaning -->
                    <p style="color: #000; font-size: 16px; margin-bottom: 20px; line-height: 1.5;">
                        (Current State) → (<strong>Estar</strong>)<br>
                        Your condition or the condition of something right now
                    </p>
                    
                    <!-- INJECTED EXAMPLE (Top Priority) -->
                    <div style="border-top: 2px solid #000; border-bottom: 2px solid #000; padding: 20px 0; margin-bottom: 25px;">
                        <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                        {example_slot}
                    </div>

                    <!-- Formulas -->
                     <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Formulas (Speech Engineering):</p>
                    <ul style="color: #000; font-size: 15px; margin-top: 0; padding-left: 20px; margin-bottom: 25px; line-height: 1.6;">
                        <li>To say the condition of something: <strong>(Está) + (Adjective)</strong><br><em style="color:#555;">Está abierto / Está delicioso</em></li>
                        <li>To say your personal condition: <strong>(Estoy) + (Adjective)</strong><br><em style="color:#555;">Estoy listo / Estoy bien</em></li>
                    </ul>

                    <!-- Particularity & Prepositions -->
                    <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Verb Particularity:</p>
                    <p style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px;">Estar → Está / Estoy / Estaba</p>

                    <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Prepositions for this Melody:</p>
                    <p style="color: #000; font-size: 15px; margin-top: 0;">→ No main preposition — connects directly to adjectives</p>
                </div>
                """,
                
                "mood": """
                <div style="margin-bottom: 60px; padding: 0; background-color: transparent;">
                     <h3 style="margin-top: 0; color: #000; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; margin-bottom: 10px;">
                        Melody of the Mood
                    </h3>
                    
                    <!-- Meaning -->
                    <p style="color: #000; font-size: 16px; margin-bottom: 20px; line-height: 1.5;">
                        (Emotional State) → (<strong>Estar</strong>)<br>
                        How you feel now / how you were feeling before
                    </p>

                     <!-- INJECTED EXAMPLE -->
                    <div style="border-top: 2px solid #000; border-bottom: 2px solid #000; padding: 20px 0; margin-bottom: 25px;">
                        <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                        {example_slot}
                    </div>

                    <!-- Formulas -->
                    <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Formulas (Speech Engineering):</p>
                    <ul style="color: #000; font-size: 15px; margin-top: 0; padding-left: 20px; margin-bottom: 25px; line-height: 1.6;">
                        <li>To say how you feel now: <strong>(Estoy) + (Emotion)</strong><br><em style="color:#555;">Estoy feliz / Estoy triste</em></li>
                        <li>To say the cause: <strong>(Estoy) + (De) + (Reason)</strong><br><em style="color:#555;">Estoy de luto</em></li>
                    </ul>

                    <!-- Particularity & Prepositions -->
                    <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Verb Particularity:</p>
                    <p style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px;">Estar → Estoy / Estaba</p>

                    <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Prepositions for this Melody:</p>
                    <p style="color: #000; font-size: 15px; margin-top: 0;">→ CON (carrying emotion) / DE (cause) / EN (where it is)</p>
                </div>
                """,
                
                "space": """
                <div style="margin-bottom: 60px; padding: 0; background-color: transparent;">
                     <h3 style="margin-top: 0; color: #000; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; margin-bottom: 10px;">
                        Melody of Space
                    </h3>
                    
                    <!-- Meaning -->
                     <p style="color: #000; font-size: 16px; margin-bottom: 20px; line-height: 1.5;">
                        (Position & Location) → (<strong>Estar</strong>)<br>
                        Where you are and who you’re with
                    </p>

                     <!-- INJECTED EXAMPLE -->
                    <div style="border-top: 2px solid #000; border-bottom: 2px solid #000; padding: 20px 0; margin-bottom: 25px;">
                        <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                        {example_slot}
                    </div>

                    <!-- Formulas -->
                     <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Formulas (Speech Engineering):</p>
                    <ul style="color: #000; font-size: 15px; margin-top: 0; padding-left: 20px; margin-bottom: 25px; line-height: 1.6;">
                        <li>To say where you are: <strong>(Estoy) + (En) + (Place)</strong><br><em style="color:#555;">Estoy en casa</em></li>
                        <li>To say who you are with: <strong>(Estoy) + (Con) + (Person)</strong><br><em style="color:#555;">Estoy con ella</em></li>
                    </ul>

                     <!-- Particularity & Prepositions -->
                    <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Verb Particularity:</p>
                    <p style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px;">Estar → Estoy / Estaba</p>

                    <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Prepositions for this Melody:</p>
                    <p style="color: #000; font-size: 15px; margin-top: 0;">→ EN (location) / CON (company) / A (direction)</p>
                </div>
                """
            }
            
            def get_estar_melody(sentence):
                s = sentence.lower()
                # 1. MOOD / EMOTION (Trumps condition often)
                if any(w in s for w in ["triste", "feliz", "contento", "enojado", "luto", "pena", "dolor", "bien", "mal", "sentir", "llorar", "reir", "muela"]):
                    return "mood"
                # 2. SPACE / LOCATION (Prepositions en/con/aqui/alla)
                if any(w in s for w in [" en ", " con ", "aquí", "allá", "donde", "casa", "calle", "mundo"]):
                    return "space"
                # 3. DEFAULT: PRESENT CONDITION (Adjectives, states)
                return "condition"

            # --- GROUPING BY MELODY ---
            melody_groups = {"mood": [], "space": [], "condition": []}
            
            for sent in sentences:
                melody_key = get_estar_melody(sent)
                if melody_key in melody_groups:
                    melody_groups[melody_key].append(sent)

            # --- RENDER EACH MELODY FOUND ---
            # Priority Order: Mood -> Space -> Condition
            display_order = ["mood", "space", "condition"]
            
            for melody_key in display_order:
                group_sentences = melody_groups.get(melody_key, [])
                if not group_sentences: continue
                
                # Pick the BEST example
                best_example = None
                for s in sentences:
                    # User example logic is already handled by 'sentences' order? 
                    # Sentences has user_example first.
                    if s in group_sentences:
                        best_example = s
                        break
                
                if not best_example: best_example = group_sentences[0]

                # Generate Q&A for this example
                eng_q, esp_q = "", ""
                # Contextual Logic
                if melody_key == "mood":
                    eng_q, esp_q = "How do you <b>feel</b>?", "¿Cómo te <b>sientes</b>?"
                elif melody_key == "space":
                    eng_q, esp_q = "Where <b>are</b> you?", "¿Dónde <b>estás</b>?"
                else: # condition
                    eng_q, esp_q = "How <b>are</b> you?", "¿Cómo <b>estás</b>?"
                
                # Answer Bolding
                ans_text = best_example
                for f in forms:
                    if f in best_example.lower():
                        ans_text = re.sub(f"(?i)(\\b{f}\\b)", r"<b>\1</b>", best_example)
                        break 
                
                # Build Example HTML
                # Minimal Example Block
                example_html = f"""
                <div style="margin-top: 0; margin-bottom: 0; padding-left: 0;">
                    <p style="margin: 0; color: #000; font-size: 18px; font-weight: 400; line-height: 1.4; margin-bottom: 5px;">{eng_q}</p>
                    <p style="margin: 0; color: #000; font-size: 18px; font-weight: 400; line-height: 1.4; font-style: italic; margin-bottom: 20px;">{esp_q}</p>
                    
                    <div style="margin: 0; color: #000; font-size: 20px; font-weight: 400; font-style: normal; line-height: 1.4; background-color: transparent;">
                        {ans_text}
                    </div>
                </div>
                """
                
                # Get Template
                template = melody_templates.get(melody_key)
                
                # Inject Example into Template
                block_html = template.replace("{example_slot}", example_html).replace("{song_title}", track_info.get('title', 'The Song'))
                
                content_stack_html += block_html
                content_stack_text += f"[{melody_key.upper()}] Q: {eng_q} / A: {ans_text}\\n"

        if not content_stack_html:
             content_stack_html = "<p>No specific melody cues found for this song today. Just listen and enjoy!</p>"
        
        # --- 4. Final Template Assembly ---
        safe_title = title.replace(" ", "%20")
        minigame_link = f"https://ifeelsochatty.com/minigames?song={safe_title}"
        flashcard_link = f"https://ifeelsochatty.com/flashcards?song={safe_title}"
        
        subject = f"🎵 Day 2: The Melody of Language ({title})"
        
        body_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Circular+Std:wght@400;700;900&family=Helvetica+Neue:wght@400;700&display=swap');
                body {{ margin: 0; padding: 0; background-color: #f5f5f5; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }}
            </style>
        </head>
        <body style="background-color: #f5f5f5; margin: 0; padding: 40px 10px; color: #333;">
            
            <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 40px 40px; border-radius: 4px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                
                <!-- SPOTIFY DARK CARD -->
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #121212; border-radius: 8px; overflow: hidden; max-width: 500px; margin: 0 auto 40px auto; box-shadow: 0 8px 16px rgba(0,0,0,0.3);">
                    <tr>
                        <td style="padding: 20px 25px; vertical-align: middle;">
                            <div style="font-family: 'Helvetica Neue', Helvetica, sans-serif; color: #ffffff; font-size: 18px; font-weight: bold; margin-bottom: 4px; text-decoration: none;">
                                <a href="{link}" target="_blank" style="color: white; text-decoration: none;">{title}</a>
                            </div>
                            <div style="font-family: 'Helvetica Neue', Helvetica, sans-serif; color: #b3b3b3; font-size: 13px; font-weight: 400;">
                                Song • {artist}
                            </div>
                        </td>
                        <td width="60" align="right" style="padding: 20px 25px; vertical-align: middle;">
                            <a href="{link}" target="_blank" style="display: block; width: 48px; height: 48px; background-color: #1DB954; border-radius: 50%; line-height: 48px; text-align: center; text-decoration: none;">
                                <span style="color: black; font-size: 24px; display: inline-block; padding-left: 4px;">&#9658;</span>
                            </a>
                        </td>
                    </tr>
                </table>
                
                <!-- Content Stack -->
                <div style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333;">
                    <p style="font-size: 14px; margin-bottom: 40px; color: #666; font-style: italic; text-align: center; line-height: 1.6;">
                        These verbs are the <strong>Melodies of Existence</strong>. They command how we express Being, State, Possession, Desire, and Ability. Listen to how they change the meaning of the song.
                    </p>
                    
                    {content_stack_html}
                </div>

                <!-- Footer -->
                <div style="margin-top: 50px; text-align: center; border-top: 1px solid #eee; padding-top: 30px;">
                     <div style="display: inline-block;">
                        <a href="{flashcard_link}" style="display: inline-block; color: #333; text-decoration: none; font-weight: bold; margin: 0 15px; font-size: 13px; border-bottom: 1px solid #333;">
                            Review Vocabulary
                        </a>
                    </div>
                    <div style="display: inline-block;">
                        <a href="{minigame_link}" style="display: inline-block; color: #333; text-decoration: none; font-weight: bold; margin: 0 15px; font-size: 13px; border-bottom: 1px solid #333;">
                            Play Mini-Games
                        </a>
                    </div>
                </div>
                
                 <!-- Legal -->
                <p style="text-align: center; color: #ccc; font-size: 10px; margin-top: 30px;">
                    Song references are used solely for educational listening purposes. Lyrics are not reproduced.
                </p>
                
            </div>
        </body>
        </html>
        """
        
        body_text = f"Day 2: The Melody of... ({title})\\n\\n{content_stack_text}\\n\\nReview: {flashcard_link}"
        return subject, body_html, body_text'''

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Replace lines 251-614 (indices 250 to 614)
# Note: lines list is 0-indexed, file lines are 1-indexed.
# Line 251 is index 250.
# Line 614 is index 613.
# But slice end is exclusive, so 614.
lines[250:614] = [new_content + '\n']

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Safely updated content_manager.py")
