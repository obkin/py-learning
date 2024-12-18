x = 'awesome'
def func():
    global x
    x = 'fantastic'

func()
print(x)