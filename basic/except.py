# -*- coding: cp936 -*-
#FileName:except.py
#�򵥵��쳣

import sys

try:
    s = raw_input('Enter something')
except EOFError:
    print 'Why did you do an EOF on me.'
    #sys.exit()  #exit the program
except:
    print '������δ֪�쳣'
print 'Done'
