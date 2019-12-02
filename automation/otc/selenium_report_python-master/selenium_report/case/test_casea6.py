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
from common.jieshuju import noround
# from common import ExcelUtil
import ddt
import json
import requests
from common.readexcel import ExcelUtil
import unittest
import ddt
from common import db
from common import config_read

c = db.db().cursor()
from common.otcapi.newprice import realprice
from case.test_casea1 import update_token

update_token(17688989111)
update_token(17688989222)

# import login
# import run_this
'''filepath = "D:\\机器猫任务\\新任务\\自动化覆盖\\风控自动化用例模板.xlsx"
sheetName = "个性投资-新增"
data = ExcelUtil.ExcelUtil(filepath, sheetName)
testData = data.dict_data()'''
'''#迭代
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='111111', db="python", charset='utf8mb4')
c = conn.cursor()
c.execute('select * from tt_gxkzl_xmb where 编号  = 0  order by 编号')
strs2 = c.fetchall();
key = strs2[0]
#print(key)
c.execute('select * from tt_gxkzl_xmb where 编号  >= 9  order by 编号')
strs = c.fetchall();
#print(strs)
testData = [dict(zip(key, v)) for v in strs]
print(testData)'''

from common.writeexcel import copy_excel, Write_excel

testData = ExcelUtil("D:\\自动化\\otc\\canshu.xlsx", "Sheet2").dict_data()
# print(testData)
s = requests.session()


