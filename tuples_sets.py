# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 =  tuple(('Apples', 'Oranges', 'Lemon'))

# Trailing comma is needed if just one variable exists in the tuple
# Otherwise, it will be just a str
fruits2 = ('Apple', )

# print(fruits2, type(fruits2))

# Get value
# print(fruits[1])

# Can't change value
# fruits[0] = 'Melon'

# Delete tuple
del fruits2

# Get the length of the tuple

# print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create a set
fruits_set = {'Apples', 'Oranges', 'Melon'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Bananas')

# Remove form set
fruits_set.remove('Apples')

# Add duplicate > not gonna add it twice
fruits_set.add('Melon')

# Clear set > empty set
# fruits_set.clear()



# # Delete
# del fruits_set

print(fruits_set)