import os
import requests
SERVERPUSHKEY = os.environ["SERVERPUSHKEY"]
url="https://api2.pushdeer.com/message/push?pushkey=" + SERVERPUSHKEY + "&text=🧐大创比赛立项ing..."
info = requests.get(url)  #发送get请求
print("响应状态码是："+str(info.status_code))
print("编码类型是"+str(info.apparent_encoding))
info.encoding='utf-8' #可以更改编码类型
print ("内容是"+info.text)  #输出服务器返回的源代码内容
