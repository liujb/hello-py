# -*- coding: utf8 -*-
# FileName:pickle.py

import cPickle as p

lstFile = 'file.txt'

lst = ['ALLEN', 'KOBE', 'JOH']
f = file(lstFile, 'w')  # 打开文件，若没有则创建文件

p.dump(lst, f)  # dump(转存，倾倒等意思) the object to a file
# 将对象序列化到文件内
f.close()

del lst

f = file(lstFile, 'r')  # 读取文件内容
storedList = p.load(f)  # load the object from file

print storedList
