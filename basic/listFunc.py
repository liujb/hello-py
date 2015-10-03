# coding=utf8
#!/usr/bin/python

list1 = ["allen", "john", 24, 26]
list2 = ['shaPbi', "sds"]

# 更新列表中的元素
list1[0] = "liujiangbei"
print list1

# 并不能更改索引️增加长度
# list1[4]= "shabi"

# 删除列表元素
del list1[0]
print list1

# get list length
print len(list1)

# concat
list3 = list1+list2
print list3

# repeat
print list3*3

# in
print 24 in list3

# loop
for i in list3:
  print i

# max and min
print max(list1)
print min(list3)

# tuple to list
seq = ("12", "34")
list4 = list(seq)
print list4

# other list func
# list.reverse()
# list.sort(func)
# list.remove(obj)
# list.insert(index,obj)
# list.append(obj)
# list.count(obj) 某元素在列表中的出现次数
# list.extend(seq)
# list.pop() # 默认是最后一个，返回改制