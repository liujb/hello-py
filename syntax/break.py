'''
using break
'''
while True:
  INPUT = raw_input("Plz enter a world ")

  if INPUT == "quit":
    print 'You have quitted.'
    break
  else:
    print 'Plz enter again'

  print 'The length of word you are entered is', len(INPUT)

else:
  print 'Plz enter again'
