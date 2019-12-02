# coding:utf-8
import requests
from common.readexcel import ExcelUtil
import unittest
import ddt
from case.test_casea2 import register, code2
from case.test_casea1 import update_token
from case.test_casea1 import update_uid

s = requests.session()


testData = ExcelUtil("D:\\自动化\\otc\\canshu.xlsx", "注册用户").dict_data()
# print(testData)
s = requests.session()


@ddt.ddt
class OTC(unittest.TestCase):
    u'''OTC注册账号'''

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
        a = register(phone, code2(phone), yzm)
        a = list(a)
        # print(type(a))
        print(a)

        self.assertEqual("成功", a[0])

        update_token(phone)
        update_uid(phone, a[1])


if __name__ == "__main__":
    unittest.main()
