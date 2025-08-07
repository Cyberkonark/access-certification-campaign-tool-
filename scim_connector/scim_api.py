import requests

SCIM_BASE = "https://your-idp.example.com/scim/v2"
TOKEN = "Bearer your_scim_token"

def get_users():
    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/scim+json"
    }
    response = requests.get(f"{SCIM_BASE}/Users", headers=headers)
    return response.json()
