# coding=utf8
#!/usr/bin/python

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"

# 元组要是只有一个元素时候，需要在后面添加逗号
tuple4 = (10,)

print tup3[1]

# 元组不允许修改
print tup1+tup2

# 元组中的元素不能删除，但是可以使用del来删除整个元组
del tup1
# print tup1

# len, in, for
print len(tup2)
print 3 in tup2
for i in tup2:
  print i