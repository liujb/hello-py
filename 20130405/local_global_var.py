#FileName:local_global_Var.py

#local variable
def func(x):
    print 'Actual parameter of x is', x
    x = 2
    print 'Actual parameter of x have changed to', x 
x = 'String'
func(x)
print 'x is still', x

#global variable
def fn():
    global y
    print 'y is', y
    y = 3
    print 'Changed local y to', y
y = 50
fn()
print 'Value of y is', y
    

