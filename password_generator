# Unsecure Password Generator

import random
import string

letters = string.ascii_letters
numbers = '0123456789'
special_characters = '!@#$%^&*+-_'

all_characters = letters + numbers + special_characters

length = int(input("How many characters would you like the password to have: "))
password = ''

for i in range(length):
    idx = random.randint(0, len(all_characters)-1)
    password = password + str(all_characters[idx])

print(password)
