# You can check the type of the variable:
x = 5
y = 'hello'
z = True

print(type(x)) # int
print(type(y)) # str
print(type(z)) # bool


# In Python, the data type is set when you assign a value to a variable:
a = 5 # int
b = 'hi' # str
c = 20.5 # float
d = 1j # complex

print(a)
print(b)
print(c)
print(d)


# Setting the data type:
person = {
    "name": "John",
    "age": 36,
    "country": "Norway",
    "married": True,
    "children": False,
    "penis_length": 17.5,
    "ex_girls": ['Julia', 'Rita', 'Anastasiya'],
    "parents": ('Martina Navratilova', 'Huan Tokyo'),
}

# How to interact with dict type:
print(person("name")) # John
print(person.get("name")) # John

person["name"] = "Robert" # You can change the value of the string
person["ex_girls"] = ['Kolya', 'Vasya', 'Stas'] # You can change values of the list

# About tuples:
person['parents'][0] = ("Stefa Navratilova", "Huan Tokyo")
# person['parents'][0] = 'Stefa' # Error! - you can change the whole tuple, but you can't change it's values


# How range type works:
age = 32
lived_years = range(age),

print(lived_years) # (0, 32)
