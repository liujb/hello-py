#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "", "test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE"

try:
  cursor.execute(sql)
  results = cursor.fetchall()

  for row in results:
    id = row[0]
    name = row[1]
    age = row[2]

    print "id=%d, name=%s, age=%d" % \
        (id, name, age)
except:
  print "Error: unable to fecth data"

db.close()
