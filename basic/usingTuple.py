# -*- coding: cp936 -*-
#FileName:usingTuple.py
zoo = ("wolf", "elephant", "penguin")
print 'Number of animals in the zoo is', len(zoo)

new_zoo = ("monkey", "dolphin", zoo)
print 'Number of animals in the new zoo is', len(new_zoo)
print "All animals in zhe new zoo are", new_zoo
print 'Animals brought from old zoo are', new_zoo[2]
print "Last animal brought from old zoo is", new_zoo[2][2]

#Ԫ��ͨ�����ڴ�ӡ�����
age = 23
name = "ALLEN"

print '\n%s is %d years old' % (name,age)
print "Why is %s playing with that Python?" % name