# coding=utf8
#!/usr/bin/python

a = 30
b = 30

if(a is b):
  print a, "is", b
else:
  print a, "not is", b

if(id(a) == id(b)):
  print a, b, "have the same identity"
else:
  print a, b, "have different indentity"
