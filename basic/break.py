'''
hello
'''
while True:
    INPUT_NAME = raw_input("Plz enter a world ")
    if INPUT_NAME == "quit":
        print 'You have quitted.'
        break
    else:
        print 'Plz enter again'
    print 'The length of word you are entered is', len(INPUT_NAME)
else:
    print 'Plz enter again'
