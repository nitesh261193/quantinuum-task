import asyncio
import requests
from behave import *
from behave.api.async_step import async_run_until_complete
from step_definition.health_check import check_service_health
from header import Header


@step("the application health status is checked")
@async_run_until_complete
async def fetch_health_status(context):
    hd = Header(
        context.authorization,
        "application/json",
        "application/json",
        context.loc,
        "full",
    )
    headers = hd.create_header()
    response = None
    try:
        response = await asyncio.wait_for(check_service_health(context.address, headers), timeout=2.0)
    except requests.RequestException as e:
        print(f"Error fetching health status: {e}")

    assert response is not None
    context.health_response = response
    assert context.health_response.status_code == 200, f"Expected status code 200, got {context.health_response.status_code}"
    print(f"Health check response: {context.health_response}")

