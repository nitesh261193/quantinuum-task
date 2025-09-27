import requests
from endpoints import BOOKING
from steps_definition.log_utility import log

async def create_booking(address, headers, booking_data):
    url = f"{address}{BOOKING}"
    headers = headers
    body = booking_data
    try:
        response = requests.post(url, headers=headers, json=body)
    except Exception as e:
        log.critical(f"Error creating booking: {e}")
        raise e
    return response