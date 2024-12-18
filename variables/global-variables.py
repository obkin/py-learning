# We have global and local variables in Python:
x = 'awesome' # global variabe (you can use it everywhere)

def myfunc():
    x = 'fantastic' # local variable (you can use it inly inside this function)
    print("Python is " + x)


print("Python is " + x) # Python is awesome
myfunc() # Python is fantastic


# You can create global variables insude functions, too:
def func():
    global num
    num = 10

    print(num)

func() # 10
print(num) # 10


# You can also change value of gloval variable inside of function:
def changeValue():
    global x
    x = 'AWESOME'

    print(x)

changeValue() # AWESOME