@ddt.ddt
class OTC(unittest.TestCase):
    u'''买卖流程'''

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

        '''出售数字货币'''
        method = data["method"]
        url = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                     "url", "ceshiip") + data["url"]
        token17688989111 = config_read.configread(
            "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "token17688989111",
            "token17688989111")
        token17688989222 = config_read.configread(
            "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "token17688989222",
            "token17688989222")
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
        if int(headers['userId']) == 1000236:
            headers['token'] = token17688989111
        if int(headers['userId']) == 1000264:
            headers['token'] = token17688989222
        # post请求body类型
        type = data["type"]
        # post请求body类型
        type = data["type"]
        token = headers['token']
        advertisementNo = body['advertisementId']
        print(advertisementNo, token)
        offer = realprice(advertisementNo, token)

        print(offer, "+++++++++++++++++++++++++++++++++++++++++++")
        buyCount = body['buyingAmount'] * 1000000 / offer / 1000000
        buyCount = noround(buyCount, 6)
        print(buyCount, "_______________________________________")
        body['buyCount'] = buyCount

        test_nub = data['id']
        sell1id = int(headers['userId'])
        buy1symbolId = body['symbolId']
        if buy1symbolId == 3:
            dongjie = 1
        if buy1symbolId == 2:
            dongjie = 1
        if buy1symbolId == 1:
            dongjie = 1
        # dongjie = body['buyingAmount'] * 1.1
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
                  (sell1id, buy1symbolId))
        strs1 = c.fetchall()
        strs1 = strs1[0]
        sell1qian = []
        c.close()
        # print(strs2)
        for i in strs1:
            # i = float(i)
            # print(i)
            # totalCount = re.sub("\D", "", i)
            sell1qian.append(i)
        # print(sell1qian)

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
        c = db.db().cursor()
        c.execute('select balance,freezing_balance,total_price from tb_user_coin where user_id  = %s and coin_id = %s',
                  (sell1id, buy1symbolId))
        strs2 = c.fetchall()
        strs2 = strs2[0]
        sell1zhong = []
        c.close()
        # print(strs2)
        for i in strs2:
            # i = float(i)
            # print(i)
            # totalCount = re.sub("\D", "", i)
            sell1zhong.append(i)
            # print(sell1zhong)
        # r=json.loads(r)
        res['orderNo'] = r['data']['orderNo']
        res['coins'] = r['message']
        # res['rowNum'] = data['rowNum']
        # res["statuscode"] = str(r.status_code)  # 状态码转成str
        print(res)

        self.assertEqual(res['coins'], '成功')

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
        buy1id = int(headers1['userId'])
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
        self.assertEqual(res['payment'], '成功')

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

        # buy1symbolId = body['symbolId']
        del headers2['userId']
        body2 = json.dumps(body2)
        print("*******正在执行用例：-----  %s  ----**********" % test_nub)
        print("请求方式：%s, 请求url2:%s" % (method, url2))
        print("请求params2：%s" % params2)
        print("请求headers2：%s" % headers2)
        print("请求body2：%s" % body2)
        c = db.db().cursor()
        c.execute('select balance,freezing_balance,total_price from tb_user_coin where user_id  = %s and coin_id = %s',
                  (buy1id, buy1symbolId))
        strs3 = c.fetchall()
        strs3 = strs3[0]
        buy1qian = []
        c.close()
        # print(strs3)
        for i in strs3:
            # i = float(i)
            # print(i)
            # totalCount = re.sub("\D", "", i)
            buy1qian.append(i)
        # print(buy1qian)

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
        res['symbol-sell'] = r2['message']
        self.assertEqual(res['symbol-sell'], '成功')
        # res['rowNum'] = data['rowNum']
        # res["statuscode"] = str(r.status_code)  # 状态码转成str



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
        del headers3['userId']
        body3 = json.dumps(body3)
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
        self.assertEqual(res['istration/inhand'], '成功')
        transactionVolume = r1['data']['list'][0]['transactionVolume']
        print(transactionVolume, "第一次取值")
        symbolPrice = r1['data']['list'][0]['symbolPrice']
        buyingAmount = r1['data']['list'][0]['buyingAmount']
        # transactionVolume=float(transactionVolume)
        transactionVolume_shouxu = transactionVolume * 1000000 * dongjie / 1000000
        print(dongjie)
        # transactionVolume = noround(transactionVolume, 6)
        print(transactionVolume, "第二次取值")
        transactionVolume_shouxu = noround(transactionVolume_shouxu, 6)
        res['ransactionVolume'] = transactionVolume
        res['transactionVolume_shouxu'] = transactionVolume_shouxu
        res['symbolPrice'] = symbolPrice
        res['buyingAmount'] = buyingAmount
        print(res)
        c = db.db().cursor()
        c.execute('select balance,freezing_balance,total_price from tb_user_coin where user_id  = %s and coin_id = %s',
                  (sell1id, buy1symbolId))
        strs4 = c.fetchall()
        strs4 = strs4[0]
        sell1hou = []
        c.close()
        # print(strs4)
        for i in strs4:
            # i = float(i)
            # print(i)
            # totalCount = re.sub("\D", "", i)
            sell1hou.append(i)
        # print(sell1hou)

        c = db.db().cursor()
        c.execute('select balance,freezing_balance,total_price from tb_user_coin where user_id  = %s and coin_id = %s',
                  (buy1id, buy1symbolId))
        strs5 = c.fetchall()
        strs5 = strs5[0]
        buy1hou = []
        c.close()
        # print(strs5)
        for i in strs5:
            # i = float(i)
            # print(i)
            # totalCount = re.sub("\D", "", i)
            buy1hou.append(i)
        # print(buy1hou)
        yanzransactionVolume = res['buyingAmount'] * 1000000 / res['symbolPrice'] / 1000000
        yanzransactionVolume = noround(yanzransactionVolume, 6)
        print(yanzransactionVolume, "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        print(sell1qian)
        print(sell1zhong)
        print(buy1qian)
        print(buy1hou)
        print(sell1hou)
        print(dongjie)
        time.sleep(0.5)
        buybalanceb = noround((buy1hou[0] - buy1qian[0]), 6)
        buyfreezing_balanceb = noround((buy1hou[1] - buy1qian[1]), 6)
        buytotal_priceb = noround((buy1hou[2] - buy1qian[2]), 6)
        print("买家资产变化%s，%s，%s" % (buybalanceb, buyfreezing_balanceb, buytotal_priceb))
        zsellbalanceb = noround((sell1zhong[0] - sell1qian[0]), 6)
        zsellfreezing_balanceb = noround((sell1zhong[1] - sell1qian[1]), 6)
        zselltotal_priceb = noround((sell1zhong[2] - sell1qian[2]), 6)
        print("刚下单卖家资产变化%s，%s，%s" % (zsellbalanceb, zsellfreezing_balanceb, zselltotal_priceb))
        sellbalanceb = noround((sell1hou[0] - sell1qian[0]), 6)
        sellfreezing_balanceb = noround((sell1hou[1] - sell1qian[1]), 6)
        selltotal_priceb = noround((sell1hou[2] - sell1qian[2]), 6)
        print("卖家资产变化%s，%s，%s" % (sellbalanceb, sellfreezing_balanceb, selltotal_priceb))
        self.assertEqual(res['transactionVolume_shouxu'], buybalanceb)
        self.assertEqual(res['transactionVolume_shouxu'], buybalanceb)
        self.assertEqual(0.0, buyfreezing_balanceb)
        self.assertEqual(-res['ransactionVolume'], zsellbalanceb)
        self.assertEqual(res['ransactionVolume'], zsellfreezing_balanceb)
        self.assertEqual(0.0, zselltotal_priceb)
        self.assertEqual(-res['ransactionVolume'], sellbalanceb)
        self.assertEqual(-res['ransactionVolume'], selltotal_priceb)
        self.assertEqual(0.0, sellfreezing_balanceb)
        self.assertEqual(yanzransactionVolume, res['ransactionVolume'])


if __name__ == "__main__":
    unittest.main()
