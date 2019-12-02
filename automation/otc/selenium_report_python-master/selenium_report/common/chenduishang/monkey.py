import os
import re
import xml.dom.minidom as xmldom
import time


class Mtest():
    def __init__(self):
        dom = xmldom.parse('config.xml')
        root = dom.documentElement
        self.packagename = root.getElementsByTagName('packagename')[0].firstChild.data
        self.mainactivity = root.getElementsByTagName('mainactivity')[0].firstChild.data
        self.interval = int(root.getElementsByTagName('interval')[0].firstChild.data)
        self.count = int(root.getElementsByTagName('count')[0].firstChild.data)
        self.whiteactivity = root.getElementsByTagName('whiteactivity')[0].firstChild.data.replace('\n', '').replace(
            ' ', '').split(',')

    def get_now_activity(self):
        os.system("adb devices")
        content = os.popen('adb shell dumpsys activity  |findstr "mResumedActivity" ').read()  # 读取当前页面
        pattern = re.compile(r'/[a-zA-Z0-9\.]+')
        alist = pattern.findall(content)
        macitivity = self.packagename + '/' + self.mainactivity
        excuteshell = 'adb shell am start -n' + macitivity
        if alist[0] not in self.whiteactivity:
            print('当前activity:' + alist[0])
            print('--------------开始返回主activity----------------')
            os.system(excuteshell)  # 可拉回主页面
        else:
            print('当前activity:' + alist[0] + '不需要返回')

    def check(self):
        for _ in range(self.count):
            time.sleep(self.interval)
            self.get_now_activity()


if __name__ == '__main__':
    test = Mtest()
    test.check()

    #test.get_now_activity()
