# coding:utf-8

c = "%u4E0A%u6D77%u60A0%u60A0"
# python3解决办法：替换%
d = c.replace("%", "\\")
#d = c.replace("u","u")
print(d)
#python3先encode成utf-8编码，再decode成默认的unicode就可以了
print(d.encode("utf-8").decode("unicode_escape"))
print(d.encode("utf-8").decode("unicode_escape"))