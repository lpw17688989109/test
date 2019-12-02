# # coding=utf-8
# d={}
# def suijisu():
#     import random
#     global d
#     #print(random.randint(0,9))
#     a=random.randint(0,9)
#     try:
#         d[a]=d[a]+1
#     except:
#         d[a] = 1
#
# n=1
# while n<1001 :
#     suijisu()
#     n=n+1
# print(d)
import json
'''a={
'advertisementId': "10874710649745409",
'buyingAmount': "110",
'currencyId': 1,
'password': "d13149de00848eb013cad318d27829db64b965d7",
'symbolId': 1
}
print(json.dumps(a))'''

b={"advertisementId": "12694569327013889", "buyingAmount": 100, "symbolId": 3, "currencyId": 1, "purchaseType": 1}
print(json.dumps(b))
#c=json.loads(b)
#print(c)
a='123'
print(list(a))