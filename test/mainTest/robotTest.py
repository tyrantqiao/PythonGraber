import requests

s = requests.session()
login_data = {'email': '51307521@qq.com', 'password': 'Tyrant', }

# post 数据实现登录
s.post('https://www.zhihu.com/#signin', login_data)

# 验证是否登陆成功，抓取'知乎'首页看看内容
r = s.get('http://www.zhihu.com')
print(r.content.decode('utf-8'))