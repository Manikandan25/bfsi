from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import csv
from datetime import datetime
from dateutil.tz import gettz
import requests
# Create your views here.

def write_json_data(data):
    with open("list_of_request.json",'r+') as file:
        file_data = json.load(file)
        new_data = {"message":2}
        file_data.append(data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)



@csrf_exempt
def chats(request):
    request_data = json.loads(request.body)
    print(request_data)
    write_json_data(request_data)
#    response = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message":request_data["messages"][0]["text"]["body"]})
#    data =json.loads(response.text)[0]
    # send_message()
    return JsonResponse(request_data)
    
@csrf_exempt    
def home(request):
    data = {
    "contacts": [{
        "profile": {
        "name": "Manikandan"
        },
        "wa_id": "Hackathon_8904585717"
    }],
    "messages":[{
        "from": "918015427671",
        "id": "11111111111",
        "timestamp": datetime.utcnow().strftime('%a %d %b %Y %H:%M:%S')+(" GMT"),
        "text": {
#        "body": json.loads(request.body)['message']
        "body":"new"
        },
        "type": "text"
    }]
    }
    headers = {
    'Content-Type': 'application/json'
    }
#    response = requests.request("POST", "https://127.0.0.1:8000/webhook", headers=headers, data=json.dumps(data), verify=False)
#    return JsonResponse(json.loads(response.text))
    return render(request,"chatview.html")
