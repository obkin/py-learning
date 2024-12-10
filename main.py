class User:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Sex: {self.age}"

user1 = User(name="Yaroslav", age=21, sex="Male")
user2 = User(name="Pidaras", age=24, sex="Male")

print(user1)
print(user2)