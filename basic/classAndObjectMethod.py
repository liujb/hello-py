# -*- coding: cp936 -*-
#FileName:classAndObjectMethod.py
#Description:��Ͷ���ķ���

class MyClass:
    flag = 0

    def __init__(self,name):    #���캯��
        self.name = name
        print 'init %s' % self.name
        MyClass.flag += 1

    def __del__(self):  #������C#�����������
        print '%s says bye' % self.name
        MyClass.flag -= 1
        
        if MyClass.flag == 0:
            print '�������һ������'
        else:
            print '����%d����'% MyClass.flag

    def sayHi(self):    #ʵ������
        print 'Hi,my name is ',self.name

    def outputFlag(self):   #ʵ������
        print 'Flag is %d' % MyClass.flag

c = MyClass('C1')
c.sayHi()
c.outputFlag()

c2 = MyClass('C2')
c2.sayHi()
c2.outputFlag()
