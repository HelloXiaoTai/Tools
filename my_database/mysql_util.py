# -*- coding: utf-8 -*-
import pymysql


class Mysql(object):

    def __init__(self, host="127.0.0.1", port=3306, user="root", password="", database=None, charset="utf8",
                 cursor_type=pymysql.cursors.DictCursor):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.cursor_type = cursor_type
        # 连接数据库
        self.connect()

    def connect(self):
        # 创建连接
        self.con = pymysql.connect(host=self.host,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database,
                                   charset=self.charset,
                                   port=self.port)
        # 创建游标
        self.cursor = self.con.cursor(cursor=self.cursor_type)

    def fetchall(self, sql, args=None):
        """以字典格式返回查询结果，用args=None防止sql注入"""
        try:
            # 使用游标发送sql
            self.cursor.execute(sql, args)
            # 获取结果
            return self.cursor.fetchall()
        except Exception as err:
            print(f"执行出错了，错误信息：{err}")

    def execute(self, sql, args=None):
        """执行增/删/改/查操作,返回受影响行数
               :param str sql: Query to execute.

               :param args: parameters used with query. (optional)
               :type args: tuple, list or dict(用args=None防止sql注入)

               :return: Number of affected rows
               :rtype: int

               If args is a list or tuple, %s can be used as a placeholder in the query.
               If args is a dict, %(keyname)s can be used as a placeholder in the query.
        """
        try:
            # 开启事务
            self.con.begin()
            # 使用游标发送sql指令
            num = self.cursor.execute(sql, args)  # 获取受影响行数
        except Exception as err:
            print(f"执行出错了，错误信息：{err}")
            self.con.rollback()
        else:
            self.con.commit()
            # 返回受影响的行数
            return num

    def __del__(self):
        self.cursor.close()
        self.con.close()


if __name__ == '__main__':
    # 指定游标返回的数据类型
    # 字典：cursor_type=pymysql.cursors.DictCursor
    # 元组：cursor_type=pymysql.cursors.Cursor
    db = Mysql(database='woniubook')
    # 查
    result = db.fetchall('select * from customer where age=%s and address=%s', args=(5, '成都'))
    print(result)
    result = db.fetchall('select * from customer where address=%(addr)s', args={'addr': '重庆'})
    print(result)
    # 删
    result=db.execute('delete from customer where username=%s',args=('杨小宁'))
    print(result)
    #改
    result=db.execute('update customer set age=%s WHERE username=%s', args=(20, '靳小杰'))
    print(result)
    #增
    result=db.execute('insert into customer values(15,"周大名","12312341234","广州",18);')
    print(result)
