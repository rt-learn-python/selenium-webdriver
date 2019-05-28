#!/usr/bin/env python3.6


# Expects you to set environment variables: `JIRA_USERNAME`, `JIRA_PASSWORD`

import os
from selenium import webdriver

import config
import login_jira

# Globals
driver = None
ticket_id = None


def main():
    '''
    This function receives user input and prints the Description and
    calculates the feature branch.
    '''
    global ticket_id
    ticket_id = input('Enter ticket ID: (e.g. MT-100): ')
    if len(ticket_id) == 0:
        ticket_id = 'MT-777'

    start_selenium()
    driver.get('https://jira.amaysim.net/browse/{}'.format(ticket_id))

    enter_username()
    enter_password()
    submit_login()
    print_summary()


def start_selenium():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)


def enter_username():
    username = os.environ['JIRA_USERNAME']
    username_element = driver.find_element_by_id('login-form-username')
    username_element.clear()
    username_element.send_keys(username)


def enter_password():
    password = os.environ.get('JIRA_PASSWORD')
    password_element = driver.find_element_by_id('login-form-password')
    password_element.clear()
    password_element.send_keys(password)


def submit_login():
    submit_element = driver.find_element_by_id('login-form-submit')
    submit_element.click()


def print_summary():
    '''
    Print the description and the calculated branch.
    '''
    global ticket_id
    desc_element = driver.find_element_by_id('summary-val')
    print(translate_to_branch(ticket_id, desc_element.text))


def translate_to_branch(id, description):
    return 'feature/{}-{}'.format(
        id,
        description.replace(' - ', '-')
        .replace(' ', '-'))


main()


result = translate_to_branch(
    'MT-777', 'Make product config database-driven - Implementation')

print(result)
