# Python has a set of built-in methods that you can use of strings:
text = 'Hello, World!'


# Upper Case:
print(text.upper()) # 'HELLO, WORLD!'


# Lower Case:
print(text.lower()) # 'hello, world!'


# Remove Whitespace (in the beginnig or/and in the end of the string):
text2 = "  This is a very bad text  "
print(text2.strip()) # 'This is a very bad text' (without spaces in the beginning and in the end)


# Replace string or some chatacters:
text3 = "Hello, Mark!"
print(text3.replace("H", "K")) # "Kello, Mark!"
print(text3.replace("Hello", "Fuck off")) # "Fuck off, Mark"


# Split the string:
text4 = "I like bananas, but I don't like mangoes"
print(text4.split()) # ['I', 'like', 'bananas,', 'but', 'I', "don't", 'like', 'mangoes']
print(text4.split(',')) # ['I like bananas', " but I don't like mangoes"]
