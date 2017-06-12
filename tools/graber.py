import re

import requests

from tools.driver import get_chrome_driver, get_phantomjs_driver


def grab_posts(text):
    titles = re.findall('<title>(.*)</title>', text)
    comheads = re.findall("<span class=\"comhead\">\((.*)\)</span>", text)
    urls = re.findall("<td class=\"title\"><a target=\"_blank\" href=(.*) rel=", text)
    print(titles.__len__())
    insert_sql = "(`POST_TITLE`,`POST_URL`,`COMHEAD`)VALUES"
    for i in range(titles.__len__()):
        print(titles[i])
        insert_sql += '''('%s','%s','%s')''' % (titles.pop(i), urls.pop(i), comheads.pop(i))
        print(insert_sql)
    return insert_sql


def grab_cookies(url):
    driver.get(url)
    # TODO fileio's tools
    # with open('..\\content\\text\\session1.txt', 'wb')as file:
    #     file.write("\n".join(driver.get_cookies()))
    # driver.quit()
    return driver.get_cookies()


driver = get_phantomjs_driver()
driver.get('http://news.dbanotes.net/')
cookies = driver.get_cookies()
print(type(cookies))
print(str(cookies))
requests_cookies = re.search('\[({.*})\]', str(cookies)).group(1)
print(requests_cookies)
print(type(requests_cookies))
response = requests.get('http://news.dbanotes.net/', cookies=requests_cookies)
# print(cookies)
print(response.content.decode('utf-8'))
driver.quit()
# response = requests.get(url, cookies=cookies)
# print(response.content.decode('utf-8'))
