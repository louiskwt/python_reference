# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

#sample json
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])

# Turn a dictionary into json
car = {'make': 'Toyota', 'model': 'Puris', 'year': 2007}

carJSON = json.dumps(car)

# Print in JSON format with " "
print(carJSON)