#!/usr/bin/env python3.6


# Expects you to set manually environment variables: `JIRA_PASSWORD`

import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import config
import login_jira

# Globals
driver = None
ticket_id = None
logger = None


def init():
    global logger
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')

    # add formatter to ch
    ch.setFormatter(formatter)
    logger.addHandler(ch)


def main():
    '''
    This function receives user input and prints the Description and
    calculates the feature branch.
    '''
    global ticket_id
    ticket_id = input('Enter ticket ID: (e.g. MT-100): ')
    if len(ticket_id) == 0:
        ticket_id = 'MT-834'

    start_selenium()
    driver.get('https://jira.amaysim.net/browse/{}'.format(ticket_id))
    logger.info('Page loaded.')
    login_jira.init(driver)
    login_jira.login()
    logger.info('Logged in to jira')
    print_summary()


def start_selenium():
    global driver

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = config.chrome_bin

    driver = webdriver.Chrome(
        executable_path=config.chrome_driver_bin,
        chrome_options=chrome_options)

    driver.implicitly_wait(10)
    logger.info('Selenium started')


def print_summary():
    '''
    Print the description and the calculated branch.
    '''
    global ticket_id
    desc_element = driver.find_element_by_id('summary-val')
    print(translate_to_branch(ticket_id, desc_element.text))
    print('{}: {}'.format(ticket_id, desc_element.text))


def translate_to_branch(id, description):
    return 'feature/{}-{}'.format(
        id,
        description.replace(' - ', '-')
        .replace(' ', '-')
        .replace("'", ''))


init()
main()
