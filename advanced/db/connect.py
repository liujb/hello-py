# coding=utf8
#! /usr/bin/python

import MySQLdb

conf = {"ip": "localhost", "port": 3306,
        "user": "root", "pwd": "", "db": "data"}

# connect database
db = MySQLdb.connect(conf["ip"], conf["user"], conf["pwd"], conf["db"])

# 获取操作游标
cursor = db.cursor()

# 执行sql语句
sql = "SELECT VERSION()"
cursor.execute(sql)

# 获取一条记录
data = cursor.fetchone()

# 打印
print "Database version %s" % data


db.close()
