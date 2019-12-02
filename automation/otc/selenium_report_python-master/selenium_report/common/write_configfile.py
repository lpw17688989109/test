#coding=utf-8
import configparser
import os

cf = configparser.ConfigParser()
def writecfigFile(section,option,value,xinzeng):
    import configparser
    import os
    addrr = "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config"
    wenjianm = "new.ini"

    os.chdir(addrr)
    cf = configparser.ConfigParser()
    cf.read('D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config\\new.ini')
    if xinzeng:
        cf.add_section(section)
    cf.set(section, option, value)  # 指定section和option则更新value


    #cf.add_section("group_d32")  # 添加section组
    #cf.set("group_d32", "d_key1", "value1")  # 给添加的section组增加option-value
    # 写回配置文件
    #print(addrr+"\\"+wenjianm)
    cf.write(open('D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config\\new.ini', "r+"))
    #with open("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config\\new.ini", "wb+") as f:
    #    cf.write(f)

#readcfigFile()
addrr="D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config"
wenjianm="new.ini"
keyy="url"
volue = "ceshiip"
os.chdir(addrr)
writecfigFile("2","2","3",0)