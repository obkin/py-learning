# String in python may be surrounded by single or double quotes:
str1 = 'hello'
str2 = "hello"


# We can also wrap strings:
str3 = '''
    This is a multi-line string.
    You can write across multiple lines.
'''

str4 = """
    This is also a multi-line string.
    You can write across multiple lines.
"""

print(str3)
print(str4)


# We can use quotes inside quotes, just use another type of quotes:
str5 = "My name's - Yarok"
str6 = 'I"m a nodejs dev'

str7 = "'bullshit' - is an informal way to express your unpleasant opinion"
str8 = 'Everybody knows, "War" - it"s bad'


# Like in many languages, strings in python - are arrays, so we can interract with them like with arrays:
str9 = "hello, dude"
print(str9[0]) # h
print(str9[1]) # e
print(str9[2]) # l


# Since strings are arrays, we can loop through the characters in string:
for x in "banana":
    print(x) # b a n a n a


# And we can find out the length of the string:
str10 = 'my length is 15'
print(len(str10)) # 15


# We can check if there a certain character or phrase in the string:
str11 = "I didn't like my teachers at college"
print("teacher" in str11) # True
print("teache" in str11) # True
print("teach" in str11) # True
print("test" in str11) # False

# We can also use it in 'if' statement:
if "teacher" in str11:
    print('Yes, "teacher" is present.')

# Check if 'not':
print("teacher" not in str11) # False
print("Teacher" not in str11) # True
print("test" not in str11) # True

# We can also use it in 'if' statement:
if "test" not in str11:
    print('There is no "test" in str11')
