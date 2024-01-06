import logging

import requests

def getUser(number):
    try:
        response = requests.get(f"https://idbot-80bt.onrender.com/user/{number}")
    except:
        logging.error("Unable to send request to the API Gateway.")
    else:
        print(response.text)
        return response.text

def getIDBotNumber(address):
    try:
        response = requests.get(f"https://idbot-80bt.onrender.com/number/{address}")
    except:
        logging.error("Unable to send request to the API Gateway.")
    else:
        print(response.text)
        return response.text
    
def getName(profile):
    try:
        response = requests.get(f"https://idbot-80bt.onrender.com/name/{profile}")
    except:
        logging.error("Unable to send request to the API Gateway.")
    else:
        print(response.text)
        return response.text
    
def getDescription(profile):
    try:
        response = requests.get(f"https://idbot-80bt.onrender.com/description/{profile}")
    except:
        logging.error("Unable to send request to the API Gateway.")
    else:
        print(response.text)
        return response.text
    
def getEmail(profile):
    try:
        response = requests.get(f"https://idbot-80bt.onrender.com/email/{profile}")
    except:
        logging.error("Unable to send request to the API Gateway.")
    else:
        print(response.text)
        return response.text
    
def getAge(profile):
    try:
        response = requests.get(f"https://idbot-80bt.onrender.com/age/{profile}")
    except:
        logging.error("Unable to send request to the API Gateway.")
    else:
        print(response.text)
        return response.text
    
def getCountry(profile):
    try:
        response = requests.get(f"https://idbot-80bt.onrender.com/country/{profile}")
    except:
        logging.error("Unable to send request to the API Gateway.")
    else:
        print(response.text)
        return response.text
    
def getState(profile):
    try:
        response = requests.get(f"https://idbot-80bt.onrender.com/state/{profile}")
    except:
        logging.error("Unable to send request to the API Gateway.")
    else:
        print(response.text)
        return response.text
    
def getPhone(profile):
    try:
        response = requests.get(f"https://idbot-80bt.onrender.com/phone/{profile}")
    except:
        logging.error("Unable to send request to the API Gateway.")
    else:
        print(response.text)
        return response.text
    
def getAddress(profile):
    try:
        response = requests.get(f"https://idbot-80bt.onrender.com/address/{profile}")
    except:
        logging.error("Unable to send request to the API Gateway.")
    else:
        print(response.text)
        return response.text
    
def getProfilePic(profile):
    try:
        response = requests.get(f"https://idbot-80bt.onrender.com/profile_pic/{profile}")
    except:
        logging.error("Unable to send request to the API Gateway.")
    else:
        print(response.text)
        return response.text
    
def getScore(profile):
    try:
        response = requests.get(f"https://idbot-80bt.onrender.com/score/{profile}")
    except:
        logging.error("Unable to send request to the API Gateway.")
    else:
        print(response.text)
        return response.text
    
def getProjects(profile):
    try:
        response = requests.get(f"https://idbot-80bt.onrender.com/projects/{profile}")
    except:
        logging.error("Unable to send request to the API Gateway.")
    else:
        print(response.json())
        return response.json()