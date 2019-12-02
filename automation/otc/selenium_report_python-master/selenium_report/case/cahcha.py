import json
import requests
from common.readexcel import ExcelUtil
import unittest
import ddt
from common import db
from common import config_read
import pymysql
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
# coding:utf-8
from selenium import webdriver
from case.test_case2 import code1
import unittest
import time

s = requests.session()
def code2(phone):
    u'''这里写了一个登录的方法,账号和密码参数化'''
    method = "post"
    url1 = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                  "url", "ceshiip") + "8087/api/user/send-sms/code"
    # print(url1)
    headers1 = {'Content-Type': 'application/json', 'channel': '0','token': '319260724aa624e9853f9e9b037449704335e77f'}

    body1 = {"code": code1(phone), "countryCode": "0086", "enName": "CNY", "phone": phone, "type": 3}
    body1 = json.dumps(body1)
    print(body1)
    verify = "verify"
    r2 = s.request(method=method,
                   url=url1,
                   headers=headers1,
                   data=body1,
                   verify=verify
                   )
    # print("页面返回信息：%s" % r1.json())
    r2 = r2.json()
    print(r2, "++++++++++++++++++++++++++")

code2(17688911111)