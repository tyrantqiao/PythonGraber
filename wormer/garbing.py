
from tools.driver import get_chrome_driver


try:
    driver=get_chrome_driver()
    driver.get("http://"+input("http://+url"))

except:
    print("no such driver")


