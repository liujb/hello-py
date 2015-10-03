# -*- coding: utf8 -*-
# FileName:return.py


def func(x, y):
  if(x > y):
    return x
  else:
    return y

x = func(5, 10)
print 'The big is', x

def func2():
  pass  # 表示一个空的语句块

func2()
