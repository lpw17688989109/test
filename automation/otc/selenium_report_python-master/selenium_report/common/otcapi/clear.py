import pymysql
from common import db
from common import config_read
class Mysql():
    def create(self):
        try:
            sql_creat = """CREATE TABLE data_test(
                        id INT unique,
                        name VARCHAR(50),
                        age INT,
                        sex enum('男','女')
                        )"""
            cursor.execute(sql_creat)
            print("建表成功")
        except UserWarning:
            print("建表失败")
    def insert(self):
        try:
            sql_insert = """insert into data_test(id, name, age, sex) VALUES(1, '李牧', 18, '男'),(2, '栗子', 20, '女'),(3, '测试', 26, '男'),(4, '尕娃', 30, '女')"""
            cursor.execute(sql_insert)
            print("插入数据成功")

        except UserWarning:
            print("插入数据失败")
    def select(self):
        try:
            sql_select = """select name from data_test where sex='男'"""
            cursor.execute(sql_select)
            print("查询数据成功")
        except UserWarning:
            print("插入数据失败")
    def delete(self,value):
        try:
            sql_delete = """delete from %s where id = %s""", value
            cursor.execute(sql_delete)
            print("数据删除成功")
        except UserWarning:
            print("数据删除失败")
    def updata(self):
        try:
            sql_update = """update data_test set sex='男' where sex='女'"""
            cursor.execute(sql_update)
            print("数据更新成功")
        except UserWarning:
            print("数据更新失败")
    def delete_table(self):
        sql_delete_table = """drop table data_test"""
        cursor.execute(sql_delete_table)
        print("清洗数据：删除数据表")

if __name__ == '__main__':
    #user表清数据++++++++++++++++++++++++++++++++++++++++++++
    #con = pymysql.connect(host='192.168.1.230', port=3306, user='root', password='123456', db="user", charset='utf8mb4')
    con = db.dbuser()
    cursor = con.cursor()
    # 实例化
    test = Mysql()
    # 建一张学生表 包含（id，name，age，sex）
    #test.create()
    # 增加四条数据
    #test.insert()
    #con.commit() # 提交
    # 查询表中sex为男的数据
    #test.select()
    #print(cursor.fetchall())
    # 删除id =3的数据
    uid17688911111 = config_read.configread(
        "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911111",
        "uid17688911111")
    uid17688911112 = config_read.configread(
        "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911112",
        "uid17688911112")
    uid17688911113 = config_read.configread(
        "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911113",
        "uid17688911113")
    uid17688911114 = config_read.configread(
        "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911114",
        "uid17688911114")
    uid17688911115 = config_read.configread(
        "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911115",
        "uid17688911115")
    uid17688911116 = config_read.configread(
        "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911116",
        "uid17688911116")
    uid17688911117 = config_read.configread(
        "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911117",
        "uid17688911117")
    uid17688911118 = config_read.configread(
        "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911118",
        "uid17688911118")
    uid17688911119 = config_read.configread(
        "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911119",
        "uid17688911119")
    uid17688911120 = config_read.configread(
        "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911120",
        "uid17688911120")


    value = ['tb_user', uid17688911120]
    test.delete(value)
    #cursor.excute("delete from %s where id = %s", value)
    #test.delete("delete from %s where id = %s", value)
    #c.execute('select balance,freezing_balance,total_price from tb_user_coin where user_id  = %s and coin_id = %s',
    #          (buyid, buysymbolId))
    con.commit() # 提交
    # 将sex为女的，修改为男
    #test.updata()
    #con.commit() # 提交

    #test.delete_table()
    cursor.close()