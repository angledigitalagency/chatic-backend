import google.oauth2.service_account
from googleapiclient.discovery import build
import os

FILE_ID = "1DCmn47rQGkR79Ls3QOszi1XnqryvSwKwmz23MwXGVjE" # "Templates"
SA_FILE = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS', 'credentials.json')

def read_drive_doc():
    print(f"📄 Fetching File Content: {FILE_ID}")
    
    try:
        creds = google.oauth2.service_account.Credentials.from_service_account_file(
            SA_FILE, 
            scopes=['https://www.googleapis.com/auth/drive.readonly']
        )
        
        service = build('drive', 'v3', credentials=creds)
        
        # Determine File Type first?
        # We know it's a Google Doc (application/vnd.google-apps.document)
        # So we MUST export it.
        # Export as text/plain
        request = service.files().export_media(fileId=FILE_ID, mimeType='text/plain')
        content = request.execute()
        
        print("✅ Content Retrieved:")
        print("--------------------------------------------------")
        print(content.decode('utf-8'))
        print("--------------------------------------------------")
                
    except Exception as e:
        print(f"❌ Error reading file: {e}")

if __name__ == "__main__":
    read_drive_doc()
