# -*- coding: cp936 -*-
#FileName��if.py
number = 23
guess = int(raw_input('Enter a number�� '))
if guess == number:
    print '��ϲ�㣬����ˣ�'
    print '����û�н���Ŷ��'
elif guess > number:
    print '����һ��㣬�������ͣ�'
else:
    print 'С��һ��㣬�������ͣ�'
print '������ֻ����һ��'
