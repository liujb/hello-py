# -*- coding: cp936 -*-
#FileName：if.py
number = 23
guess = int(raw_input('Enter a number： '))
if guess == number:
    print '恭喜你，答对了！'
    print '但是没有奖励哦！'
elif guess > number:
    print '大了一点点，继续加油！'
else:
    print '小了一点点，继续加油！'
print '噢啦，只能试一次'
