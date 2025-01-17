str1 = 'cherry'
text = """"
    I'd like to return to the past, when you are a child and you don't have to care about nothing... 
    Just about the homework, sometimes.
"""

for x in str1:
    print(x)

print("Length:", len(text))
print("child" in text) # True
print("chil" in text) # True
print("cat" in text) # False

if "child" in text:
    print("Yes. there's a 'child' ")
else:
    print("No, there's no any 'child'")


print('cat' not in text) # True
print('child' not in text) # False

if 'cat' not in text:
    print("There's no any cat in 'text'")
else:
    print("Yes. There's a cat in 'text'")
    

# Castings:
print(int('1')) # 1
print(float(1)) # 1.0
print(str(13)) # 13