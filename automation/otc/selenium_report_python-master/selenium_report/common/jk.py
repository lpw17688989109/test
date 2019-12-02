# coding=utf-8
import requests
par={"Keywords":"yoyoketang"}
r = requests.get('http://www.cnblogs.com/yoyoketang/')
r = requests.get('http://zzk.cnblogs.com/s/blogpost?',params=par)
r = requests.get('https://www.baidu.com/')
print(r.status_code)
#print(r.text)
print(r.content)
-- r.status_code     #响应状态码
-- r.content           #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
-- r.headers          #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
-- r.json()             #Requests中内置的JSON解码器
-- r.url                  # 获取url
-- r.encoding         # 编码格式
-- r.cookies           # 获取cookie
-- r.raw                #返回原始响应体
-- r.text               #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
-- r.raise_for_status() #失败请求(非200响应)抛出异常