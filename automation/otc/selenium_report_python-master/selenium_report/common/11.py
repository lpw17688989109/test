from decimal import Decimal
import decimal
a=0.00081
#a=a*1000000
#a= int(a)
print(a*1.2)
print(a*1000000*1.2/1000000)
a=0.00081
a=Decimal('0.00081')*Decimal('1.2')
print(a)
s="abcdefg"; r=''.join(reversed(s))
print(r)
print(''.join(s))
print(s[::-1])

import requests
import json
s = requests.session()

method="post"
url1="http://192.168.1.233:8087/api/user/otc/login"
print(url1)
headers1={'Content-Type': 'application/json', 'channel': '0',"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}
body1={"code":"","countryId":1,"loginPassword":"d13149de00848eb013cad318d27829db64b965d7","messageCode":"000000","phone": 17688989111}
print(body1)
body1=json.dumps(body1)
print(body1)
verify="verify"
r1 = s.request(method=method,
               url=url1,
               headers=headers1,
               data=body1
               )
print("页面返回信息：%s" % r1.json())
r2 = r1.json()
r3=r1.content

print(r1,r3)
