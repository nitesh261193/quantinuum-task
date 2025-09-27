# coding: utf-8
from behave import use_step_matcher
from user_configuration import load_config
from steps_definition.log_utility import log
from my_context import MyContext

use_step_matcher("re")


def before_all(context):
    log.info("=======================================================")
    log.info("Creating configuration context - in progress")
    log.info("=======================================================")
    load_config(context)

def before_scenario(context, scenario):
    context.my_context = MyContext()
