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
            "saber", "querer", "dar", "llegar", "pasar", "poner", "parecer", 
            "creer", "hablar", "comer", "vivir", "tomar", "trabajar", "sentir"
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


    def generate_reverse_qa(self, sentence, verb_lemma, verb_token):
        """
        Generates a 'Natural' Question for a given sentence and target verb.
        Uses context-aware heuristics (e.g. 'ir a' = future) and template fallbacks.
        """
        s_lower = sentence.lower()
        
        # 1. CONTEXT AWARE HEURISTICS (Specific Usages)
        
        # IR (Movement vs Future)
        if verb_lemma == "ir":
            # Check for "ir a + infinitive" pattern (Future)
            # Simple check: "va a", "voy a", "vas a", "van a", "vamos a" followed by word
            if re.search(r'\b(voy|vas|va|vamos|van)\s+a\s+\w+', s_lower):
                 return { "question_en": "What is going to happen?", "question_es": "¿Qué va a pasar?" }
            # Check for reflexive "irse" (leaving)
            if any(w in s_lower for w in ["me voy", "te vas", "se va", "nos vamos", "se van"]):
                 return { "question_en": "Who is leaving?", "question_es": "¿Quién se va?" }
            # Default: Movement
            return { "question_en": "Where is the movement going?", "question_es": "¿Hacia dónde va el movimiento?" }

        # TENER (Possession vs Obligation vs Idioms)
        if verb_lemma == "tener":
            # Obligation (Tener que)
            if "que" in s_lower and re.search(r'\btienes?\s+que', s_lower):
                return { "question_en": "What is necessary to do?", "question_es": "¿Qué se tiene que hacer?" }
            # Idioms (Miedo, Ganas, Culpa, Razón)
            if "ganas" in s_lower:
                return { "question_en": "What is the desire?", "question_es": "¿De qué tienes ganas?" }
            if "miedo" in s_lower:
                return { "question_en": "What is the fear?", "question_es": "¿De qué tienes miedo?" }
            if "culpa" in s_lower:
                return { "question_en": "Who has the blame?", "question_es": "¿Quién tiene la culpa?" }
            # Default: Possession
            return { "question_en": "What is being had/possessed?", "question_es": "¿Qué se tiene?" }

        # DAR (Giving vs Idioms)
        if verb_lemma == "dar":
            # Dar la gana
            if "gana" in s_lower:
                 return { "question_en": "What does the soul want?", "question_es": "¿Qué te da la gana?" }
            # Dar cuenta
            if "cuenta" in s_lower:
                 return { "question_en": "What is being realized?", "question_es": "¿De qué se da cuenta?" }
            # Default: Giving
            return { "question_en": "What is being given?", "question_es": "¿Qué se da?" }

        # QUERER (Wanting vs Loving)
        if verb_lemma == "querer":
            if any(w in s_lower for w in ["te", "me", "lo", "la"]) and "mas" not in s_lower: 
                # Heuristic: Object pronoun usually implies loving a person in songs, unless "mas" (want more)
                return { "question_en": "Who is loved?", "question_es": "¿A quién se quiere?" }
            return { "question_en": "What is wanted?", "question_es": "¿Qué se quiere?" }

        # 2. DEPENDENCY-BASED GENERATION (Dynamic & Specific)
        # Check if we have a valid Spacy token to work with
        if verb_token and hasattr(verb_token, 'children'):
            # Find Direct Object (What?)
            dobj = next((t for t in verb_token.children if t.dep_ in ['dobj', 'obj']), None)
            # Find Subject (Who?)
            nsubj = next((t for t in verb_token.children if t.dep_ in ['nsubj', 'nsubj:pass']), None)
            # Find Prepositional Object (Where/How?) -- complicated, simplifying
            
            # Case A: Transitive Verb with Object (e.g. "Tengo la camisa")
            if dobj:
                # "What do I have?" -> "¿Qué tengo?"
                # We need to construct the Spanish Q based on the verb form.
                # This is hard without a conjugator. 
                # BUT we can format it: "¿Qué [verb]?" + (optionally) subject?
                
                # Heuristic: If it has a direct object, ask "What [verb]...?"
                # "Que tengo?" "Que quiero?" "Que perdi?"
                
                # We need to be careful with Pronouns ("Lo quiero").
                if dobj.pos_ == "PRON":
                    return { 
                        "question_en": f"What/Who is {verb_lemma} referring to?", 
                        "question_es": f"¿A qué/quién se refiere '{dobj.text}'?" 
                    }
                
                # Simple Subject Inference for English
                subject_en = "he/she/it"
                aux_en = "does"
                
                v_text = verb_token.text.lower()
                if v_text.endswith('o') and not v_text in ['dijo', 'hizo']: # rough check
                    subject_en = "I"
                    aux_en = "do"
                elif v_text.endswith('as') or v_text.endswith('es'):
                    subject_en = "you"
                    aux_en = "do"
                elif v_text.endswith('mos'):
                    subject_en = "we"
                    aux_en = "do"
                elif v_text.endswith('an') or v_text.endswith('en'):
                    subject_en = "they"
                    aux_en = "do"
                
                # Check explicit nsubj
                if nsubj and nsubj.pos_ in ['PRON', 'PROPN', 'NOUN']:
                    if nsubj.text.lower() in ['yo']: subject_en = "I"; aux_en = "do"
                    elif nsubj.text.lower() in ['tu', 'tú']: subject_en = "you"; aux_en = "do"
                    # else keep he/she/it or use noun? "What does the soul have?"
                
                return {
                    "question_en": f"What {aux_en} {subject_en} {verb_lemma}?", 
                    "question_es": f"¿Qué {verb_token.text}?" 
                }
        
        # 3. GENERIC CONCEPT TEMPLATES (Fallback)
        concept_questions = {
            "hacer": ("What is being done?", "¿Qué se está haciendo?"),
            "decir": ("What is being said?", "¿Qué se dice?"),
            "ver": ("What is being seen?", "¿Qué se ve?"),
            "saber": ("What is known?", "¿Qué se sabe?"),
            "llegar": ("Who or what arrives?", "¿Quién o qué llega?"),
            "pasar": ("What is happening?", "¿Qué pasa?"),
            "vivir": ("How is life lived?", "¿Cómo se vive?"),
            "tomar": ("What is being taken/drunk?", "¿Qué se toma?"),
            "sentir": ("What is the feeling?", "¿Qué se siente?"),
            "trabajar": ("What is the work?", "¿En qué se trabaja?"),
            "comer": ("What is being eaten?", "¿Qué se come?"),
            "hablar": ("What is being spoken about?", "¿De qué se habla?"),
            "poner": ("What is being placed?", "¿Qué se pone?"),
            "poder": ("What is possible?", "¿Qué se puede hacer?"),
        }

        if verb_lemma in concept_questions:
            return {
                "question_en": concept_questions[verb_lemma][0],
                "question_es": concept_questions[verb_lemma][1]
            }

        # 3. ABSOLUTE FALLBACK
        return {
            "question_en": f"What is the action of {verb_lemma}?",
            "question_es": f"¿Cuál es la acción de {verb_lemma}?"
        }


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
                        
                        # --- ARTICLE GAME DATA ---
                        # Get Gender (Fem/Masc)
                        gender = token.morph.get("Gender")
                        if gender:
                            article = "La" if "Fem" in gender else "El"
                            # Store unique capitalized nouns with their article
                            noun_display = token.text.capitalize()
                            # Avoid duplicates by checking if we have this noun already (basic check)
                            # Actually, let's store it in a dict to dedupe
                            if "article_game_data" not in reference_sheet:
                                reference_sheet["article_game_data"] = {}
                            
                            # Simple heuristics to avoid bad ones
                            if len(noun_display) > 2 and word_text not in self.BLOCKLIST:
                                reference_sheet["article_game_data"][noun_display] = article

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

        final_sheet = {}
        for k, v in reference_sheet.items():
            if k == "article_game_data":
                final_sheet[k] = v # Keep as dict
            else:
                final_sheet[k] = sorted(list(v))

        # 2. Sentence Evaluation & Verb Mapping
        lines = [line.strip() for line in cleaned_text.split('\n') if line.strip()]
        
        candidates = []
        verb_sentence_map = defaultdict(list)
        prep_sentence_map = defaultdict(list)

        for line in lines:
            word_count = len(line.split())
            if word_count < 3: continue
            
            doc = self.nlp(line)
            
            # Check for Target Verbs & Prepositions in this specific line
            line_has_target = False
            for token in doc:
                # A. VERBS
                # Include AUX for ser/estar
                if (token.pos_ == "VERB" or token.pos_ == "AUX") and token.lemma_.lower() in self.TARGET_VERBS:
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
                            "conjugated": token.text,
                            "lemma": token.lemma_.lower(),
                            "is_safe": is_safe,
                            "safety_reason": reason,
                            "aux_context": None
                        }
                        
                        # 1. Check HEAD (e.g. "Quiero comer" -> comer.head = quiero)
                        if token.head.pos_ in ['VERB', 'AUX'] and token.head != token:
                             entry["aux_context"] = token.head.lemma_.lower()
                        
                        # 2. Check CHILDREN (e.g. "Puedo comer" -> comer.children = [puedo])
                        # This overrides HEAD if found (as direct aux is usually tighter context)
                        for child in token.children:
                            if child.dep_ in ['aux', 'aux:pass'] and child.pos_ in ['VERB', 'AUX']:
                                entry["aux_context"] = child.lemma_.lower()
                                break
                        
                        # Generate Reverse Q&A for Day 3/4 content
                        qa_entry = self.generate_reverse_qa(line, token.lemma_.lower(), token)
                        if isinstance(qa_entry, dict):
                            entry["question_es"] = qa_entry.get("question_es")
                            entry["question_en"] = qa_entry.get("question_en")
                        else:
                            entry["question_es"] = qa_entry
                            entry["question_en"] = None
                        
                        verb_sentence_map[token.lemma_.lower()].append(entry)
                        line_has_target = True

                # B. PREPOSITIONS
                elif token.pos_ == "ADP":
                    # Simple extraction for Day 4
                    is_safe, reason = self.check_safety(doc)
                    if is_safe and word_count <= 20:
                        entry = {
                            "sentence": line,
                            "lemma": token.lemma_.lower(),
                            "text": token.text,
                            "is_safe": is_safe
                        }
                        prep_sentence_map[token.lemma_.lower()].append(entry)
            
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
            "verb_sentence_map": dict(verb_sentence_map),
            "prep_sentence_map": dict(prep_sentence_map)
        }
