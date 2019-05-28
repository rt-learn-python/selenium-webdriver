import os

from dotenv import load_dotenv

load_dotenv()

username = os.getenv('JIRA_USERNAME')
password = os.getenv('JIRA_PASSWORD')

if not password:
    print('Jira password was not found in the environment variables.')

chrome_driver_bin = os.getenv('CHROME_DRIVER_BIN')
chrome_bin = os.getenv('CHROME_BIN')
