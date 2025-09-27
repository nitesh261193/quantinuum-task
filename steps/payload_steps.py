from behave import *
import json


@step("The payload stored as '(.*)'")
def step_impl(context, context_name):
    # This step takes a json blob in comments and converts it
    # For example
    """
    {
      "Route": "/asset/a64ae734-b6ca-4e9c-9859-01cf7e73b637",
      "Type": "Asset"
    }
    """
    # This replaces the more endpoint specific steps we have
    # It's an alternative to the step that takes the parameters in a table
    body = json.loads(context.text)
    context.my_context.add(context_name, body)