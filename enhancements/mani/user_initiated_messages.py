# import requests
# import json
# from datetime import datetime

class Send:
    def __init__(self):
        self.base_url = "https://iqwhatsapp.airtel.in/gateway/airtel-xchange/basic/whatsapp-manager/v1/session/"
        self.headers = {
          'X-Correlation-Id': 'abcd',
          'X-Date': datetime.utcnow().strftime('%a %d %b %Y %H:%M:%S')+(" GMT"),
          'Authorization': 'Basic QUlSVEVMX0RJR19RajVCRTJQcnVkenhSU0tWdTFKczp6KkxVNktOPGt6c0w/K2JXMg==',
          'Content-Type': 'application/json'
        }
        self.sender = "918904585717"
        self.business_id = 'Hackathon_8904585717'
        
    def text(self, receiver, session_id, text):
        payload = json.dumps({
          "sessionId": session_id,
          "to": receiver,
          "from": self.sender,
          "message": {
            "text": text
          }
        })
        response = requests.request("POST", self.base_url+"send/text", headers=self.headers, data=payload)
        return response.text
    
    def interactive_list(self, receiver, session_id, text, options_list):
        payload = json.dumps({
          "sessionId": session_id,
          "to": receiver,
          "from": self.sender,
          "message": {
            "text": text
          },
          "list": options_list
        })
        response = requests.request("POST", self.base_url+"send/interactive/list", headers=self.headers, data=payload)
        return response.text
    
    def upload_media(self, media_type, media_name, media, media_format):
        payload={'type': media_type,
        'businessId': self.business_id}
        files = [
          ('file',(media_name, media, media_format))
        ]
        response = requests.request("POST", self.base_url+"media", headers=self.headers, data=payload, files=files)
        return response.text
    
    def media(self, receiver, session_id, media_type, media_id, text):
        payload = json.dumps({
          "sessionId": session_id,
          "to": receiver,
          "from": self.sender,
          "mediaAttachment": {
            "type": media_type,
            "id": media_id,
            "caption": text # coming as message
          }
        })
        response = requests.request("POST", self.base_url+"send/media", headers=self.headers, data=payload)
        return response.text
    
    def interactive_buttons(self, receiver, session_id, media_type, media_id, text, button_list):
        payload = json.dumps({
          "sessionId": session_id,
          "to": receiver,
          "from": self.sender,
          "mediaAttachment": {
            "type": media_type,
            "id": media_id,
            "caption": text # getting replaced with message text
          },
          "message": {
            "text": text
          },
          "buttons": button_list
        })
        response = requests.request("POST", self.base_url+"send/interactive/buttons", headers=self.headers, data=payload)
        return response.text