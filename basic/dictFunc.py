# coding=utf8
#!/usr/bin/python

dict = {"name": "liujiangbei", 2: "is 2B"}
dict["fucking"] = "you"

# get item
print dict
print dict.keys()
print dict.values()
print dict.get("name")
print dict["name"]

# check has key
print dict.has_key("name1")

# for
for i in dict.items():
  print i

#  删除元素或者整个字典
del dict["fucking"]
dict.clear()
print dict
