import requests
from endpoints import AUTH


async def create_auth_token(base_url, headers, payload):
    url = f"{base_url}{AUTH}"
    headers = headers
    payload = payload
    try:
        response = requests.post(url, headers=headers, json=payload)
        return response
    except requests.RequestException as e:
        print(f"Error creating auth token: {e}")
        return None
