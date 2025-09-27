import requests
from endpoints import BOOKING
from steps_definition.log_utility import log

async def delete_booking(address, headers, booking_id):
    url = f"{address}{BOOKING}/{booking_id}"
    try:
        response = requests.delete(url, headers=headers)
    except Exception as e:
        log.critical(f"Error deleting booking: {e}")
        raise e
    return response
