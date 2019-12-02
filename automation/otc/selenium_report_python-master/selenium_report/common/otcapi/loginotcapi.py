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
from case.test_case2 import code1
from case.test_case1 import update_token
from case.test_case2 import code2
from common.otcapi.newprice import realprice

testData=ExcelUtil("D:\\自动化\\otc\\canshu.xlsx","login").dict_data()
#print(testData)
s = requests.session()


@ddt.ddt
class OTC(unittest.TestCase):
    u'''登录'''

    @classmethod
    def setUpClass(cls):
        #cls.driver = webdriver.Chrome()
        s = requests.session()

    @classmethod
    def tearDownClass(cls):
        #cls.driver.quit()
        s = requests.session()

    @ddt.data(*testData)
    def test_maidan(self, data):

        '''登录'''
        method = data["method"]
        url = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config","new.ini","url","ceshiip")+data["url"]
        test_nub=data['id']
        try:
            params = eval(data["params"])
        except:
            params = None
        # 请求头部headers
        try:
            headers = eval(data["headers"])
            #print("请求头部：%s" % headers)
        except:
            headers = None
        # 请求body
        try:
            body = eval(data["body"])
            print("请求body：%s" % body)
            #print(type(body))
        except:
            body = None

        if test_nub > 17:
            body['code']=code1(body['phone'])
            #body['code']="318584"
        #body={"code": "318584", "countryId": 1, "loginPassword": "d13149de00848eb013cad318d27829db64b965d7",
         #    "messageCode": "000000", "phone": "17688989111"}


        phone=body['phone']
        body=json.dumps(body)
        print("*******正在执行用例：-----  %s  ----**********" % test_nub)
        print("请求方式：%s, 请求url:%s" % (method, url))
        print("请求params：%s" % params)
        print("请求headers：%s" % headers)
        print("请求body：%s" % body)


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
        r=r.json()

        #print(res)
        #print(res)
        if r['code']==1:
            result="成功"
            update_token(phone)
        else:
            result = "失败"
        #json.loads(body)
        #print(phone,"+++++++++++++++++++++++++++++")
        #update_token(phone)

        self.assertEqual(result, data['result'])







if __name__ == "__main__":
    unittest.main()
