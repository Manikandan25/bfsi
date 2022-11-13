from enhancements.mani.user_initiated_messages import Send
import requests
import json
from datetime import datetime

#sending text
session_id = "999784hhgyug"
receiver = "918015427671"
send = Send()
text = "Good Morning"
response = send.text(receiver, session_id, text)
print(json.loads(response))

# sending interactive list
options_list = {"heading": "Accounts",
"options": [
  {
    "tag": "savings_account",
    "title": "Savings Account",
    "description": "view options in saving account tab"
  },
  {
    "tag": "current_account",
    "title": "Current Account",
    "description": "view options in current account tab"
  }
]
}
text = "Account Menu"
response = send.interactive_list(receiver, session_id, text, options_list)
print(json.loads(response))

# upload media
media_type = "IMAGE" # VIDEO
media_name = '247137.png'
media = open(r"image.png",'rb') # some file
media_format = 'image/png' # video/mp4
response = send.upload_media(media_type, media_name, media, media_format)
print(response)

#send media
#response = {"mediaId":"837036577567453"}
#send media
media_id = response['mediaId']
media_type = "IMAGE"
text = "Spidey Signature"
response = send.media(receiver, session_id, media_type, media_id, text)
print(response)

# send interactive buttons
button_list = [
    {
      "tag": "interested",
      "title": "Interested"
    },
    {
      "tag": "not_interested",
      "title": "Not interested"
    }
  ]
text = "Spiderman movie released"
response = send.interactive_buttons(receiver, session_id, media_type, media_id, text, button_list)
response