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
    confirm_deletion()

    start_selenium()
    driver.get('https://automation.amaysim.net/')

    username = os.environ['USERNAME']
    type_username(username)

    password = os.environ.get('PASSWORD')
    type_password_and_enter(password)

    click_run_button()
    select_env01()

    start_build_job()


def confirm_deletion():
    answer = input('Are you sure you want to delete webdev 01 [yN]? ')
    if answer.lower() != 'y':
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


# def expand_ma():

#     is_displayed()
#     if not visible:
#         ma_toggle_element = driver.find_element_by_xpath(
#             //*[@id="blockHandleovr_project30"])
#         ma_toggle_element.click()


def click_run_button():
    run_element = driver.find_element_by_xpath(
        '//*[@id="bt323-div"]/table/tbody/tr/td[2]/span/button[1]')
    run_element.click()


def select_env01():
    select = Select(driver.find_element_by_id('parameter_ENVIRONMENT_NUMBER'))
    select.select_by_value('01')


def start_build_job():
    run_build_element = driver.find_element_by_id('runCustomBuildButton')
    run_build_element.click()


main()
