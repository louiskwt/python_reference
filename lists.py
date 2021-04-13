# A List is a collection which is ordered and changeable. Allows duplicate members.

# create a list  (equilvant to array)
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Watermelon', 'Strawberries']

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits[3])

# Get the link of the list
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove("Apples")

# Insert into position
fruits.insert(2, 'Lemon')

# Remove from certain position
fruits.pop(2)

# Reverse the list
fruits.reverse()

# Sort list ( in alphabetical order)
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

# Change value
fruits[0] = 'Blueberries'

print(fruits)