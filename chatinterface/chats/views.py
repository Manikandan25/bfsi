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

@csrf_exempt
def chats(request):
    request_data = json.loads(request.body)
    response = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message":request_data["messages"][0]["text"]["body"]})
    data =json.loads(response.text)[0]
    # send_message()
    return JsonResponse(data)
    
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
        "body": json.loads(request.body)['message']
        },
        "type": "text"
    }]
    }
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", "https://127.0.0.1:8000/webhook", headers=headers, data=json.dumps(data), verify=False)
    return JsonResponse(json.loads(response.text))