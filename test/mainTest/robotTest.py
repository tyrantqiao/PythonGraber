import requests

response=requests.get('http://dytt8.net/html/tv/oumeitv/20170922/55087.html')
print(response.content)