import config

driver = None


def init(web_driver):
    global driver
    driver = web_driver


def login():
    enter_username()
    enter_password()
    submit_login()


def enter_username():
    username = config.username
    username_element = driver.find_element_by_id('login-form-username')
    username_element.clear()
    username_element.send_keys(username)


def enter_password():
    password = config.password
    password_element = driver.find_element_by_id('login-form-password')
    password_element.clear()
    password_element.send_keys(password)


def submit_login():
    submit_element = driver.find_element_by_id('login-form-submit')
    submit_element.click()
