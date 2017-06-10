from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def get_chrome_driver():
    return webdriver.Chrome("..\\content\\engine\\chromedriver.exe")


#The By is only a Class to save things like html_tags.
def wait_element_presence(driver,element_tag,element_name):
    try:
        # by_element_tag.upper()
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((element_tag, element_name))
        )
        print(element)
    finally:
        driver.quit()


def __init__():
    if __name__ == '__main__':
        driver=webdriver.Chrome("..\\content\\engine\\chromedriver.exe")
        print('main program')
    else:
        print('invoke successfully')


