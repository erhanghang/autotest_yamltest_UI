#-*- coding:utf-8 -*-
#author:yupeng
'''
python连接数据库，必要时使用数据库取数据作为测试数据，或做断言验证
'''
import pymysql
from common.conf.readconfig import ReadConfig

readconfig = ReadConfig()

class mysql_test():
    def __init__(self):
        '''数据库连接信息'''
        self.connection = pymysql.connect(
            host=readconfig.get_db('host'),
            port=readconfig.get_db('port'),
            user=readconfig.get_db('username'),
            password=readconfig.get_db('password'),
            db=readconfig.get_db('database'),
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor   #select出的结果是以dict格式输出的，不设置的话默认为tuple格式
        )
        #创建数据库游标
        self.cursor = self.connection.cursor()

    def select_sql(self,sql):
        '''执行sql'''
        try:
            self.cursor.execute(sql)
            #self.connection.commit()#提交到数据库中执行   （select语句貌似不需要提交就可以执行）
            result=self.cursor.fetchone()  #fetchall()取所有值返回的是一个list嵌套字典，fetchone()取一个值，返回一个字典
            return result
        except:
            return "Error: sql execution failure"
        finally:
            #关闭数据库
            self.connection.close()

    def execute_sql(self,sql):
        '''执行sql'''
        try:
            self.cursor.execute(sql)
            self.connection.commit()#提交到数据库中执行
            return 'sql执行成功'
        except:
            self.connection.rollback()  #发生错误是回滚
            return "Error: sql execution failure"
        finally:
            #关闭数据库
            self.connection.close()

if __name__ == '__main__':
    # sql_test=mysql_test()
    ss='小黑'
    #新增sql
    insert_sql="INSERT INTO `yupeng`.`student` (student_name) VALUES ('{}');".format(ss)
    print(insert_sql)
    # insert_result=sql_test.execute_sql(insert_sql)
    # print(insert_result)
    # assert '成功' in insert_result
    # #更新sql
    # undate_sql="UPDATE `yupeng`.`student` set student_name='小白' WHERE student_name='小黑';"
    # update_result=sql_test.execute_sql(undate_sql)
    # print(update_result)
    # #查询sql
    # select_sql="SELECT * FROM `yupeng`.`student` where student_name='小黑';"
    # select_result=sql_test.select_sql(select_sql)
    # assert select_result[0]['student_name']=='小黑'
    # #删除sql
    # delete_sql="DELETE FROM `yupeng`.`student` where student_name='小白';"
    # delete_result=sql_test.execute_sql(delete_sql)
    # print(delete_result)