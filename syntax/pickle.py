# -*- coding: cp936 -*-
#FileName:pickle.py

import cPickle as p
#import pickle as p

lstFile = 'file.txt'

lst = ['ALLEN','KOBE','JOH']
f = file(lstFile,'w')   #���ļ�����û���򴴽��ļ�
p.dump(lst,f)   #dump(ת�棬�㵹����˼) the object to a file
#���������л����ļ���
f.close()

del lst

f = file(lstFile,'r')   #��ȡ�ļ�����
storedList = p.load(f)  #load the object from file

print storedList
