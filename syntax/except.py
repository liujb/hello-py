# -*- coding: utf8 -*-

import sys

try:
  s = raw_input('Enter something')
except EOFError:
  print 'Why did you do an EOF on me.'
except:
  print '发生了未知异常'

print 'Done'