# coding=utf8
#!/usr/bin/python

import string

# 原始字符串
print r"\\\n\n\n"

# format string
print "My name is %s and weight is %d kg!" % ('Zara', 21)

strs = "http://www.baidu.com"
print strs.encode()
print strs.decode()

# 如果string中只包含数字则返回True
print "123".isdigit()

# join
strs = "||"
array = ("12", "23", "jsd")
array2 = ["12", "34", "56"]

print strs.join(array)
print strs.join(array2)
