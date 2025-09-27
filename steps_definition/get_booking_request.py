import requests
from endpoints import BOOKING
from steps_definition.log_utility import log

async def get_booking(address, headers, booking_id):
    url = f"{address}{BOOKING}/{booking_id}"
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        log.critical(f"Error getting booking: {e}")
        raise e
    return response


async def get_booking_ids(address, headers):
    url = f"{address}{BOOKING}"
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        log.critical(f"Error getting booking: {e}")
        raise e
    return response
