# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Ikura'
age = str(20)

# Concatenate
# print('Hello, my name is ' + name + ' and I am ' + age)


# String Formatting

# Arguments by position
# print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-string
# print(f'Hello my name is {name} and I am {age}')

# String Methods
s = 'hello world'

# capitalise string
print(s.capitalize())

# Turn it into upper case
print(s.upper())

# Length
print(len(s))

# count 
sub = 'hello'

print(s.count(sub))

# start and end with  > return boolean
print(s.startswith('h'))  
print(s.endswith('d'))

# split into a list( aka an array )
print(s.split())

# find
print(s.find('l'))

# Is alphanumeric
print(s.isalnum())

# Is alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())