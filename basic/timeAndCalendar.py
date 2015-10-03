# coding=utf8
#!/usr/bin/python

import time

ticks = time.time()
print ticks
print time.localtime(ticks)
print time.asctime(time.localtime(ticks))

# 返回当前CPU的时间
print time.clock()



# print type(calendar)
