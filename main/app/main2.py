import os
import time
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive"]

import os

def upload_to_google_drive(file_path, service, folder_id):
    if os.path.exists(file_path):  # Check if the file exists
        try:
            file_metadata = {
                "name": os.path.basename(file_path),
                "parents": [folder_id]
            }
            media = MediaFileUpload(file_path)
            upload_file = service.files().create(
                body=file_metadata,
                media_body=media,
                fields="id"
            ).execute()
            print("Backed up file: " + file_path)
        except HttpError as e:
            print("Error: " + str(e))

class MyHandler(FileSystemEventHandler):
    def __init__(self, service, folder_id):
        self.service = service
        self.folder_id = folder_id

    def on_created(self, event):
        if not event.is_directory and not event.src_path.startswith('.goutputstream'):
            time.sleep(3)  # Introduce a short delay
            upload_to_google_drive(event.src_path, self.service, self.folder_id)

    def on_moved(self, event):
        if not event.is_directory and not event.dest_path.startswith('.goutputstream'):
            time.sleep(3)  # Introduce a short delay
            upload_to_google_drive(event.dest_path, self.service, self.folder_id)

    def on_modified(self, event):
        if not event.is_directory and not event.src_path.startswith('.goutputstream'):
            time.sleep(3)  # Introduce a short delay
            upload_to_google_drive(event.src_path, self.service, self.folder_id)

def main():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("drive", "v3", credentials=creds)
    response = service.files().list(
        q="name='BackupFolder4' and mimeType='application/vnd.google-apps.folder'",
        spaces='drive'
    ).execute()
    if not response['files']:
        file_metadata = {
            "name": "BackupFolder4",
            "mimeType": "application/vnd.google-apps.folder"
        }    
        file = service.files().create(body=file_metadata, fields="id").execute()
        folder_id = file.get('id')
    else:
        folder_id = response['files'][0]['id']

    # Backup initial contents of the folder
    for root, dirs, files in os.walk('backupfiles'):
        for file in files:
            upload_to_google_drive(os.path.join(root, file), service, folder_id)

    observer = Observer()
    event_handler = MyHandler(service, folder_id)
    observer.schedule(event_handler, path='backupfiles', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()

