# coding=utf8
#!/usr/bin/python


class Parent:
  parentAttr = 100

  def __init__(self):
    print "Call parent init."

  def parentMethod(sef):
    print "Call parent method."

  def setAttr(self, attr):
    Parent.parentAttr = attr

  def getAttr(self):
    print "ParentAttr: ", Parent.parentAttr


class Child(Parent):

  def __init__(self):
    print "Call child init."

  def childMethod(self):
    print "Call child method."


c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(2000)
c.getAttr()
p = Parent()

print issubclass(Child, Parent)
print isinstance(c, Child)
print isinstance(c, Parent)
print isinstance(p, Parent)
print isinstance(p, Child)
