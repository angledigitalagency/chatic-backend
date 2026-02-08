import spacy
import re
from collections import defaultdict
from spellchecker import SpellChecker

class Linguist:
    def __init__(self):
        try:
            self.nlp = spacy.load("es_core_news_sm")
            print("Loaded Spanish Model: es_core_news_sm")
        except OSError:
            print("Error: Spacy model 'es_core_news_sm' not found. Please run: python -m spacy download es_core_news_sm")
            self.nlp = None

        # Level 1 Target Verbs
        self.TARGET_VERBS = {
            "ser", "estar", "tener", "hacer", "poder", "decir", "ir", "ver", 
            "saber", "querer", "dar", "llegar", "pasar", "poner", "parecer", 
            "creer", "hablar", "comer", "vivir", "tomar", "trabajar"
        }
        
        # Dictionary for Validation
        try:
            self.spell = SpellChecker(language='es')
            print("Loaded Spanish Dictionary (pyspellchecker)")
        except Exception as e:
            print(f"Error loading dictionary: {e}")
            self.spell = None

        # Custom Blocklist (Words causing issues or English noise)
        self.BLOCKLIST = {
            "home", "come", "on", "english", # True noise/English
            "intro", "verse", "chorus", "bridge", "outro" # Metadata noise
        }
        
        # PG-13 Safety Filter Patterns (Sex, Profanity, Sensitive Topics)
        self.SAFETY_BLOCKLIST = {
            # Profanity / Vulgarity
            "puta", "puto", "perra", "perro", "zorra", "zorro", "mierda", "carajo", "cabron", "cabrón", "culo", "nalga", 
            "verga", "pene", "bicho", "polla", "follar", "chupar", "mamar", "coger", "cojon", "cojones",
            # Sexual / Suggestive (Reggaeton context)
            "enterrar", "enterrártelo", "mamita", "papi", "daddy", "juya", "bellaquera", "sexo", "cama", "desnudo", "desnuda",
            "gemir", "sudar", "caliente", "duro", "suave", "lento", "piel", "beso", "labios", "tocar",
            # Religion / Politics
            "dios", "jesús", "santo", "santa", "iglesia", "amén", "cielo", "diablo", "infierno",
            "política", "presidente", "gobierno", "ley", "nación"
        }



    def clean_lyrics(self, lyrics):
        """
        Removes metadata markers like [Chorus], (Verse 1), and cleans up whitespace.
        Also removes Genius scraping noise (e.g., '12 ContributorsTranslations').
        """
        # Remove [text] and (text) - typically structure markers
        cleaned = re.sub(r'\[.*?\]', '', lyrics)
        cleaned = re.sub(r'\(.*?\)', '', cleaned)

        # Remove Genius metadata noise (e.g. "12 Contributors" or "Translations" headers)
        # Matches lines that look like "3 Contributors" or "Translations...Español"
        # Also catches mashed lines like "36 ContributorsTranslationsEnglish"
        # Aggressive match for the mashed header often found at the start
        cleaned = re.sub(r'\d+\s*ContributorsTranslations\w*', '', cleaned, flags=re.IGNORECASE)
        
        cleaned = re.sub(r'^.*Contributors.*Translations.*$', '', cleaned, flags=re.MULTILINE|re.IGNORECASE)
        cleaned = re.sub(r'^\d+\s*Contributors.*$', '', cleaned, flags=re.MULTILINE|re.IGNORECASE)
        cleaned = re.sub(r'^.*Translations.*$', '', cleaned, flags=re.MULTILINE|re.IGNORECASE)
        cleaned = re.sub(r'^Embed$', '', cleaned, flags=re.MULTILINE|re.IGNORECASE)
        
        return cleaned.strip()

    def check_safety(self, doc_or_text):
        """
        Checks if a sentence is 'Safe' or 'Unsafe' based on Blocklist and NER.
        Returns (is_safe, reason).
        """
        if isinstance(doc_or_text, str):
            doc = self.nlp(doc_or_text)
        else:
            doc = doc_or_text
            
        text_lower = doc.text.lower()
        
        # 1. Keyword Check
        for token in doc:
            if token.lemma_.lower() in self.SAFETY_BLOCKLIST or token.text.lower() in self.SAFETY_BLOCKLIST:
                return False, f"Keyword: {token.text}"
            
        # 2. NER Check (Names)
        for ent in doc.ents:
            if ent.label_ == "PER":
                return False, f"Name: {ent.text}"
                
        return True, "Safe"

    def analyze_lyrics(self, lyrics):
        """
        Analyzes lyrics to produce a reference sheet, valid sentences, and Level 1 verb mapping.
        """
        if not self.nlp:
            return None

        cleaned_text = self.clean_lyrics(lyrics)
        
        # 1. Reference Sheet (Categorization) - Analyze whole text
        full_doc = self.nlp(cleaned_text.replace('\n', ' '))
        
        reference_sheet = defaultdict(set)
        
        for token in full_doc:
            if token.is_alpha and not token.is_stop:
                lemma = token.lemma_.lower()
                word_text = token.text.lower()
                pos = token.pos_
                
                # --- FILTERING & CATEGORIZATION LAYER ---
                
                # 1. Tier 1: STOPWORDS / BLOCKLIST (Delete)
                if word_text in self.BLOCKLIST or lemma in self.BLOCKLIST:
                    continue

                # 2. Tier 2: NEUTRAL SPANISH (Dictionary Valid)
                is_valid_spanish = False
                if self.spell:
                    if word_text in self.spell or lemma in self.spell:
                        is_valid_spanish = True
                    # Trust PROPN as valid "neutral" references if they are names, 
                    # but if it's "English" tagged as PROPN, it might slip.
                    # For strictness, we require dictionary match for Nouns/Verbs/Adjs 
                    # unless it's a strongly typed entity? 
                    # Let's stick to: In Dict = Neutral. Not in Dict = Slang Candidate.
                
                if is_valid_spanish:
                    # Add to Standard Categories
                    if pos in ['NOUN', 'PROPN']:
                        reference_sheet['Nouns'].add(lemma)
                    elif pos == 'VERB':
                        reference_sheet['Verbs'].add(lemma)
                    elif pos == 'ADJ':
                        reference_sheet['Adjectives'].add(lemma)
                    elif pos == 'ADV':
                        reference_sheet['Adverbs'].add(lemma)
                    elif pos == 'ADP':
                        reference_sheet['Prepositions'].add(lemma)
                else:
                    # 3. Tier 3: SLANG CANDIDATES (Preserve cultural data)
                    # Filter out tiny noise or symbols
                    if len(word_text) > 2 and word_text.isalpha():
                        reference_sheet['Slang_Candidates'].add(word_text) # Keep original text for slang, not lemma (often lemma is wrong for slang)

        final_sheet = {k: sorted(list(v)) for k, v in reference_sheet.items()}

        final_sheet = {k: sorted(list(v)) for k, v in reference_sheet.items()}

        # 2. Sentence Evaluation & Verb Mapping
        lines = [line.strip() for line in cleaned_text.split('\n') if line.strip()]
        
        candidates = []
        verb_sentence_map = defaultdict(list)

        for line in lines:
            word_count = len(line.split())
            if word_count < 3: continue
            
            doc = self.nlp(line)
            
            # Check for Target Verbs in this specific line
            line_has_target = False
            for token in doc:
                if token.pos_ == "VERB" and token.lemma_.lower() in self.TARGET_VERBS:
                    # Found a level 1 verb!
                    
                    # 1. Extract Tense/Form
                    tense_list = token.morph.get("Tense")
                    verb_form_list = token.morph.get("VerbForm")
                    
                    if tense_list:
                        tense_str = tense_list[0]
                    elif verb_form_list:
                        form = verb_form_list[0]
                        if form == "Inf": tense_str = "Infinitive"
                        elif form == "Ger": tense_str = "Gerund"
                        elif form == "Part": tense_str = "Participle"
                        else: tense_str = form
                    else:
                        tense_str = "Unknown"
                    
                    # 2. Calculate Difficulty
                    # Simple: <6 words, Medium: 6-12, Hard: >12
                    difficulty = 1 if word_count < 6 else (2 if word_count <= 12 else 3)
                    
                    # 3. Safety Check
                    is_safe, reason = self.check_safety(doc)

                    # Verify length constraint for game (not too long)
                    if word_count <= 20: 
                        entry = {
                            "sentence": line,
                            "tense": tense_str,
                            "difficulty": difficulty,
                            "conjugated": token.text, # Store exact form (e.g. "tengo")
                            "is_safe": is_safe,
                            "safety_reason": reason
                        }
                        verb_sentence_map[token.lemma_.lower()].append(entry)
                        line_has_target = True
            
            # General Candidate Selection (must have verb)
            has_verb = any(token.pos_ == "VERB" for token in doc)
            if has_verb:
                candidates.append(line)

        # Output Preparation
        
        # Strategy: 1 Unique Sentence per Found Level 1 Verb
        # We want to maximize diversity. If we found 5 target verbs, show 5 sentences.
        final_list = []
        seen_sentences = set()
        
        # 1. Iterate through found verbs and pick the best sentence for each
        for verb, entries in verb_sentence_map.items():
            # Sort entries by length (shortest is usually best/cleanest example)
            sorted_entries = sorted(entries, key=lambda x: len(x['sentence']))
            
            for entry in sorted_entries:
                # PG-13 Filter: Skip unsafe sentences for the extracted summary
                if not entry.get('is_safe', True):
                    continue

                sent = entry['sentence']
                # If we haven't used this sentence yet, take it and break (move to next verb)
                # This ensures we try to get a unique sentence for this verb.
                if sent not in seen_sentences:
                    final_list.append(f"{verb}:{sent}")
                    seen_sentences.add(sent)
                    break
            else:
                # If loop finishes without break, try to grab *any* safe sentence (even if duplicate logic triggers)
                # Or just skip if all are unsafe.
                safe_entries = [e for e in sorted_entries if e.get('is_safe', True)]
                
                if safe_entries:
                    sent = safe_entries[0]['sentence']
                    formatted_sent = f"{verb}:{sent}"
                    if formatted_sent not in final_list: # Avoid exact list duplicates
                        final_list.append(formatted_sent)

        # 2. Fallback: If no target verbs found, use General Candidates
        if not final_list:
            unique_general = []
            for c in candidates:
                c_clean = c.lower().strip()
                if c_clean not in seen_sentences:
                    unique_general.append(c)
                    seen_sentences.add(c_clean)
            final_list = unique_general[:3] # Limit to 3 if just random sentences

        # Return All Selected Sentences (No Limit for Target Verbs)
        top_sentences = final_list

        return {
            "reference_sheet": final_sheet,
            "top_sentences": top_sentences,
            "verb_sentence_map": dict(verb_sentence_map)
        }

