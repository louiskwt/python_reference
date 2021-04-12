# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Similar to objects in JS
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# create Dict 
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Constructor way
# person2 = dict(first_name="Sara", last_name="Williams")

# Get value -  [ ] notation
print(person['first_name'])

print(person.get('last_name'))

# Add key value
person['phone'] = '2334 1600'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# print(person)

# copy a dictionary
person2 = person.copy()
person2['city'] = 'Boston'

# print(person2)

# Remove item
del(person['age'])
person.pop('phone')

# Clear dictionary
person.clear()

# Get lengths
print(len(person2))

# print(person)

# print(person, type(person))

# List of dictionaries

people = [
    {'name': 'Ikura', 'age': 20},
    {'name': 'Ayase', 'age': 20}
]

print(people[0]['name'])