# coding=utf8
#!/usr/bin/python

import random
import math

num = "123"

# str to number
print int(num)
print long(num)
print float(num)
print complex(num)

# number to hex（16进制） and oct（8进制）
print hex(int(num))
print oct(int(num))

# 将字符转换成他的整数值
print ord("A")

# 将整数转换成字符
print chr(11)

# 将整数转换成Unicode字符
print unichr(12)

# 生成随机数
print random.random()
print random.uniform(10, 20)

# 使用math.sin
print math.sin(math.pi/6)
print math.cos(math.radians(30))


