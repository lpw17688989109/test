# coding=utf-8
import configparser
import os

def configread(addr,wenjian,key,volue):

    os.chdir(addr)
    cf = configparser.ConfigParser()

    # read(filename) 读文件内容
    filename = cf.read(wenjian)
    #print(filename)
    # sections() 得到所有的section，以列表形式返回
    sec = cf.sections()
   # print(sec)
    #调用get方法，然后获取配置的数据
    sender=cf.get(key,volue)
    #print(sender)
    return sender
