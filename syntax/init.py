# FileName:init.py


class MyClass:

  def __init__(self, name):
    self.name = name

  def instanceMethod(self):
    print 'Hi, %s let me fuck you.' % self.name

c = MyClass('ALLEN')
c.instanceMethod()
