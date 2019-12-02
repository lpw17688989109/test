# coding:utf-8
import threading
import time

def chi():
    print("%s 吃着火锅开始：" % time.ctime())
    time.sleep(1)
    print("%s 吃着火锅：涮羊肉" % time.ctime())
    time.sleep(1)
    print("%s 吃着火锅：涮牛肉" % time.ctime())
    time.sleep(1)
    print("%s 吃着火锅：贡丸" % time.ctime())
    time.sleep(1)
    print("%s 吃火锅结束！" % time.ctime())
def ting():
    print("%s 哼着小曲1！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲2！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲3！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲4！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲5！" % time.ctime())
    time.sleep(2)

def ting2():
    print("%s 11哼着小曲1！" % time.ctime())
    time.sleep(2)
    print("%s 11哼着小曲2！" % time.ctime())
    time.sleep(2)
    print("%s 11哼着小曲3！" % time.ctime())
    time.sleep(2)
    print("%s 11哼着小曲4！" % time.ctime())
    time.sleep(2)
    print("%s 11哼着小曲5！" % time.ctime())
    time.sleep(2)

# 创建线程数组
threads = []
# 创建线程t1，并添加到线程数组
t1=threading.Thread(target=ting2)
threads.append(t1)
t1 = threading.Thread(target=chi)
threads.append(t1)
# 创建线程t2，并添加到线程数组
t2 = threading.Thread(target=ting)
threads.append(t2)

if __name__ == '__main__':
    # 启动线程
    for t in threads:
        t.start()