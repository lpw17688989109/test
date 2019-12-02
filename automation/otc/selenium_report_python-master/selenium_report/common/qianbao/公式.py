#print((-0.001372*1000000-0.000009*1000000)/1000000)
from decimal import Decimal
from decimal import getcontext


#买：[目标价或（当前成交价*涨跌值）-当前成交价]除以[（持续时间-已执行时间-下单间隔时间）除以下单间隔时间]除以每秒下单单数+最新成交价=委托价

n=0
a=10000
def jg1(n):
    global a
    a =(11000 - a )/((3600-10*n)/10)+ a
    print(a)
for n in range(360):
    n=n+1
    jg1(n)



#