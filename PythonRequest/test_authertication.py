import requests

#basic
r = requests.get("http://httpbin.org/basic-auth/user/password",auth=('user','password'))
print(r.text)