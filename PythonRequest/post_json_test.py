import requests

host = "https://httpbin.org/"
endpoint = "post"
url = "".join([host, endpoint])

data = {
    "info": {"code": 1, "sex": "男", "id": "1000", "name": "测试"},
    "code": 1,
    "name": "测试", "sex": "女",
    "data": [{"code": 1, "sex": "男", "id": "1000", "name": "测试"}, {"code": 1, "sex": "女", "id": "1000", "name": "测试"}],
    "id": 1000
}

# r = requests.post(url=url, data=data)#data的值无法显示
# r = requests.post(url=url, data=json .dumps(data))#序列化
r = requests.post(url=url, json=data)

print(r.headers)
print(r.text)

# resp = r.json()
