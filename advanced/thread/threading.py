# coding=utf8
#!/usr/bin/python

import threading
import time

exitFlag = 0

class myThread (threading.Thread):

  def __init__(self, threadId, name, counter):
    threading.Thread.__init__(self)
    self.threadID = threadId
    self.name = name
    self.counter = counter

  def run(self):
    print "Starting " + self.name
    printTime(self.name, self.counter, 5)
    print "Exiting "+self.name


def printTime(threadName, counter, delay):
  while counter:
    if exitFlag:
      thread.exit()
    time.sleep(delay)
    print "%s: %s" % (threadName, time.ctime(time.time()))
    counter -= 1


# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启线程
thread1.start()
thread2.start()

print "Exiting Main Thread"