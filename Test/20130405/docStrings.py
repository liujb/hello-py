#FileName:func_doc.py
def func(x,y):
    '''Print the maximun of two numbers. 

    The two values must be integers.'''
    x = int(x)
    y = int(y)
    if (x > y):
        print x, 'is the maximun'
    else:
        print y, 'is the maximun'

func(3,4)
print func.__doc__
