import google.oauth2.service_account
from googleapiclient.discovery import build
import os

FOLDER_ID = "1sRYa-l-J_N4GYwANXVJphPDW4LIqCLsx"
SA_FILE = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS', 'credentials.json')

def list_folder_contents():
    print(f"📂 Checking Drive Folder: {FOLDER_ID}")
    
    try:
        creds = google.oauth2.service_account.Credentials.from_service_account_file(
            SA_FILE, 
            scopes=['https://www.googleapis.com/auth/drive'] # Need drive scope
        )
        
        service = build('drive', 'v3', credentials=creds)
        
        # Query files in folder
        query = f"'{FOLDER_ID}' in parents and trashed = false"
        results = service.files().list(q=query, fields="nextPageToken, files(id, name, mimeType)").execute()
        items = results.get('files', [])
        
        if not items:
            print("❌ No files found in folder.")
        else:
            print("✅ Found files:")
            for item in items:
                print(f"📄 {item['name']} ({item['mimeType']}) - ID: {item['id']}")
                
    except Exception as e:
        print(f"❌ Error listing folder: {e}")

if __name__ == "__main__":
    list_folder_contents()
