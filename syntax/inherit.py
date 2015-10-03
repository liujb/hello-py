# -*- coding: utf8 -*-
# FileName：inherit.py


class Base:

  def __init__(self, name, age):
    self.name = name
    self.age = age
    print 'init a object name:%s, age:%s' % (self.name, self.age)

  def tell(self):
    print 'Hi,boys and girls \
My name is %s, age is %s' % (self.name, self.age)


class Son(Base):

  def __init__(self, name, age, score):
    Base.__init__(self, name, age)
    self.score = score

  def tell(self):
    print 'Hi,My name is %s,age is %s ,I am got %d' % (
        self.name, self.age, self.score)

b = Base('ALLEN', 24)
# b.tell()

s = Son("Son-ALLEN", 6, 100)
# s.tell()

member = [b, s]
for item in member:
  item.tell()
