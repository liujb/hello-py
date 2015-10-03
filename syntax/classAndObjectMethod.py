'''
define class and
'''
# -*- coding: utf8 -*-
# FileName:classAndObjectMethod.py
# Description: class and object method


class MyClass:
  flag = 0

  def __init__(self, name):
    self.name = name
    print 'init %s' % self.name
    MyClass.flag += 1

  def __del__(self):
    print '%s says bye' % self.name
    MyClass.flag -= 1

    if MyClass.flag == 0:
      print 'I am last one'
    else:
      print 'Have %d ' % MyClass.flag

  def sayHi(self):
    print 'Hi, my name is ', self.name

  def outputFlag(self):
    print 'Flag is %d' % MyClass.flag

c = MyClass('C1')
c.sayHi()
c.outputFlag()

c2 = MyClass('C2')
c2.sayHi()
c2.outputFlag()
