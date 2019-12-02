# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
# import cx_Oracle
import pymysql
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import unittest
from common import login
# from common import ExcelUtil
from common.jieshuju import noround
import ddt
import json
import requests
from common.readexcel import ExcelUtil
import unittest
import ddt
from common import db
from common import config_read
from case.test_casea2 import register, code2
from common.otcapi.newprice import realprice
from case.test_casea2 import register, code2
from case.test_casea1 import update_token
from case.test_casea1 import update_uid

s = requests.session()
from common import loginotc
from common import config_write

from common.writeexcel import copy_excel, Write_excel

testData = ExcelUtil("D:\\自动化\\otc\\canshu.xlsx", "高级商户").dict_data()
# print(testData)
s = requests.session()


@ddt.ddt
class OTC(unittest.TestCase):
    u'''高级商户'''

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome()
        s = requests.session()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        s = requests.session()

    @ddt.data(*testData)
    def test_maidan(self, data):

        '''高级商户'''
        method = data["method"]
        url = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                     "url", "ceshiip") + data["url"]

        # url后面的params参数
        try:
            params = eval(data["params"])
        except:
            params = None
        # 请求头部headers
        try:
            headers = eval(data["headers"])
            # print("请求头部：%s" % headers)
        except:
            headers = None
        # 请求body
        try:
            body = eval(data["body"])
            # print("请求body：%s" % body)
            # print(type(body))
        except:
            body = None
        # print(type(body))
        # phone=body['']

        headers['token'] = config_read.configread(
            "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
            "token" + str(body['userId']),
            "token" + str(body['userId']))
        userid = body['userId'] = config_read.configread(
            "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
            "uid" + str(body['userId']),
            "uid" + str(body['userId']))

        c = db.dbuser().cursor()
        c.execute('select id from tb_kyc_authentication where user_id  = %s ',
                  (userid))
        strs2 = c.fetchall()[0][0]
        body['id'] = strs2
        c.close()
        test_nub = data['id']

        body = json.dumps(body)
        print("*******正在执行用例：-----  %s  ----**********" % test_nub)
        print("请求方式：%s, 请求url:%s" % (method, url))
        print("请求params：%s" % params)
        print("请求headers：%s" % headers)
        print("请求body：%s" % body)
        print("++++++++++++++++++++++++++++++++++++++++++")

        verify = False
        res = {}  # 接受返回数据

        r = s.request(method=method,
                      url=url,
                      params=params,
                      headers=headers,
                      data=body,
                      verify=verify
                      )
        print("页面返回信息：%s" % r.json())
        r = r.json()
        print(r)

        self.assertEqual(1, r['code'])

        # 后台认证+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        method = data["method1"]
        url = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                     "url", "ceshiip") + data["url1"]

        # url后面的params参数
        try:
            params = eval(data["params1"])
        except:
            params = None
        # 请求头部headers
        try:
            headers = eval(data["headers1"])
            # print("请求头部：%s" % headers)
        except:
            headers = None
        # 请求body
        try:
            body = eval(data["body1"])
            # print("请求body：%s" % body)
            # print(type(body))
        except:
            body = None
        # print(type(body))

        headers['token'] = config_read.configread(
            "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
            "token" + str("admin"),
            "token" + str("admin"))

        body['id'] = strs2
        c.close()

        test_nub = data['id']

        body = json.dumps(body)
        print("*******正在执行用例：-----  %s  ----**********" % test_nub)
        print("请求方式：%s, 请求url:%s" % (method, url))
        print("请求params：%s" % params)
        print("请求headers：%s" % headers)
        print("请求body：%s" % body)
        print("++++++++++++++++++++++++++++++++++++++++++")

        verify = False
        res = {}  # 接受返回数据

        r = s.request(method=method,
                      url=url,
                      params=params,
                      headers=headers,
                      data=body,
                      verify=verify
                      )
        print("页面返回信息：%s" % r.json())
        r = r.json()
        print(r)

        self.assertEqual(1, r['code'])


if __name__ == "__main__":
    unittest.main()
