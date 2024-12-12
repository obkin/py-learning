a = input("Enter a: ")
b = input("Enter b: ")

# print(type(a))
# print(type(b))

a = int(a) # makes integer
b = int(b) # makes float

if a > b:
    print(f"{a} is greater than {b}")
elif a == b:
    print(f"{b} is equal {a}")
else:
    print(f"{b} is greater than {a}")

sum = a + b

print(f"The sum of {a} and {b} is: {sum}")