from tools.driver import wait_element_presence
from tools.driver import get_chrome_driver
from selenium.webdriver.common.keys import Keys

from tools.filetool import write_text

driver = get_chrome_driver()
driver.get("http://" + input("http://+url\n"))

wait_element_presence(driver, 10, 'id', 'loginname')

element_account = driver.find_element_by_id("loginname")
element_password = driver.find_element_by_name("password")
element_account.send_keys(input("input your account\n"))
element_password.send_keys(input("input your password\n"))
element_password.send_keys(Keys.RETURN)
try:
    wait_element_presence(driver, 5, 'title', 'tyrantQiao')
    #cannot use devTools when you use the driver. This action will crash the driver.
    write_text(driver.page_source, 'weiboIndex')
except:
    print('cannot write text,something wrong')
finally:
    driver.quit()
