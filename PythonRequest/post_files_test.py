import requests

host = "https://httpbin.org/"
endpoint = "post"
url = "".join([host, endpoint])

# 1.普通上传
# file = open("hello world.txt", "rb")
# files = {"files":file}
# 2.上传字符串
# files = {"files":("hello world.txt","send sss")}#不懂啊

# 3.自定义文件名、文件类型、以及请求头（请求文件名称、文件路径、文件类型、文件请求头）
# files = {"files":("测试.jpg",open("测试.jpg","rb"),"image/png")}

# 4.传送多个文件
# files = [("file1", ("hello world.txt", open("hello world.txt", "rb"))),
#          ("file2", ("测试.jpg", open("测试.jpg", "rb"), "image/png"))]

#5.流式上传
with open("hello world.txt") as f:
    r = requests.post(url=url,data=f)#注意第2个参数是data

# r = requests.post(url=url, files=files)

print(r.headers)
print(r.text)
