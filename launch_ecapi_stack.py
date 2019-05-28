#!/usr/bin/env python3

# 1. Reading environment variables.
import os
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Globals
driver = None
delete_at_night = None


def main():
    confirm_current_project()

    global delete_at_night
    delete_at_night = input('Delete stack at night [Yn]? ): ')

    start_selenium()
    driver.get('https://automation.amaysim.net/')

    username = os.environ['USERNAME']
    type_username(username)

    password = os.environ.get('PASSWORD')
    type_password_and_enter(password)

    click_run_button()
    set_code_base()
    configure_keep_stack()
    selectR4Large()
    toggle_shark_on()
    start_build_job()


def confirm_current_project():
    current_ticket = os.environ.get('CURRENT_TICKET_ID')
    answer = input('Current Ticket: {}, proceed [Yn]? '.format(current_ticket))
    if answer.lower() == 'n':
        print('Aborted.')
        quit()


def start_selenium():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)


def type_username(username):
    username_element = driver.find_element_by_name('username')
    username_element.clear()
    username_element.send_keys(username)


def type_password_and_enter(password):
    password_element = driver.find_element_by_name('password')
    password_element.clear()
    password_element.send_keys(password)
    password_element.send_keys(Keys.RETURN)


def click_run_button():
    run_element = driver.find_elements_by_xpath(
        '//*[@id="bt543-div"]/table/tbody/tr/td[2]/span/button[1]')[0]
    run_element.click()


def set_code_base():
    version_element = driver.find_element_by_name('parameter_Codebase_Version')
    version_element.clear()
    app_version = calc_app_version()
    print('App Version: {}'.format(app_version))
    version_element.send_keys(app_version)


def start_build_job():
    run_build_element = driver.find_element_by_id('runCustomBuildButton')
    run_build_element.click()


def calc_app_version():
    project_path = os.environ.get('PROJECT_FOLDER')
    feature_id = os.environ.get('CURRENT_TICKET_ID')
    meta = json.load(open('{}/meta.json'.format(project_path)))

    return "{}-{}-SNAPSHOT".format(
        meta['version'],
        feature_id)


def selectR4Large():
    r4_large_option = driver.find_element_by_xpath(
        '//*[@id="parameter_Instance_Type"]/option[2]')
    r4_large_option.click()


def configure_keep_stack():
    '''Ask user to delete stack at night. Defaults Yes.'''
    if delete_at_night.lower() == 'n':
        delete_element = driver.find_element_by_id(
            'parameter__STACK_ADD_TO_DELETE')
        if delete_element.is_selected:
            delete_element.click()


def toggle_shark_on():
    shark_element = driver.find_element_by_xpath(
        '//*[@id="parameter_TOGGLE_SHARK"]/option[2]')
    shark_element.click()


main()
