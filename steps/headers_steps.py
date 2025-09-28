import asyncio
from behave import step
from behave.api.async_step import async_run_until_complete
from header import Header
from steps_definition.auth import create_auth_token
import json


@step("I have created username_password header '(.*)'")
def get_me_universal_header(context, header_context):
    # Create user headers
    hd = Header(
        "admin",
        "password123",
        "application/json",
        "application/json"
    )
    header = hd.create_header()
    context.my_context.add(header_context, header)


@step("I have created token header '(.*)'")
@async_run_until_complete
async def get_me_token_header(context, header_context):
    # Create user headers
    hd = Header(
        "None",
        "None",
        "application/json",
        "application/json"
    )
    body = """{
        "username": "admin",
        "password": "password123"
    }"""
    payload = json.loads(body)
    headers = hd.create_header()
    response = None
    try:
        response = await asyncio.wait_for(create_auth_token(context.address, headers, payload), timeout=2.0)
    except asyncio.TimeoutError:
        print("Timeout on creating auth token")
    token = response.json().get("token")
    header_1 = hd.create_header()
    header_1["Cookie"] = f"token={token}"
    context.my_context.add(header_context, header_1)
