# You can use print() to output variables:
x = "Python is awesome"
print(x) # Python is awesome


# You can output multiple variables separated by a commma or using + operator:
a = 'Python'
b = 'is'
c = 'awesome'

print(a, b, c) # Python is awesome
print(a + b + c) # Pythonisawesome


# For numbers, + operator works like a mathematical operator:
num1 = 5
num2 = 10

print(num1 + num2) # 15


# If you try to combine string and number variables into print, you'll get an error:
o = 2
j = "hello"

# print(o + j) # ERROR


# The best way to output multiple variables in the print() is to separate them with comma (works even with different types):
y = 4
t = "hello"

print(y, t) # 4 "hello"