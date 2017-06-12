import re
import requests
from collections import deque

from tools.database import get_mysql_db
from tools.graber import grab_posts

queue = deque()
visited = set()

url = 'http://news.dbanotes.net'  # 入口页面, 可以换成别的
queue.append(url)
cnt = 0

db = get_mysql_db('root', '1YTINTERNshipQsql', 'posts')
cursor = db.cursor()
while queue:
    url = queue.popleft()  # 队首元素出队
    visited = {url}  # 标记为已访问

    print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
    cnt += 1

    response = requests.get(url)
    # print(response.headers)
    # 避免程序异常中止, 用try..catch处理异常
    try:
        data = response.content.decode('utf-8')
        print(data)
    except:
        print('error, cannot read the horrible things')
        continue

    posts_sql = grab_posts(data)
    cursor.execute(posts_sql)
    db.close()

    # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
    linkre = re.compile('href="(.+?)"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列 --->  ' + x)
