import random
from agents.storage import Storage

class ActivityManager:
    def __init__(self):
        self.storage = Storage()
        
    def get_content_for_day(self, day_number, user_name="Friend"):
        """
        Returns (subject, body_html, body_text) for the specific day of the cycle.
        day_number is 1-based (1 to 7).
        """
        # Normalize to 1-7 cycle
        cycle_day = ((day_number - 1) % 7) + 1
        
        methods = {
            1: self.day1_group_session,
            2: self.day2_song_intro,
            3: self.day3_fluency_verbs,
            4: self.day4_action_verbs,
            5: self.day5_prepositions,
            6: self.day6_pov_tense,
            7: self.day7_quiz
        }
        
        method = methods.get(cycle_day)
        if method:
            return method(user_name)
        else:
            return "Chatic Daily", "<p>Enjoy your Spanish practice today!</p>", "Enjoy your Spanish practice today!"

    def day1_group_session(self, user_name):
        subject = "Day 1: Join the Group Session 🟢"
        html = f"""
        <h3>Hola {user_name}! It's Day 1.</h3>
        <p>Today we start the cycle with a live group session/game.</p>
        <p><strong>Activity:</strong> Join the group link below.</p>
        <p><a href="https://meet.google.com/xyz-example">Click here to join the Session</a></p>
        <p><em>(Link available to chatbot to choose a game)</em></p>
        """
        text = f"Hola {user_name}! It's Day 1.\nJoin the group session here: https://meet.google.com/xyz-example"
        return subject, html, text

    def day2_song_intro(self, user_name):
        # Fetch a song from DB
        songs = self.storage.get_all_songs()
        song = random.choice(songs) if songs else {}
        title = song.get("Title", "La Camisa Negra")
        artist = song.get("Artist", "Juanes")
        link = song.get("Link", "https://spotify.com")
        lyrics = song.get("Full_Lyrics", "")[:500] + "..." # Snippet
        
        subject = f"Day 2: Song of the Week - {title} 🎵"
        html = f"""
        <h3>Day 2: Song & Lyrics</h3>
        <p>This week we learn with <strong>{title}</strong> by {artist}.</p>
        <p><strong>Task:</strong> Listen to the song and read the lyrics.</p>
        <p><a href="{link}">Listen on Spotify</a></p>
        <hr>
        <h4>Lyrics Snippet:</h4>
        <pre>{lyrics}</pre>
        """
        text = f"Day 2: Song & Lyrics\nSong: {title} by {artist}\nListen: {link}\n\nTask: Listen and read lyrics."
        return subject, html, text

    def day3_fluency_verbs(self, user_name):
        # Ser, Estar, Tener, Querer, Poder
        subject = "Day 3: Fluency Verbs 🧰"
        html = f"""
        <h3>Day 3: The 5 Power Verbs</h3>
        <p>Focus on: <strong>Ser, Estar, Tener, Querer, Poder</strong>.</p>
        <p><strong>Drill:</strong></p>
        <ul>
            <li>To say "I have": <em>Tengo</em></li>
            <li>To say "I want": <em>Quiero</em></li>
            <li>To say "I can": <em>Puedo</em></li>
        </ul>
        <p>Try to find these verbs in this week's song!</p>
        """
        text = "Day 3: Fluency Verbs\nFocus: Ser, Estar, Tener, Querer, Poder.\nTengo (I have), Quiero (I want), Puedo (I can)."
        return subject, html, text

    def day4_action_verbs(self, user_name):
        subject = "Day 4: Action Verbs ⚙️"
        html = f"""
        <h3>Day 4: Moving into Action</h3>
        <p>Focus on: <em>hacer, ir, decir, dar, llegar...</em></p>
        <p><strong>Challenge:</strong> Identify one action verb in the song lines.</p>
        """
        text = "Day 4: Action Verbs\nFocus: hacer, ir, decir, dar, llegar.\nChallenge: Find an action verb in the song."
        return subject, html, text

    def day5_prepositions(self, user_name):
        subject = "Day 5: Preposition Patterns 🪞"
        html = f"""
        <h3>Day 5: Connecting Words</h3>
        <p>Look for: <strong>A, De, Por, Con, En</strong></p>
        <p>Example: <em>Voy <strong>a</strong> casa</em> (Direction).</p>
        """
        text = "Day 5: Prepositions\nLook for: A, De, Por, Con, En.\nExample: Voy a casa."
        return subject, html, text

    def day6_pov_tense(self, user_name):
        subject = "Day 6: Time Travel ⏳"
        html = f"""
        <h3>Day 6: Past & Future</h3>
        <p>Let's change the tense.</p>
        <p>Present: <em>Tengo la camisa negra</em></p>
        <p>Past: <em>Tuve la camisa negra</em></p>
        <p>Future: <em>Tendré la camisa negra</em></p>
        """
        text = "Day 6: Past & Future\nPresent: Tengo\nPast: Tuve\nFuture: Tendré"
        return subject, html, text

    def day7_quiz(self, user_name):
        q_text, answer = self.generate_verb_quiz() # Re-using existing quiz logic
        subject = "Day 7: Weekly Quiz 📝"
        html = f"""
        <h3>Day 7: Test Yourself</h3>
        <p>{q_text}</p>
        <p><em>(Reply with your answer!)</em></p>
        """
        text = f"Day 7: Weekly Quiz\n{q_text}\n(Reply with your answer!)"
        return subject, html, text

    def generate_verb_quiz(self):
        """
        Generates a short verb quiz (fill-in-the-blank).
        Returns: (question_text, answer_key)
        """
        # Fetch Verb Index
        sheet = self.storage.get_or_create_sheet()
        if not sheet: return "Quiz unavailable (DB Error)", None
        
        try:
            ws = sheet.worksheet("Verb_Index")
            rows = ws.get_all_records()
        except Exception as e:
            print(f"Error fetching Verb_Index: {e}")
            return "Quiz unavailable", None
            
        if not rows:
            return "No verbs found. Check back later!", None
            
        # Filter for SAFE entries
        safe_rows = [r for r in rows if "Safe" in str(r.get("Safety", "Safe"))]
        
        if not safe_rows:
            return "No safe verbs available.", None
            
        # Pick random row
        entry = random.choice(safe_rows)
        
        verb = entry.get("Verb")
        sentence = entry.get("Sentence")
        conjugated = entry.get("Conjugated")
        
        if conjugated and conjugated in sentence:
            question = sentence.replace(conjugated, "_____")
            prompt = f"Fill in the blank for '{verb}':\n\n{question}"
            return prompt, conjugated
        else:
            return f"Conjugate '{verb}' found in this song: {entry.get('Song_Title')}", conjugated
