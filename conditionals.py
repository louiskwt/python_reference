# If/ Else conditions are used to decide to do something based on something being true or false

x = 30
y = 3


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# if x > y:
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{y} is greater than {x}')

# if x > y:
#     print(f'{x} is greater than {y}')
# elif x == y:
#     print(f'{x} is euqal {y}')
# else:
#     print(f'{x} is less than {y}')

# Nested if
# if x > 2:
#     if x <= 10:
#         print(f'{x} is greater than 2 and less than or equal to 10')

# Logical operators (and, or, not) - Used to combine conditional statements
# if x > 2 and x <= 10:
#     print(f'{x} is greater than 2 and less than or equal to 10')
    
# if x > 2 or x <= 10:
#     print(f'{x} is greater than 2 and less than or equal to 10')

# if not(x == y):
#     print(f'{x} is not equal to {y}')


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object
numbers = [1, 2, 3, 4, 5]

# in
# if x in numbers:
#     print(x in numbers)
    
# not in
# if y not in numbers:
#     print(y not in numbers)



# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x is y:
    print(x is y)
    
# is not
if x is not y:
    print(x is not y)
