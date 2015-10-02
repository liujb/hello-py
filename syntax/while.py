# -*- coding: cp936 -*-
#FileName:while.py
number = 23
flag = True
while flag:
    guess = int(raw_input('Plz Enter a number: '))
    if guess == number:
        print '恭喜你，猜对了'
        flag = False # This cause can stop the while loop
    elif guess<number:
        print '小了一点点，继续加油.'
    else:
        print '大了一点点，继续加油.'
else:
    print 'While loop is stoped!'
