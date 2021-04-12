# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

'''
Hi
'''

# x = 1           # int
# y = 2.5         # float
# name = 'Ikura'  #str
# is_cool = True  # bool (first letter must be capital)

x, y, name, is_cool = (1, 2.5, 'Ikura', True)

print("Hello ", name)
print(x + y)

# Casting
x = str(x)
y = int(y)

print(type(x))
print(type(y), y)