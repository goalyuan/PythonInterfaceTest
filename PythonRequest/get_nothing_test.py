import requests

host = "https://httpbin.org/"
endpoint = "get"
url = "".join([host, endpoint])
# print(url)

r = requests.get(url)
# print(r.url)#获取url
# print(r.status_code,r.reason)#获取状态码，原因
# print(r.headers)#响应头
# print(r.text)#请求体，文本形式
# print(r.content)#请求体，二进制

# print(r.request.headers)
# print(r.request.url)
# print(r.request.method)
response = r.json()
print(type(response))
print(response["headers"]["Connection"])
print(eval(r.text)["headers"]["Connection"])