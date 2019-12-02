# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
#import cx_Oracle
import pymysql
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import unittest
from common import config_write
#from common import conf
from common.jieshuju import noround
import ddt
import json
import requests
from common.readexcel import ExcelUtil
import unittest
import ddt
from common import db
from common import config_read
from case.test_casea2 import code1
#from case.test_casea1 import update_token
from case.test_casea2 import code2
from common.otcapi.newprice import realprice



s = requests.session()
def login():
    u'''这里写了一个登录的方法,账号和密码参数化'''
    method="post"
    url1=config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config","new.ini","url","ceshiip")+"8004/api/admin/user/login"
    print(url1,"+++++++++++++++++++++")
    headers1={'Content-Type': 'application/json', 'channel': '1'}
    body1={"loginAccount":"admin","loginPassword":"123456","pageNum":1,"pageSize":13}
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
    return r1['data']['token']
login()
#update_token()
config_write.write(("tokenadmin"),("tokenadmin"),login())
