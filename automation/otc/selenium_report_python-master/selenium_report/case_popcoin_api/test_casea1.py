# coding:utf-8
import json
import time
import requests
s = requests.session()
from common.popcoin_api import login
'''def update_token(phone):
    config_write.write(("token" + str(phone)), ("token" + str(phone)), login(phone))
def update_uid(phone, uid):
    config_write.write(("uid" + str(phone)), ("uid" + str(phone)), uid)'''
#config_write.write(("tokenadmin"), ("tokenadmin"), login())
from common.readexcel import ExcelUtil
import unittest
import ddt
from common.popcoin_api import code
from common.popcoin_api.update_idtoken import update_token
from common.popcoin_api.update_idtoken import update_uid
from common import config_write

testData = ExcelUtil("D:\\自动化\\otc\\popcanshu.xlsx", "注册用户").dict_data()
print(testData)
#time.sleep(10000)

s = requests.session()


@ddt.ddt
class OTC(unittest.TestCase):
    u'''pop注册'''

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

        '''注册'''

        try:
            phone = int(data["phone"])
        except:
            phone = None
        try:
            yzm = str(data["yzm"])
        except:
            yzm = None
        print(phone)
        # print(data)
        a = code.register(phone, code.send_sms_code(phone))
        a = list(a)
        #print(type(a))
        print(a)


        self.assertEqual("成功", a[0])

        update_token(phone)
        update_uid(phone, a[1])


if __name__ == "__main__":
    unittest.main()
