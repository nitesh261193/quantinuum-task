import asyncio
from behave import *
from steps_definition.delete_booking_request import delete_booking
from utility import table_to_object
from steps_definition.log_utility import log

@step('I send request to delete booking')
async def get_booking_details(context):
    my_table = table_to_object(context)
    headers = my_table["headers"]
    booking_id = my_table["booking_id"]
    response = None
    try:
        response = await asyncio.wait_for(delete_booking(context.address, headers, booking_id), timeout=5)
    except TimeoutError as e:
        log.critical(e)
    context.my_context.add(my_table["response_to_be_stored"], response)