# -*- coding: cp936 -*-
#FileName:series.py
#Description:序列
lst = ["AAA","BBB","CCC","DDD"]
for item in lst:
    print item
print '\n',lst[-1] #-1表示序列的最后一个元素
print lst[-2] #-2表示序列的倒数第二个元素

print lst[1:3]
print lst[2:]
print lst[1:-1]
print lst[:]

name = "ALLLENEN"
print name[1:3]
print name[2:]
print name[1:-1]
print name[:]
