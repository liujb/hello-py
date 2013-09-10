# -*- coding: cp936 -*-
#FileName:except.py
#简单的异常

import sys

try:
    s = raw_input('Enter something')
except EOFError:
    print 'Why did you do an EOF on me.'
    #sys.exit()  #exit the program
except:
    print '发生了未知异常'
print 'Done'
