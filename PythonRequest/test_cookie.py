import requests

host = "https://httpbin.org/"
endpoint = "cookies"
url = "".join([host, endpoint])

url1="https://www.baidu.com/"
r = requests.get(url=url1)
print(r.cookies)#获取cookie jar包

dic = requests.utils.dict_from_cookiejar(r.cookies)#jar包转换为字典
print(dic)


#发送cookie给服务器
cookies = {"cookie-name":"sanye"}
r1 = requests.get(url=url,cookies=cookies)
print(r1.text)

#复杂写法（目前不太明白）
s = requests.Session()
c = requests.cookies.RequestsCookieJar()
c.set("cookies-name","cookies-value",path="/",domain=".test.com")
s.cookies.update(c)
print(s.cookies)
