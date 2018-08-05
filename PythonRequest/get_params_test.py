import requests

host = "https://httpbin.org/"
endpoint = "get"
url = "".join([host, endpoint])

# 有参数请求
params = {"show_env": 1}
r = requests.get(url, params=params)

print(r.status_code, r.reason)
print(r.headers)
print(r.text)
