number = 23
guess = int(raw_input('Enter a number: '))

if guess == number:
  print 'success.'
elif guess > number:
  print 'gather.'
else:
  print 'less'
print 'plz retry'
