import asyncio
from behave import *
from behave.api.async_step import async_run_until_complete
from steps_definition.update_booking_request import update_booking
from steps_definition.update_patch_booking_request import update_partial_booking
from utility import table_to_object, load_response
from steps_definition.log_utility import log


@step('I update a booking with the following details')
@async_run_until_complete
async def update_booking_step(context):
    my_table = table_to_object(context)
    headers = my_table["headers"]
    body = my_table["body"]
    booking_id = my_table["booking_id"]
    response = None
    try:
        response = await asyncio.wait_for(update_booking(context.address, headers, body, booking_id), timeout=5)
    except TimeoutError as e:
        log.critical(e)
    context.my_context.add(my_table["response_to_be_stored"], response)



@step('I update partial booking with the following details')
@async_run_until_complete
async def update_booking_step(context):
    my_table = table_to_object(context)
    headers = my_table["headers"]
    body = my_table["body"]
    booking_id = my_table["booking_id"]
    response = None
    try:
        response = await asyncio.wait_for(update_partial_booking(context.address, headers, body, booking_id), timeout=5)
    except TimeoutError as e:
        log.critical(e)
    context.my_context.add(my_table["response_to_be_stored"], response)