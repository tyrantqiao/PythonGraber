from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

from tools.exception import NotAccurateUrl, ElementNotFound


def get_phantomjs_driver():
    return webdriver.PhantomJS("..\\content\\engine\\phantomjs.exe")


# cannot use devTools when you use the driver. This action will crash the driver.
def get_chrome_driver():
    return webdriver.Chrome("..\\content\\engine\\chromedriver.exe")


def driver_wait_seconds(driver, wait_seconds=5):
    driver.implicitly_wait(wait_seconds)


# The By is only a Class to save things like html_tags.
# non-default-parameter follows default-parameter
def wait_element_presence(driver, wait_seconds, element_tag, element_name):
    try:
        WebDriverWait(driver, wait_seconds).until(
            EC.presence_of_element_located((element_tag, element_name))
        )
        print("I find the element " + element_name)
    except:
        print("too long to find the element " + element_name)


def assert_page_load(driver, page_url):
    actual_url = driver.current_url
    if page_url in actual_url:
        print('yes it is the page you want')
        return True
    else:
        raise NotAccurateUrl


def login_directly(driver, account_tag, account_tag_name, passwd_tag, passwd_tag_name, wait_seconds=10):
    wait_element_presence(driver, wait_seconds, account_tag, account_tag_name)

    element_account = driver.find_element(account_tag, account_tag_name)
    element_password = driver.find_element(passwd_tag, passwd_tag_name)
    element_account.send_keys(input("input your account\n"))
    element_password.send_keys(input("input your password\n"))
    element_password.send_keys(Keys.RETURN)
    return driver


def search_content(driver, search_tag, search_name, search_content):
    try:
        wait_element_presence(driver, '5', search_tag, search_name)
        search_element = driver.find_element(search_tag, search_name)
        search_element.send_keys(search_content)
        search_element.send_keys(Keys.RETURN)
    except:
        raise ElementNotFound


def __init__():
    if __name__ == '__main__':
        driver = webdriver.Chrome("..\\content\\engine\\chromedriver.exe")
        print('main program')
    else:
        print('invoke successfully')
