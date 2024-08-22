import requests
from django.conf import settings
from django.core.files.storage import Storage
from django.core.files.base import ContentFile
from django.utils.deconstruct import deconstructible

@deconstructible
class FileStorage(Storage):
    def __init__(self, api_token=None):
        self.api_token = api_token or settings.GOFILE_API_TOKEN
        self.base_url = "https://api.gofile.io"

    def _get_upload_server(self):
        response = requests.get(f"{self.base_url}/servers")
        response.raise_for_status()
        data = response.json()
        if data['status'] == 'ok':
            return data['data']['servers'][0]['name']  # Use the first server
        raise Exception("Failed to get GoFile server")

    def _open(self, name, mode='rb'):
        url = name  # In this implementation, 'name' is the download URL
        response = requests.get(url)
        response.raise_for_status()
        return ContentFile(response.content)

    def _save(self, name, content):
        server = self._get_upload_server()
        upload_url = f"https://{server}.gofile.io/contents/uploadfile"
        
        files = {'file': (name, content)}
        data = {'token': self.api_token}
        
        response = requests.post(upload_url, files=files, data=data, 
                                 headers={'Authorization': f'Bearer {self.api_token}'})
        response.raise_for_status()
        
        result = response.json()
        if result['status'] == 'ok':
            return result['data']['downloadPage']  # Return the download URL as the file name
        raise Exception(f"Failed to upload file: {result['status']}")

    def delete(self, name):
        # GoFile doesn't provide a direct method to delete files
        # You might need to keep track of file IDs separately
        raise NotImplementedError("GoFile doesn't support file deletion via API")

    def exists(self, name):
        # Since 'name' is the download URL, we can check if it's accessible
        try:
            response = requests.head(name)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def url(self, name):
        return name  # 'name' is already the download URL

    def size(self, name):
        # GoFile doesn't provide a method to get file size
        raise NotImplementedError("GoFile doesn't provide file size information")

    def listdir(self, path):
        # GoFile doesn't provide a method to list files
        raise NotImplementedError("GoFile doesn't support listing files")