# Python has functions for creating, reading, updating, and deleting files.
# open a file
myFile = open('myfile.txt', 'w')

# get some info
print('name: ', myFile.name)
print('Is close: ', myFile.closed)
print('Opening mode: ', myFile.mode)

# Write to file
myFile.write('I love python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file - w will overwrite the file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like React')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)
