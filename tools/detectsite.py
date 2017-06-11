import re
import urllib3
import requests
import builtwith

def read_robots_text(url):
    robot_url = 'http://' + url + '/robots.txt'
    session = requests.get(robot_url)
    content = session.content
    print(content)


def test_robots_with_agent(user_agent, url):
    #detect whether which kind of agent can use.
    pass
