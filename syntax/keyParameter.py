# -*- coding: utf8 -*-
# FileName:keyParameter.py


def fn(a, b, c=1, d=2):
  print 'a is', a,\
      'b is', b,\
      'c is', c,\
      'd is', d

fn(1, 2)
fn(a=2, b=4)
fn(a=1, b=3, c=4)
