# -*- coding: cp936 -*-
#FileName break.py
while True:
    s = raw_input("Plz enter a world： ")
    if(s=='quit'):
        print 'You have quitted.'
        break
    else:
        print 'Plz enter again'
    print 'The length of word you are entered is', len(s)
else:
    print 'Plz enter again'
