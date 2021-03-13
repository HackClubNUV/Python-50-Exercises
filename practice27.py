"""
The random password generator, utilises the string library,
and the random library to generate a password with the mixture of letters,digits & special characters
"""
#Importing Libraries
import string
from random import *

#Defining all possible characters for the password
password_available_characters = string.ascii_letters + string.punctuation  + string.digits

#The password generator module
password_generator =  "".join(choice(password_available_characters) for x in range(randint(8, 32)))

#Printing the generated password
print(password)
