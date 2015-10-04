# coding=utf8
#!/usr/bin/python


class Parent:

  def myMethod(self):
    print "call parent method."


class Child(Parent):

  def myMethod(self):
    print "call child method."


c = Child()
c.myMethod()


# 通用功能，可以在类中重写
# __init__ obj = className(args)
# __del__ dell obj
# __repr__ repr(obj)
# __str__ str(obj)
# __cmp__ cmp(obj, x)
