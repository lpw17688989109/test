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
from common.otcapi.newprice import realprice
# c = db.db().cursor()

from case.test_casea1 import update_token

update_token(17688989111)
update_token(17688989222)

testData = ExcelUtil("D:\\自动化\\otc\\canshu.xlsx", "Sheet1").dict_data()
# print(testData)
s = requests.session()


@ddt.ddt
class OTC(unittest.TestCase):
    u'''OTC买卖'''

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

        '''广告购买'''
        method = data["method"]
        url = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                     "url", "ceshiip") + data["url"]
        token17688989111 = config_read.configread(
            "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "token17688989111",
            "token17688989111")
        token17688989222 = config_read.configread(
            "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "token17688989222",
            "token17688989222")
        print(token17688989111)
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
            print("请求body：%s" % body)
            # print(type(body))
        except:
            body = None
        # print(type(body))
        if int(headers['userId']) == 1000236:
            headers['token'] = token17688989111
        if int(headers['userId']) == 1000264:
            headers['token'] = token17688989222
        # del headers['userId']

        # post请求body类型
        type = data["type"]
        token = headers['token']
        advertisementNo = body['advertisementId']
        # print(advertisementNo, token)
        offer = realprice(advertisementNo, token)

        # print(offer,"+++++++++++++++++++++++++++++++++++++++++++")
        buyCount = body['buyingAmount'] * 1000000 / offer / 1000000
        buyCount = noround(buyCount, 6)
        print(buyCount, "_______________________________________")
        body['buyCount'] = buyCount

        test_nub = data['id']
        print(body, "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        buyid = int(headers['userId'])
        buysymbolId = body['symbolId']
        buy1symbolId = body['symbolId']
        if buy1symbolId == 3:
            dongjie = 1
        if buy1symbolId == 2:
            dongjie = 1
        if buy1symbolId == 1:
            dongjie = 1
        # headers=json.dumps(headers)
        del headers['userId']
        body = json.dumps(body)
        print("*******正在执行用例：-----  %s  ----**********" % test_nub)
        print("请求方式：%s, 请求url:%s" % (method, url))
        print("请求params：%s" % params)
        print("请求headers：%s" % headers)
        print("请求body：%s" % body)
        print("++++++++++++++++++++++++++++++++++++++++++")
        c = db.db().cursor()
        c.execute('select balance,freezing_balance,total_price from tb_user_coin where user_id  = %s and coin_id = %s',
                  (buyid, buysymbolId))
        strs2 = c.fetchall()
        strs2 = strs2[0]
        buyqian = []
        c.close()
        print(strs2)
        for i in strs2:
            # i = float(i)
            # print(i)
            # totalCount = re.sub("\D", "", i)
            buyqian.append(i)
        # print(buyqian)

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
        # r=json.loads(r)
        res['orderNo'] = r['data']['orderNo']
        res['coins'] = r['message']
        # res['rowNum'] = data['rowNum']
        # res["statuscode"] = str(r.status_code)  # 状态码转成str
        print(res)

        ####################################################################################
        method1 = data["method"]
        url1 = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                      "url", "ceshiip") + data["url1"]
        # url后面的params参数
        try:
            params1 = eval(data["params1"])
        except:
            params1 = None
        # 请求头部headers
        try:
            headers1 = eval(data["headers1"])
            # print("请求头部：%s" % headers)
        except:
            headers1 = None
        # 请求body
        try:
            body1 = eval(data["body1"])
            # print("请求body：%s" % body)
            # print(type(body))
        except:
            body1 = None
        # print(type(body))
        if int(headers1['userId']) == 1000236:
            headers1['token'] = token17688989111
        if int(headers1['userId']) == 1000264:
            headers1['token'] = token17688989222
        # post请求body类型
        body1['orderNo'] = res['orderNo']
        del headers1['userId']
        body1 = json.dumps(body1)
        print("*******正在执行用例：-----  %s  ----**********" % test_nub)
        print("请求方式：%s, 请求url1:%s" % (method1, url1))
        print("请求params1：%s" % params1)
        print("请求headers1：%s" % headers1)
        print("请求body1：%s" % body1)

        r1 = s.request(method=method,
                       url=url1,
                       params=params1,
                       headers=headers1,
                       data=body1,
                       verify=verify
                       )
        print("页面返回信息：%s" % r1.json())
        r1 = r1.json()
        # r=json.loads(r)
        res['payment'] = r1['message']
        # res['rowNum'] = data['rowNum']
        # res["statuscode"] = str(r.status_code)  # 状态码转成str
        print(res)

        ##########################################################################################################################
        method1 = data["method"]
        url2 = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                      "url", "ceshiip") + data["url2"]
        # url后面的params参数
        try:
            params2 = eval(data["params2"])
        except:
            params2 = None
        # 请求头部headers
        try:
            headers2 = eval(data["headers2"])
            # print("请求头部：%s" % headers)
        except:
            headers2 = None
        # 请求body
        try:
            body2 = eval(data["body2"])
            # print("请求body：%s" % body)
            # print(type(body))
        except:
            body2 = None
        # print(type(body))
        if int(headers2['userId']) == 1000236:
            headers2['token'] = token17688989111
        if int(headers2['userId']) == 1000264:
            headers2['token'] = token17688989222
        # post请求body类型
        body2['orderNo'] = res['orderNo']
        sellid = int(headers2['userId'])
        # sellsymbolId = body2['symbolId']
        body2 = json.dumps(body2)
        del headers2['userId']
        print("*******正在执行用例：-----  %s  ----**********" % test_nub)
        print("请求方式：%s, 请求url2:%s" % (method, url2))
        print("请求params2：%s" % params2)
        print("请求headers2：%s" % headers2)
        print("请求body2：%s" % body2)
        c = db.db().cursor()
        c.execute('select balance,freezing_balance,total_price from tb_user_coin where user_id  = %s and coin_id = %s',
                  (sellid, buysymbolId))
        strs2 = c.fetchall()
        strs2 = strs2[0]
        sellqian = []
        # print(strs2)
        c.close()
        for i in strs2:
            # i = float(i)
            # print(i)
            # totalCount = re.sub("\D", "", i)
            sellqian.append(i)
        # print(sellqian)

        r2 = s.request(method=method,
                       url=url2,
                       params=params2,
                       headers=headers2,
                       data=body2,
                       verify=verify
                       )
        print("页面返回信息：%s" % r2.json())
        r2 = r2.json()
        # r=json.loads(r)
        res['seller/confirmation'] = r2['message']
        # res['rowNum'] = data['rowNum']
        # res["statuscode"] = str(r.status_code)  # 状态码转成str
        time.sleep(0.5)

        #################################################################订单管理
        method3 = data["method"]
        url3 = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                      "url", "ceshiip") + data["url3"]
        # url后面的params参数
        try:
            params3 = eval(data["params3"])
        except:
            params3 = None
        # 请求头部headers
        try:
            headers3 = eval(data["headers3"])
            # print("请求头部：%s" % headers)
        except:
            headers3 = None
        # 请求body
        try:
            body3 = eval(data["body3"])
            # print("请求body：%s" % body)
            # print(type(body))
        except:
            body3 = None
        # print(type(body))
        if int(headers3['userId']) == 1000236:
            headers3['token'] = token17688989111
        if int(headers3['userId']) == 1000264:
            headers3['token'] = token17688989222
        # post请求body类型
        body3['orderNo'] = res['orderNo']
        body3 = json.dumps(body3)
        del headers3['userId']
        print("*******正在执行用例：-----  %s  ----**********" % test_nub)
        print("请求方式：%s, 请求url1:%s" % (method1, url3))
        print("请求params3：%s" % params3)
        print("请求headers3：%s" % headers3)
        print("请求body3：%s" % body3)

        r1 = s.request(method=method,
                       url=url3,
                       params=params3,
                       headers=headers3,
                       data=body3,
                       verify=verify
                       )
        print("页面返回信息：%s" % r1.json())
        r1 = r1.json()
        # r=json.loads(r)
        res['istration/inhand'] = r1['message']
        transactionVolume = r1['data']['list'][0]['transactionVolume']
        rebatefee = transactionVolume * 4000000 / 1000000000
        rebatefee = noround(rebatefee, 6)
        #print(rebatefee, "--------------------------------------------------------------")
        symbolPrice = r1['data']['list'][0]['symbolPrice']
        buyingAmount = r1['data']['list'][0]['buyingAmount']
        transactionVolume_shouxu = transactionVolume * 1000000 * dongjie / 1000000
        print(dongjie)
        # print(transactionVolume)
        # print(transactionVolume_shouxu)
        # transactionVolume=noround(transactionVolume, 6)
        # transactionVolume_shouxu = transactionVolume * dongjie
        transactionVolume_shouxu = noround(transactionVolume_shouxu, 6)

        res['ransactionVolume'] = transactionVolume
        res['transactionVolume_shouxu'] = transactionVolume_shouxu
        res['symbolPrice'] = symbolPrice
        res['buyingAmount'] = buyingAmount

        # res['rowNum'] = data['rowNum']
        # res["statuscode"] = str(r.status_code)  # 状态码转成str



        print(res)
        c = db.db().cursor()
        c.execute('select balance,freezing_balance,total_price from tb_user_coin where user_id  = %s and coin_id = %s',
                  (buyid, buysymbolId))
        strs2 = c.fetchall()
        strs2 = strs2[0]
        buyhou = []
        c.close()
        # print(strs2)
        for i in strs2:
            # i = float(i)
            # print(i)
            # totalCount = re.sub("\D", "", i)
            buyhou.append(i)
        # print(buyhou)

        c = db.db().cursor()
        c.execute('select balance,freezing_balance,total_price from tb_user_coin where user_id  = %s and coin_id = %s',
                  (sellid, buysymbolId))
        strs2 = c.fetchall()
        strs2 = strs2[0]
        sellhou = []
        # print(strs2)
        c.close()
        for i in strs2:
            # i = float(i)
            # print(i)
            # totalCount = re.sub("\D", "", i)
            sellhou.append(i)
        # print(sellhou)
        yanzransactionVolume = res['buyingAmount'] * 1000000 / res['symbolPrice'] / 1000000
        yanzransactionVolume = noround(yanzransactionVolume, 6)

        print(buyqian)
        print(buyhou)
        print(sellqian)
        print(sellhou)
        buybalanceb = noround((buyhou[0] - buyqian[0]), 6)
        buyfreezing_balanceb = noround((buyhou[1] - buyqian[1]), 6)
        buytotal_priceb = noround((buyhou[2] - buyqian[2]), 6)
        print("买家资产变化%s，%s，%s" % (buybalanceb, buyfreezing_balanceb, buytotal_priceb))

        sellbalanceb = noround((sellhou[0] - sellqian[0]), 6)
        sellbalanceb = noround(sellbalanceb, 6)

        sellfreezing_balanceb = noround((sellhou[1] - sellqian[1]), 6)
        selltotal_priceb = noround((sellhou[2] - sellqian[2]), 6)
        sellend = (selltotal_priceb * 1000000 - rebatefee * 1000000) / 1000000
        sellend = noround(sellend, 6)

        print("卖家资产变化%s，%s，%s" % (str(sellbalanceb), sellfreezing_balanceb, selltotal_priceb))
        # self.assertEqual(res['ransactionVolume'], buybalanceb)
        # self.assertEqual(res['ransactionVolume'], buytotal_priceb)
        self.assertEqual(res['ransactionVolume'], buybalanceb)
        self.assertEqual(res['ransactionVolume'], buybalanceb)
        self.assertEqual(0.0, buyfreezing_balanceb)

        self.assertEqual(-res['transactionVolume_shouxu'], sellfreezing_balanceb)
        self.assertEqual(sellfreezing_balanceb, sellend)
        self.assertEqual(rebatefee, sellbalanceb)
        self.assertEqual(yanzransactionVolume, res['ransactionVolume'])


if __name__ == "__main__":
    unittest.main()
if __name__ == "__main__":
    unittest.main
if __name__ == "__main__":
    unittest.main
