# coding=utf8
#!/usr/bin/python

i = 2
while(i < 1000):
  j = 2
  while (j <= (i/j)):
    if not(i % j):
      break
    j = j+1
  if(j > i/j):
    print i, "是素数"
  i = i+1

print "Goodbye"
