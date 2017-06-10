from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


def get_chrome_driver():
    return webdriver.Chrome("..\\content\\engine\\chromedriver.exe")


# The By is only a Class to save things like html_tags.
def wait_element_presence(driver, wait_seconds, element_tag, element_name):
    try:
        WebDriverWait(driver, wait_seconds).until(
            EC.presence_of_element_located((element_tag, element_name))
        )
        print("I find the element " + element_name)
    except:
        print("too long to find the element "+element_name)


def __init__():
    if __name__ == '__main__':
        driver = webdriver.Chrome("..\\content\\engine\\chromedriver.exe")
        print('main program')
    else:
        print('invoke successfully')
