import requests
import json

def send_message_to_chatbot(message, api_key):
    url = "https://search0-t4eqhr5zv6b54.search.windows.net/indexes/ragindex/docs/search?api-version=2021-04-30-Preview"

    headers = {
        'Content-Type': 'application/json',
        'api-key': api_key
    }

    payload = {
        "search": message,
        "top": 5
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}
