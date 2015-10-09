# coding=utf8
#!/usr/bin/python

import demjson

# dictionary
dict = [{"abc": 123, "def": 234}, {"es": 12}]
print dict

# json encode
json = demjson.encode(dict)
print type(json)
print json

# json encode list
list = [12, 34, "124"]
print demjson.encode(list)

# json encode tuple
tuple = (12, 23, "45", "abcded")
print demjson.encode(tuple)

# json decode
txt = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
dict = demjson.decode(txt)
print type(dict)

# json encode dict
dict = {"abcd": "1234"}
print demjson.encode(dict)
