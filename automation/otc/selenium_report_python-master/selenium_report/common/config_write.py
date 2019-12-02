from configobj import ConfigObj

def write(section,key,value):

    # *** 配置文件预处理 *** #
    config = ConfigObj("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config\\new.ini",encoding='UTF8')

    # *** 读配置文件 *** #
    # print(config['txtB'])
    # print(config['txtB']['name'])

    # *** 修改配置文件 *** #
    #try:
     #   config['token181']['token181'] = "Mufasa"
    #except:


    config[section] = {}
    config[section][key] = value
    config.write()

    # *** 添加section *** #
    # config['txtC'] = {}
    # config['txtC']['index0'] = "wanyu00"
    # config.write()

#write("token1810","token181","token")
