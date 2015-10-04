# coding=utf8
#!/usr/bin/python

import MySQLdb

conf = {"ip": "localhost", "port": 3306,
        "user": "root", "pwd": "", "db": "data"}

# connect database
db = MySQLdb.connect(conf["ip"], conf["user"], conf["pwd"], conf["db"])

# create table sql
createTableSql = """CREATE TABLE EMPLOYEE (
        FIRST_NAME  CHAR(20) NOT NULL,
        LAST_NAME  CHAR(20),
        AGE INT,  
        SEX CHAR(1),
        INCOME FLOAT )"""
cursor = db.cursor()

# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
cursor.execute(createTableSql)

db.close()
