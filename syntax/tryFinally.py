# FileName:tryFinally.py

import time

try:
  f = file('poe.txt')
  while True:
    line = f.readline()
    if len(line) == 0:
      break
    time.sleep(2)
    print line
finally:
  # f.close()
  print 'exception....'
