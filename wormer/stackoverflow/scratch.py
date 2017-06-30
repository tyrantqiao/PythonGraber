from http import cookiejar

import requests
import re

session = requests.session()

# s_obj = session.get('http://stackoverflow.com')
# print(s_obj.content.decode('utf-8'))
# with open('stack_index.txt', 'wb')as stack_file:
#     stack_file.write(s_obj.content)
#     print('done')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Host': 'stackoverflow.com:443'
}


def login():
    session.cookies = cookiejar.LWPCookieJar(filename='cookies.txt')
    try:
        print(session.cookies)
        print('you have the cookies')
    except:
        print('no cookies, need login first')

    s = session.get('http://stackoverflow.com/users/login')
    post_form = make_form(s.text)
    print(post_form)
    response=session.post('http://stackoverflow.com/users/login', data=post_form, headers=headers)

    print(response.content)
    print(response.cookies)
    cookiejar.LWPCookieJar.save(filename='cookies.txt')


def find_fkey(content):
    fkey = re.search('input type="hidden" name="fkey" value="([a-z0-9]*)"', content)
    return fkey.group(1)


def make_form(content):
    form = {}
    form.update({'fkey': find_fkey(content)})
    form.update({'ssrc': 'head'})
    while True:
        param = input('param: bye to leave\n')
        if param == 'bye':
            break
        value = input('value\n')
        form[param]=value
        #or form._setitem_(xx,xx)
    return form

login()
