# -*- coding: cp936 -*-
#FileName:while.py
number = 23
flag = True
while flag:
    guess = int(raw_input('Plz Enter a number: '))
    if guess == number:
        print '��ϲ�㣬�¶���'
        flag = False # This cause can stop the while loop
    elif guess<number:
        print 'С��һ��㣬��������.'
    else:
        print '����һ��㣬��������.'
else:
    print 'While loop is stoped!'
