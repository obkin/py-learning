# You don't have to set type of variable (auto setting) and you can change the type later:
name = "Yarik" #str
age = 21 # int

print(name) # Yarik
print(age) # 21

print(type(name)) #str
print(type(age)) #int


# You can cast types of variables:
x = 5
x = str(5) # str: "5"

y = 3
y = int(3) # int: 3

z = 7
z = float(7) # float: 7.0

print(x) # "5"
print(y) # 3
print(z) # 7.0

print(type(x)) # str
print(type(y)) # int
print(type(z)) # float


# You can use either double or single quotes, no difference:
surname = "Hudz"
city = 'Ternopil'

print(surname)
print(city)


# Variable names are case-sensitive:
a = 123
A = 321

print(a)
print(A)