import os
import json
import gspread
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class Storage:
    def __init__(self, credentials_path="credentials.json", token_path="token.json", product="ifeelsochatty"):
        self.credentials_path = credentials_path
        self.token_path = token_path
        self.product = product
        self.scopes = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        self.client = None
        self.master_sheet_name = "Chatic_Master_DB" # Default name, but we use ID mostly
        self._authenticate()

    def _authenticate(self):
        """
        Authenticates with Google Sheets.
        Supports Service Account (simpler, headless) which works for editing shared sheets.
        Checks for GOOGLE_CREDENTIALS_JSON env var first (for Cloud/Render), then local file.
        """
        # 1. Try Environment Variable (Cloud Deployment)
        google_creds_json = os.getenv("GOOGLE_CREDENTIALS_JSON")
        if google_creds_json:
            try:
                creds_dict = json.loads(google_creds_json)
                self.client = gspread.service_account_from_dict(creds_dict)
                print("Authenticated using GOOGLE_CREDENTIALS_JSON env var.")
                return
            except Exception as e:
                print(f"Error loading credentials from env var: {e}")
                # Fall through to file check

        # 2. Try Local File (Local Development)
        if not os.path.exists(self.credentials_path):
            print(f"Error: {self.credentials_path} not found and GOOGLE_CREDENTIALS_JSON not set.")
            return

        try:
            self.client = gspread.service_account(filename=self.credentials_path)
            print("Authenticated using local Service Account file.")
        except Exception as e:
            print(f"Service Account Auth failed: {e}")
            self.client = None

    def get_or_create_sheet(self):
        """
        Gets the Master Spreadsheet by ID based on the configured product.
        """
        if not self.client:
            return None

        # Sheet IDs provided by user / config
        SHEET_IDS = {
            "ifeelsochatty": "1RqHrKVi_241nKOkCG2hfuTsO3vdpMpIDueiFQm5snXA",
            "chatic": "1RqHrKVi_241nKOkCG2hfuTsO3vdpMpIDueiFQm5snXA", # Alias for backward compatibility
            "fluency": "1FBTeBWYsrTDWo_jRiT1_gjpq2EZFGTSI-zkcbIu_VxE"
        }
        
        target_product = self.product.lower()
        if "fluency" in target_product:
             target_product = "fluency"
        
        SHEET_ID = SHEET_IDS.get(target_product, SHEET_IDS["ifeelsochatty"]) # Default to ifeelsochatty

        try:
            # Open by Key (ID) is more robust
            sheet = self.client.open_by_key(SHEET_ID)
            print(f"Connected to Sheet ({self.product}): {sheet.title}")
        except gspread.SpreadsheetNotFound:
            print(f"Error: Could not find Sheet with ID: {SHEET_ID} for product {self.product}")
            return None

        # Ensure tabs exist - Common Schema for now, can diverge later
        self._ensure_tab(sheet, "Songs_DB", ["Spotify_ID", "Artist", "Title", "Link", "Extracted_Sentences", "Word_Analysis", "Level_1_Verbs", "Full_Lyrics", "Last_Updated"])
        self._ensure_tab(sheet, "User_Logs", ["Email", "Spotify_ID", "Song_Title", "Date_Sent"])
        self._ensure_tab(sheet, "Users", ["Email", "Phone", "Name", "Preferences", "Active", "Start_Date", "Stripe_Customer_ID", "Source"])
        
        return sheet

    def _ensure_tab(self, sheet, title, headers):
        try:
            worksheet = sheet.worksheet(title)
        except gspread.WorksheetNotFound:
            worksheet = sheet.add_worksheet(title=title, rows=100, cols=len(headers))
            worksheet.append_row(headers)
        return worksheet

    def get_queue_links(self):
        """
        Reads Spotify links from the 'Queue' tab.
        Assumes links are in Column A (index 0).
        Returns a list of tuples: (row_index, link)
        """
        sheet = self.get_or_create_sheet()
        if not sheet: return []

        self._ensure_tab(sheet, "Queue", ["Spotify_Link", "Status"])
        ws = sheet.worksheet("Queue")
        
        # Get all values from Col A (skip header)
        rows = ws.get_all_values()
        if not rows: return []
        
        links = []
        for i, row in enumerate(rows): # Keep 0-based index for logic, but gspread uses 1-based for rows
            row_num = i + 1
            if row_num == 1: continue # Skip header
            
            if row and row[0].startswith("http"):
                # Check status in Col B (if exists)
                status = row[1] if len(row) > 1 else ""
                if status.lower() != "done":
                    links.append((row_num, row[0]))
        
        return links

    def update_queue_status(self, row_index, status):
        """
        Updates the Status column (Col B) for a specific row in the Queue tab.
        """
        sheet = self.get_or_create_sheet()
        if not sheet: return

        try:
            ws = sheet.worksheet("Queue")
            ws.update_cell(row_index, 2, status) # Col 2 is Status
        except Exception as e:
            print(f"Error updating queue status: {e}")

    def log_song(self, track_info, sentences, analysis, verb_map, full_lyrics=""):
        """
        Logs song data to Songs_DB. Check for duplicates first.
        """
        sheet = self.get_or_create_sheet()
        if not sheet: return False

        ws = sheet.worksheet("Songs_DB")
        spotify_id = track_info.get('external_url', 'unknown_id') # Using URL as ID for checking since we extract ID elsewhere
        
        headers = ["Spotify_ID", "Artist", "Title", "Link", "Extracted_Sentences", "Word_Analysis", "Word_Analysis_print", "Level_1_Verbs", "Full_Lyrics", "Last_Updated"]
        self._ensure_tab(sheet, "Songs_DB", headers)
        ws = sheet.worksheet("Songs_DB")
        
        # Check if exists (Simple check by URL column - assuming col 4 is Link)
        # Check if exists (Simple check by URL column - assuming col 4 is Link)
        try:
            cell = ws.find(spotify_id)
            if cell:
                print(f"Updating existing entry for {track_info.get('title')}...")
                ws.delete_rows(cell.row)
        except gspread.CellNotFound:
            pass

        # Prepare Data
        # Flatten analysis for storage (JSON string)
        # ensure_ascii=False ensures 'adiós' stays 'adiós' instead of 'adi\u00f3s'
        analysis_json = json.dumps(analysis, ensure_ascii=False)
        
        # Create Readable Print Version
        # Format: "Nouns: a, b | Verbs: c, d"
        print_parts = []
        for category, words in analysis.items():
            if words:
                print_parts.append(f"{category}: {', '.join(words)}")
        analysis_print = "\n\n".join(print_parts) # Double newline for readability in cell

        sentences_str = " | ".join(sentences)

        # Format Level 1 Verbs as "Verb:Conjugation" pairs (e.g., "tener:tengo, saber:sé")
        pair_list = []
        for verb, entries in verb_map.items():
            # Get unique conjugated forms for this verb (lowercase to avoid Tener:Tengo vs tener:tengo)
            unique_forms = sorted(list(set(entry.get('conjugated', '').lower() for entry in entries)))
            for form in unique_forms:
                if form:
                    pair_list.append(f"{verb}:{form}")
        
        level_1_str = ", ".join(pair_list)
        
        row = [
            spotify_id,
            track_info.get('artist'),
            track_info.get('title'),
            track_info.get('external_url'),
            sentences_str,
            analysis_json,
            analysis_print, # New Readable Column
            level_1_str, 
            full_lyrics, # New Column
            str(os.environ.get('CurrentTime', 'Now')) 
        ]
        
        ws.append_row(row)

        # --- Update Verb_Index (Relational Table) ---
        if verb_map:
            self._update_verb_index(track_info, verb_map)

        print(f"Logged song: {track_info.get('title')}")
        return True

    def get_all_songs(self):
        """
        Retrieves all songs from Songs_DB.
        Returns a list of dicts.
        """
        sheet = self.get_or_create_sheet()
        if not sheet: return []

        try:
            ws = sheet.worksheet("Songs_DB")
            return ws.get_all_records()
        except Exception as e:
            print(f"Error fetching songs: {e}")
            return []

    def _update_verb_index(self, track_info, verb_map):
        """
        Appends entries to the Verb_Index tab.
        Schema: Verb | Sentence | Tense | Difficulty | Song_Title | Link | Safety
        """
        sheet = self.get_or_create_sheet()
        if not sheet: return

        # Define Headers (Added Safety Column)
        headers = ["Verb", "Conjugated", "Sentence", "Tense", "Difficulty", "Song_Title", "Link", "Safety"]
        self._ensure_tab(sheet, "Verb_Index", headers)
        ws = sheet.worksheet("Verb_Index")
        
        rows_to_add = []
        for verb, entries in verb_map.items():
            for entry in entries:
                # Calculate Safety Status String
                is_safe = entry.get('is_safe', True)
                reason = entry.get('safety_reason', 'Safe')
                safety_str = "Safe" if is_safe else f"UNSAFE: {reason}"

                rows_to_add.append([
                    verb,
                    entry.get('conjugated', ''),
                    entry['sentence'],
                    entry['tense'],
                    entry['difficulty'],
                    track_info.get('title'),
                    track_info.get('external_url'),
                    safety_str # New Column
                ])
        

        
        if rows_to_add:
            ws.append_rows(rows_to_add)

    def add_user(self, email, phone, name, preferences="both", start_date=None, stripe_id=None, source="chatic"):
        """
        Adds or updates a user in the Users tab.
        """
        sheet = self.get_or_create_sheet()
        if not sheet: return False
        
        # Ensure Headers include new columns
        headers = ["Email", "Phone", "Name", "Preferences", "Active", "Start_Date", "Stripe_Customer_ID", "Source"]
        self._ensure_tab(sheet, "Users", headers)
        ws = sheet.worksheet("Users")
        
        # Check if user exists (by Email)
        try:
            cell = ws.find(email)
            if cell:
                print(f"Updating existing user {email}...")
                ws.delete_rows(cell.row)
        except gspread.CellNotFound:
            pass
            
        row = [
            email, 
            phone, 
            name, 
            preferences, 
            "TRUE", 
            str(start_date) if start_date else "", 
            str(stripe_id) if stripe_id else "",
            source
        ]
        ws.append_row(row)
        print(f"User {name} added/updated via {source}.")
        return True

    def get_active_users(self):
        """
        Returns a list of active users.
        """
        sheet = self.get_or_create_sheet()
        if not sheet: return []
        
        ws = sheet.worksheet("Users")
        
        # Use get_all_values to avoid 'duplicate header' error if there are empty cols
        rows = ws.get_all_values()
        if not rows or len(rows) < 2:
            return []
            
        headers = rows[0]
        data = rows[1:]
        
        active_users = []
        for row_idx, row_data in enumerate(data):
            # Create dict based on known headers
            user_dict = {}
            for col_idx, header in enumerate(headers):
                if col_idx < len(row_data) and header.strip():
                     user_dict[header.strip()] = row_data[col_idx]
            
            # Check Active status
            is_active = str(user_dict.get("Active", "")).upper() == "TRUE"
            if is_active:
                active_users.append(user_dict)
                
        return active_users

