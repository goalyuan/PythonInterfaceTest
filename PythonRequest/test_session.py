import requests

host = "https://httpbin.org/"
endpoint = "cookies/set/sessioncookie/123456789"
url = "".join([host, endpoint])

url1 = "https://httpbin.org/cookies"
r = requests.get(url=url1)
print(r.text)

session = requests.Session()#创建一个Session对象
session.get(url)#将cookie信息存储在session中
r1 = session.get(url1)#通过会话访问cookie
print(r1.text)

