import asyncio
from behave import *
from behave.api.async_step import async_run_until_complete
from steps_definition.get_booking_request import get_booking, get_booking_ids
from utility import table_to_object
from steps_definition.log_utility import log

@step('I send GET request for booking')
@async_run_until_complete
async def get_booking_details(context):
    my_table = table_to_object(context)
    headers = my_table["headers"]
    booking_id = my_table["booking_id"]
    response = None
    try:
        response = await asyncio.wait_for(get_booking(context.address, headers, booking_id), timeout=5)
    except TimeoutError as e:
        log.critical(e)
    context.my_context.add(my_table["response_to_be_stored"], response)

@step('I send GET request for all booking ids')
@async_run_until_complete
async def get_booking_details(context):
    my_table = table_to_object(context)
    headers = my_table["headers"]
    response = None
    try:
        response = await asyncio.wait_for(get_booking_ids(context.address, headers), timeout=5)
    except TimeoutError as e:
        log.critical(e)
    context.my_context.add(my_table["response_to_be_stored"], response)