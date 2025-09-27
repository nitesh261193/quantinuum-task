import asyncio
import requests
from behave import *
from behave.api.async_step import async_run_until_complete
from steps_definition.health_check import check_service_health
from header import Header
from utility import get_formatting_string_value, get_response_object_from_formatted_string, match_single_json_obj, \
    is_specific_type
import time
from steps_definition.log_utility import log



@step("The system is ready to interact with user")
@async_run_until_complete
async def fetch_health_status(context):
    hd = Header(username="admin", password="password123",
                accept="application/json", content_type="application/json")
    headers = hd.create_header()
    response = None
    try:
        response = await asyncio.wait_for(check_service_health(context.address, headers), timeout=2.0)
    except requests.RequestException as e:
        log.critical(f"Error fetching health status: {e}")

    assert response.status_code == 201, f"Health check failed,{response.text}"


@then("I see status code '(.*)' in '(.*)'")
def step_impl(context, expected_status_code, working_context):
    response_file = get_formatting_string_value(context, working_context)
    assert str(response_file.status_code) == expected_status_code, (
        f"Assertion error for a status code {str(response_file.status_code)},"
        f"The actual response is {response_file.text}"
    )


@step("the json path in '(.*)' has specific value in the object")
def step_impl(context, response):
    for row in context.table:
        data = get_response_object_from_formatted_string(context, response)
        expected_value = get_formatting_string_value(context, row[1])
        if isinstance(expected_value, str):
            if "!" in expected_value:
                expected_value = expected_value.replace("!", "|")
        pre_processed_value = get_formatting_string_value(context, row[0])
        my_value = match_single_json_obj(pre_processed_value, data)
        expected_value = is_specific_type(expected_value, my_value)
        if isinstance(my_value, str):
            my_value = my_value.replace("\r\n", "").lower()
            expected_value = str(expected_value).lower()
        assert my_value == expected_value, (
            f"Assertion failed. "
            f"Reason: {my_value} != {expected_value} {row[0]} != {row[1]}"
        )

@step("Test waits '(.*)' seconds")
def step_impl(context, seconds):
    time.sleep(int(seconds))
