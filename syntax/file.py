content = 'hello, nice to meet'

f = file('test.txt', 'w')

f.write(content)
f.close()

f = file('test.txt')  # only open the file
while True:
  line = f.readline()
  if len(line) == 0:  # last line break the loop
    break
  print line
f.close()
