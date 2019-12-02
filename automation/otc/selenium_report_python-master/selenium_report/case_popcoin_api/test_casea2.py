# coding:utf-8
import json
import time
import requests
from common.readexcel import ExcelUtil
import unittest
import ddt
import random
from common import config_read
from common.popcoin_api import code
from common.popcoin_api.update_idtoken import update_token
from common.popcoin_api.update_idtoken import update_uid

testData = ExcelUtil("D:\\自动化\\otc\\popcanshu.xlsx", "login").dict_data()
# print(testData)
s = requests.session()
codehuakuai = 0


@ddt.ddt
class OTC(unittest.TestCase):
    u'''登录'''

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
        global codehuakuai

        '''登录'''
        method = data["method"]
        url = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                     "url", "ceshiip") + data["url"]
        #print(url)
        #time.sleep(10000)
        test_nub = data['id']
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

        if test_nub == 20:
            codehuakuai = code.get_slider_code(body['phone'])
            body['code'] = codehuakuai
        if test_nub >711:
            # codehuakuai = code1(body['phone'])
            if body['phone']:
                body['phone']=random.randint(17610000000,17699999999)
                print(body['phone'],'++++++++++++++++++++++++++++++++++++++++++++++')
            #body['code'] = codehuakuai
            # body['code']="318584"
            # body={"code": "318584", "countryId": 1, "loginPassword": "d13149de00848eb013cad318d27829db64b965d7",
            #    "messageCode": "000000", "phone": "17688989111"}

        phone = body['phone']
        body = json.dumps(body)
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
        r = r.json()

        # print(res)
        # print(res)
        if r['code'] == 1:
            result = "成功"
            update_token(phone)
        else:
            result = "失败"
        # json.loads(body)
        # print(phone,"+++++++++++++++++++++++++++++")
        # update_token(phone)

        self.assertEqual(result, data['result'])


if __name__ == "__main__":
    unittest.main()
