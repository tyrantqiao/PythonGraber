import re
from tools.driver import wait_element_presence, assert_page_load
from tools.driver import get_chrome_driver
from selenium.webdriver.common.keys import Keys
from tools.exception import ElementNotFound
from tools.filetool import write_text
import requests
# driver = get_chrome_driver()
# driver.get("http://" + input("http://+++\n"))

response=requests.get('http://zhihu.com')
print(response.content)



