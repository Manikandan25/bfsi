from enhancements.mani.user_initiated_messages import Send
import requests
import json
from datetime import datetime

session_id = "999784hhgyug"
receiver = "918015427671"
send = Send()
text = "Good Morning"
response = send.text(receiver, session_id, text)
print(json.loads(response))