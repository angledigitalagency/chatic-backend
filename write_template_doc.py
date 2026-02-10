import google.oauth2.service_account
from googleapiclient.discovery import build
import os

FILE_ID = "1DCmn47rQGkR79Ls3QOszi1XnqryvSwKwmz23MwXGVjE" # "Templates"
SA_FILE = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS', 'credentials.json')

TEMPLATE_CONTENT = """DAY 2: MELODIES OF EXISTENCE

[STATIC HEADER]
Melodies of Existence
These verbs are the Melodies of Existence. They command how we express Being, State, Possession, Desire, and Ability. Listen to how they change the meaning of the song.
[END STATIC HEADER]

---
[DYNAMIC CONTENT BLOCK - REPEAT FOR EACH MELODY]

## Melody of {{ melody_title }}
(Grammar Concept) → ({{ melody_verb }})
{{ melody_meaning }}

### From {{ song_title }}:
• {{ question }}
{{ sentence_translation }}
**{{ sentence_original }}**

### This Melody sings:
{{ melody_concept }}
**I {{ melody_verb_en }} ({{ melody_verb_es }})** __________________

### Formulas (Speech Engineering):
{{ formula_list }}

### Verb Tense:
Past ← {{ melody_verb }} → Future
{{ verb_past }} ← {{ verb_present }} → {{ verb_future }}

### Prepositions for this Melody:
→ {{ prepositions }}

### Key Reminder:
{{ key_reminder }}

---
[END DYNAMIC CONTENT BLOCK]

[STATIC FOOTER]
Play: El vs La | Review Vocabulary
Song references are used solely for educational listening purposes.
[END STATIC FOOTER]
"""

def write_template_doc():
    print(f"📝 Writing to Template Doc: {FILE_ID}")
    
    try:
        creds = google.oauth2.service_account.Credentials.from_service_account_file(
            SA_FILE, 
            scopes=['https://www.googleapis.com/auth/drive'] # Full Drive scope usually works better
        )
        
        service = build('docs', 'v1', credentials=creds)
        
        # Insert Text at Index 1
        requests = [
            {
                'insertText': {
                    'location': {
                        'index': 1,
                    },
                    'text': TEMPLATE_CONTENT
                }
            }
        ]
        
        result = service.documents().batchUpdate(documentId=FILE_ID, body={'requests': requests}).execute()
        print("✅ Document Updated Successfully!")
                
    except Exception as e:
        print(f"❌ Error writing to doc: {e}")

if __name__ == "__main__":
    write_template_doc()
