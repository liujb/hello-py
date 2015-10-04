#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "", "test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

sql = """INSERT INTO EMPLOYEE(name,
         age)
         VALUES ('liujiangbei', 24)"""
try:
  cursor.execute(sql)
  db.commit()
except:
  db.rollback()


db.close()
