'''
using dictionary
'''

dic = {
    "ALLEN": "Liujiangbei@126.com",
    "SB": "SB@126.com",
    "NB": "NB@126.com"
}

print 'The length of dic is %d' % len(dic)
print "ALLEN's address is %s" % dic["ALLEN"]

dic["SX"] = "SX@126.com"  # Add a key/value pair

del dic["NB"]  # Delete a key/value pair

for key, value in dic.items():  # loop
  print 'Contact %s at %s' % (key, value)
