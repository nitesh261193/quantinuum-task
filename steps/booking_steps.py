import asyncio
from behave import *
from behave.api.async_step import async_run_until_complete
from steps_definition.create_booking_request import create_booking
from utility import table_to_object, load_response
from steps_definition.log_utility import log


@step('I create a booking with the following details')
@async_run_until_complete
async def create_new_booking(context):
    my_table = table_to_object(context)
    headers = my_table["headers"]
    body = my_table["body"]
    response = None
    try:
        response = await asyncio.wait_for(create_booking(context.address, headers, body), timeout=5)
    except TimeoutError as e:
        log.critical(e)
    context.my_context.add(my_table["response_to_be_stored"], response)
    r = load_response(response)
    if r is not None:
        context.my_context.add(my_table["booking_id_stored_as"], r["bookingid"])
    else:
        log.error("No booking ID found in response")
