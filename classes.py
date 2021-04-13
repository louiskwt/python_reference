# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create Class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    # Methods
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    def has_birthday(self):
        self.age += 1
    
# Init user object
ikura = User('Ikuta Rira', 'ikura@gamil.com', 20)

ikura.has_birthday()
print(ikura.greeting())

# Extend class
class Customer(User):
     # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    # Method
    def set_balance(self, balance):
        self.balance = balance
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# Init customer object
lisa = Customer('Lisa', 'lisa@gamil.com', 26)

lisa.set_balance(500)

print(lisa.greeting())