# coding=utf8
#!/usr/bin/python


class JustCounter:
  __privateCount = 0  # private variable
  publicCount = 0  # public variable

  def count(self):
    self.__privateCount += 1
    self.publicCount += 1

    print self.__privateCount

counter = JustCounter()
counter.count()
counter.count()

print counter.publicCount
# print counter.__privateCount # 报错
# 另一访问私有变量的方法
print counter._JustCounter__privateCount
