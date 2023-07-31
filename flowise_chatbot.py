"""_summary_
This is a flowise prototype using a local server instance. It will not work
when cloned via github

Flowise is a no-code langchain tool that is useful for prototyping langchain
projects. The example below is using a chatbot trained on the Automattic 
fieldguide, an employee manual for Automattic employees.
"""
import requests

API_URL = "http://localhost:3000/api/v1/prediction/e9b5a208-4932-4170-8667-ea90b89fc8e1"

def query(payload):
    response = requests.post(API_URL, json=payload)
    print(response.json())
    return response.json()
    
output = query({
    "question": "Can you list what travel upgrades I can and can't use?",
})