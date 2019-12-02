#print((-0.001372*1000000-0.000009*1000000)/1000000)
from decimal import Decimal
from decimal import getcontext


#买1=外部市场价*[1-盘口价差值（固定值）]
#卖1=外部市场价*[1+盘口价差值（固定值）]
#买N=买1-（成交价-买1）*（N-1）*（50%～100%随机值）
#卖N=卖1+（卖1-成交价）*（N-1）*（50%～100%随机值）

print(Decimal('7431.8')*Decimal('0.9995'))

print(Decimal('7431.8')-(Decimal('0.0239110000000000')-Decimal('0.0209110000000000'))*5*1)












# 资产变更------- 1001843
# usdt
'''print("1001843   usdt---")
print(Decimal('6249.97')*Decimal('5.8888'))
print(Decimal('938195.8816620000000000')-Decimal('938195.8816620000000000'))
print(Decimal('36804.8233360000000000')-Decimal('0.0000000000000000'))
print(Decimal('975000.7049980000000000')-Decimal('938195.8816620000000000'))
print(Decimal('6249.98')*Decimal('2'))#*Decimal('0.998'))'''


#btc
print("1001843   btc---")
print(Decimal('9009.999999')*Decimal('9.9999')+Decimal('9000.999998')*Decimal('1.8888')+Decimal('8999.999997')*Decimal('1.7777'))
print(Decimal('8999.999996')*Decimal('6'))
print(Decimal('1000000.0000000000000000') -Decimal('876900.5122200000000000'))
print(Decimal('0.0000000000000000') -Decimal('123099.4877800000000000'))
print(Decimal('1000000.0000000000000000') -Decimal('946000.0000240000000000'))
print(Decimal('5.8888')*Decimal('0.998'))
print(Decimal('5.8888')*Decimal('0.002'))



#eth
print("1001843   eth---")
print(Decimal('1000000.0000000000000000') -Decimal('876900.5122200000000000'))
print(Decimal('0.0000000000000000') -Decimal('123099.4877800000000000'))
print(Decimal('1000000.0000000000000000') -Decimal('1000000.0000000000000000'))
print(Decimal('5.8888')*Decimal('0.998'))
print(Decimal('5.8888')*Decimal('0.002'))



print("+++++++++++++++++++++++++++++++++++++")
# 资产变更------- 1001844
# usdt
'''print("1001844   usdt----")
print(Decimal('6249.97')*Decimal('6.6666'))
print(Decimal('1162864.7782448680000000')-Decimal('1121282.0603428720000000'))
print(Decimal('0.0000000000000000')-Decimal('0.0000000000000000'))
print(Decimal('1162864.7782448680000000')-Decimal('1121282.0603428720000000'))
print(Decimal('6249.97')*Decimal('6.6666')*Decimal('0.998'))
print(Decimal('6249.98')*Decimal('6.6666')*Decimal('0.002'))'''


#btc
print("1001844   btc---")
print((Decimal('9009.999999')*Decimal('9.9999')+Decimal('9000.999998')*Decimal('1.8888')+Decimal('8999.999997')*Decimal('1.7777'))*Decimal('0.998'))
print((Decimal('8999.999999')*Decimal('9.9999')+Decimal('8998.999998')*Decimal('1.8888')+Decimal('8997.999998')*Decimal('1.7777')))
print(Decimal('9009.999999')*Decimal('9.9999')+Decimal('9000.999998')*Decimal('1.8888')+Decimal('8999.999997')*Decimal('1.7777'))
print(Decimal('1000000.0000000000000000') -Decimal('876900.5122191106000000'))
print(Decimal('0.0000000000000000') -Decimal('123099.4877800000000000'))
print(Decimal('1000000.0000000000000000') -Decimal('876900.5122191106000000'))
print(Decimal('8999.999996')*Decimal('6')*Decimal('0.998'))
print(Decimal('13.6664')*Decimal('0.998'))
print(Decimal('13.6664')*Decimal('0.002'))

#eth
print("1001844   eth----")
print(Decimal('9.9999')+Decimal('1.8888')+Decimal('1.7777'))
print(Decimal('1000000.0000000000000000') -Decimal('1162864.7782448680000000'))
print(Decimal('0.0000000000000000') -Decimal('123099.4877800000000000'))
print(Decimal('1000000.0000000000000000') -Decimal('1162864.7782448680000000'))
print(Decimal('5.8888')*Decimal('0.998'))
print(Decimal('5.8888')*Decimal('0.002'))


print(Decimal('9.999999')+Decimal('1.888888')+Decimal('1.777777'))

