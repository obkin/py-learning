# There are 3 numeric types in Python:
a = 17 # int
b = 3.14 # float
c = 3j # complex


# We still can check the type of any numeric variable:
print(type(a)) # integer
print(type(b)) # float
print(type(c)) # complex


# Type int or integer:
x = 10
y = 4234234123
z = -123243


# Type float:
t = 1.10
p = 3.1
v = -35.59

# It can also be a scientific number with "e" to indicate the power of 10:
o = 10e3
i = 1e4
u = -35.59e100

print(o) # 10000.0
print(i) # 10000.0
print(u) # -3.559e+101


# Type complex:
r = 3+5j
e = 5j
w = -5j

print(r) # (3+5j)
print(e) # 5j
print(w) # (-0-5j)


# We can also convert numbers from one type to another:
age = 32
age_float = float(age) # 32.0

pi = 3.14
pi_int = int(pi) # 3

comp = complex(age) # (32+0j)

print(int(5.9)) # 5


# Random number:
# Python doesn't have a random function to generate a random number, but it has a built-in module:

import random
print(random.randrange(1, 100)) # 1-100
