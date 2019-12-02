# coding=utf-8
# coding:utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest, time, re
#import cx_Oracle
import pymysql
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import unittest
from common import login
#from common import ExcelUtil
from common.jieshuju import noround
import ddt
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
import unittest
import time
s = requests.session()

def login(phone):
    u'''这里写了一个登录的方法,账号和密码参数化'''
    method="post"
    url1=config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config","new.ini","url","ceshiip")+"8006/api/user/pop/login"
    print(url1)
    headers1={'Content-Type': 'application/json', 'channel': '3', 'deviceType': '3'}
    body1={"code":"","countryId":1,"loginPassword":"d13149de00848eb013cad318d27829db64b965d7","messageCode":"000000","phone": phone,"serviceKey":"POPCoin70947"}
    #{"code":"","loginPassword":"d13149de00848eb013cad318d27829db64b965d7","phone":"17688900005","serviceKey":"POPCoin70947"}
    body1=json.dumps(body1)
    verify="verify"
    r1 = s.request(method=method,
                   url=url1,
                   headers=headers1,
                   data=body1,
                   verify=verify
                   )
    #print("页面返回信息：%s" % r1.json())
    r1 = r1.json()
    print(r1['data']['token'])
    print(r1)
    return r1['data']['token']

login(17688900005)



