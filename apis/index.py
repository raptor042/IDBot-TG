import requests
import logging

async def create_did_IDBot(data):
    print(data)
    try:
        response = requests.post(f"http://localhost:8000/create", json=data)
    except:
        logging.error("Unable to send request to API gateway")
    else:
        return response.json()