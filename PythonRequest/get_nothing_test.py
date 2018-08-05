import requests

host = "https://httpbin.org/"
endpoint = "get"
url = "".join([host, endpoint])
# print(url)

r = requests.get(url)
print(r.url)#获取url
print(r.status_code,r.reason)#获取状态码
print(r.headers)
print(r.content)