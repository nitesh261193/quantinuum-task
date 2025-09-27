import requests
from endpoints import BOOKING
from steps_definition.log_utility import log


async def update_partial_booking(address, headers, payload, booking_id):
    url = f"{address}{BOOKING}/{booking_id}"
    headers = headers
    body = payload
    try:
        response = requests.patch(url, headers=headers, json=body)
    except Exception as e:
        log.critical(f"Error updating booking: {e}")
        raise e
    return response
