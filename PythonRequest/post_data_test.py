import requests

host = "https://httpbin.org/"
endpoint = "post"
url = "".join([host, endpoint])

# 有参数请求
params = {"show_env": 1}
data = {"a": "张三", "b": "test"}
r = requests.post(url=url,data=data,params=params)

print(r.headers)
print(r.text)

resp = r.json()
print(resp["form"]["a"])
