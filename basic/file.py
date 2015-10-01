# -*- coding: cp936 -*-
#FileName:file.py

content = '''\
Let me fuck you！！！！
Oh yeah,oh yeah.
'''

f = file('test.txt', 'w')
#open for writing,if not exists the file, program will create it.
f.write(content)    #write text to file
f.close()   #close the file stream

f = file('test.txt')    #only open the file
while True:
    line = f.readline() 
    if len(line) ==0:   #last line break the loop
        break;
    print line
f.close()
#code by ALLEN 
