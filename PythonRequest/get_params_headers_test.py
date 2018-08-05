import requests

host = "https://httpbin.org/"
endpoint = "get"
url = "".join([host, endpoint])

# 有参数请求
params = {"show_env": 1}
headers = {"User-Agent":"python-requests/2.18.4","Connection":"keep-alive","Accept-Encoding":"gzip, deflate","Accept":"*/*"}
r = requests.get(url, params=params, headers=headers)

print(r.status_code, r.reason)
print(r.headers)
print(r.text)
print(r.request.headers)
