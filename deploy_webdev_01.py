#!/usr/bin/env python3

# 1. Reading environment variables.
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


# Globals
driver = None
delete_at_night = None


def main():
    start_selenium()
    driver.get('https://automation.amaysim.net/')

    username = os.environ['USERNAME']
    type_username(username)

    password = os.environ.get('PASSWORD')
    type_password_and_enter(password)

    click_run_button()
    keep_stack()

    select_dev_abb()
    select_dev_idp()
    select_ec()
    select_env01()
    select_payment()
    activate_express_delivery()
    activate_shark()

    start_build_job()


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
    run_element = driver.find_element_by_xpath(
        '//*[@id="bt319-div"]/table/tbody/tr/td[2]/span/button[1]')
    run_element.click()


def keep_stack():
    delete_element = driver.find_element_by_id(
        'parameter__STACK_ADD_TO_DELETE')

    if delete_element.is_selected:
        delete_element.click()


def select_dev_abb():
    select = Select(driver.find_element_by_id('parameter_ABB_API_URL'))
    select.select_by_index(0)


def select_dev_idp():
    select = Select(
        driver.find_element_by_id('parameter_AMAYSIM_IDP_ENVIRONMENT'))
    select.select_by_index(0)


def select_ec():
    select = Select(
        driver.find_element_by_id('parameter_EC_WSDL'))
    select.select_by_value('ecapi-staging3.amaysim.net')


def select_env01():
    select = Select(driver.find_element_by_id('parameter_ENVIRONMENT_NUMBER'))
    select.select_by_value('01')


def select_payment():
    select = Select(driver.find_element_by_id('parameter_PAYMENTS_HOST'))
    select.select_by_value('payments-qa.amaysim.net')


def activate_express_delivery():
    select = Select(driver.find_element_by_id(
        'parameter_TOGGLE_FUNNEL_EXPRESS_DELIVERY'))
    select.select_by_value('active')


def activate_shark():
    select = Select(driver.find_element_by_id(
        'parameter_TOGGLE_FUNNEL_PROJECT_SHARK'))
    select.select_by_value('active')


def start_build_job():
    run_build_element = driver.find_element_by_id('runCustomBuildButton')
    run_build_element.click()


main()
