import requests
from requests.exceptions import RequestException
from endpoints import HEALTH_CHECK


async def check_service_health(address, headers):
    url = f'{address}{HEALTH_CHECK}'
    headers = headers
    response = None
    try:
        response = requests.get(url, headers)
    except RequestException as e:
        print(f"Error checking service health: {e}")
    return response
