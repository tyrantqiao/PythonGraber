import re
import requests
from http.cookiejar import LoadError
from http import cookiejar
import time

headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87'
}

session = requests.session()
session.cookies = cookiejar.LWPCookieJar(filename='..\\content\\text\\cookies.txt')
try:
    print(session.cookies)
    session.cookies.load(ignore_discard=True)
except:
    print("还没有cookie信息")


def get_xsrf():
    response = session.get('http://www.zhihu.com')
    html_text = response.content.decode('utf-8')
    xsrf = re.search('<input type=\"hidden\" name=\"_xsrf\" value=\"([\d\a]*)\">', html_text)
    print(xsrf)
    return xsrf


def get_captcha():
    """
    把验证码图片保存到当前目录，手动识别验证码
    :return:
    """
    t = str(int(time.time() * 1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
    captcha = input("验证码：")
    return captcha


def login(email, password):
    login_url = 'https://www.zhihu.com/login/email'
    # https://www.zhihu.com/#signin
    data = {
        'email': email,
        'password': password,
        '_xsrf': get_xsrf(),
        # # "captcha": 'cn'
        "captcha": get_captcha(),
        'remember_me': 'true'
    }
    response = session.post(login_url, data=data, headers=headers)
    login_code = response.json()
    print(login_code['msg'])
    for i in session.cookies:
        print('session'+str(i))
    session.cookies.save('..\\content\\text\\cookies.txt')



login('51307521@qq.com', 'Tyrant')
session.cookies = cookiejar.LWPCookieJar(filename='..\\content\\text\\cookies.txt')
session_obj=session.get('http://www.zhihu.com')
content=session_obj.content
print(content.decode('utf-8'))