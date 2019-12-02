# coding:utf-8
import json
import requests
s = requests.session()
from common.popcoin_api import config_write
from common.popcoin_api.login import login



def update_token(phone):
    config_write.write(("token" + str(phone)), ("token" + str(phone)), login(phone))
def update_uid(phone, uid):
    config_write.write(("uid" + str(phone)), ("uid" + str(phone)), uid)

#config_write.write(("tokenadmin"), ("tokenadmin"), login())

#login(17688900060)

#print(login(17688900060))