import socket
from behave import use_step_matcher
from steps_definition.log_utility import log
from utility import get_base_url

use_step_matcher("re")


def load_config(context):
    # Creating initial configuration context
    log.info("=======================================================")
    log.info(
        f"Test execution is using configuration file for environment"
    )
    log.info("=======================================================")
    context.address = get_base_url()
    log.info(f"Config Url: {context.address}")



