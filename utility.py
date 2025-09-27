import json
import os
import re
from steps_definition.log_utility import log
import jsonpath_rw_ext as jp
import datetime

def get_base_url():
    """Get base URL from config.json"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    package_json_path = os.path.join(current_dir, 'config.json')

    with open(package_json_path, 'r') as f:
        config = json.load(f)
    return config.get('BASE_URL')



def table_to_object(context):
    my_table = {}
    for row in context.table:
        field = row[0]
        value = row[1]

        if is_json_object(value):
            value = json.loads(value)

        value = get_formatting_string_value(context, value)

        my_table.update({field: value})
    return my_table


def is_json_object(data):
    return data[:1] == "{" and data[-1:] == "}"


def is_formatting_string(data):
    return re.match("#{([^}]+)}", data)


def get_formatting_string(data):
    formatting_strings = re.search("#{([^}]+)}", data)
    return formatting_strings.group(1)



def get_formatting_string_value(context, data):
    if is_formatting_string(data):
        formatting_string = get_formatting_string(data)
        return context.my_context.get(formatting_string)
    return data

def load_response(data_source):
    data = data_source.text
    return json.loads(data)

def get_response_object_from_formatted_string(context, data):
    if is_formatting_string(data):
        formatting_string = get_formatting_string(data)
        value = context.my_context.get(formatting_string)
        return load_response(value)
    return data

def match_single_json_obj(path, data):
    try:
        log.info(f"JSONPath failed in match_single_json_obj: {path}")
        result = jp.match(path, data)
    except Exception as e:
        log.critical(f"JSONPath {path} failed in match_single_json_obj: {e}")
        raise e
    return result[0]

def is_specific_type(value, my_value=None):
    if isinstance(my_value, str):
        return value
    elif isinstance(value, int):
        return value
    elif isinstance(value, datetime.datetime):
        return str(value)
    elif isinstance(value, str) and value.isnumeric():
        return int(value)
    elif isinstance(value, str) and value.replace(".", "", 1).isdecimal():
        return float(value)
    elif isinstance(value, str) and "[]" in value and not "@" in value:
        return list(value.replace("[", "").replace("]", ""))
    elif value == "True":
        return True
    elif value == "False":
        return False
    elif value == "None":
        return None
    else:
        return value

