# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core module

# Importing the whole thing
# import datetime

# Importhing just the date from datetime and then you can use it 
from datetime import date
from time import time

# Pip module
from camelcase import CamelCase

# Import custom module
from validator import validate_email

today = date.today()

timestamp = time()

c = CamelCase()

# print(c.hump('hello world'))

email = 'test#test.com'

if validate_email(email):
    print('Email is valid')
else:
    print('Not valid')