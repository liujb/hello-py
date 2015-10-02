# -*- coding: cp936 -*-
#FileName:classAndObjectMethod.py
#Description:类和对象的方法

class MyClass:
    flag = 0

    def __init__(self,name):    #构造函数
        self.name = name
        print 'init %s' % self.name
        MyClass.flag += 1

    def __del__(self):  #类似于C#里的析构函数
        print '%s says bye' % self.name
        MyClass.flag -= 1
        
        if MyClass.flag == 0:
            print '我是最后一个啦！'
        else:
            print '还有%d个！'% MyClass.flag

    def sayHi(self):    #实例方法
        print 'Hi,my name is ',self.name

    def outputFlag(self):   #实例方法
        print 'Flag is %d' % MyClass.flag

c = MyClass('C1')
c.sayHi()
c.outputFlag()

c2 = MyClass('C2')
c2.sayHi()
c2.outputFlag()
