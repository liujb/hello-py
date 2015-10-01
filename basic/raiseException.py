#FileName:raiseException.py

class DefinedException(Exception):
    def __init__(self,length,least):
        Exception.__init__(self)
        self.length = length
        self.least = least

try:
    s = raw_input('Enter something-->')
    if(len(s) < 3):
        raise DefinedException(len(s),3)
        #raise EOFError
    else:
        pass
except EOFError:
    print 'Why did you do an EOF on me.'
except DefinedException, x:
    print 'DefinedException: The input was of length %d \
was exception at least %d' % (x.length, x.least)
else:
    print 'No exception was raised.'
