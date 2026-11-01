import random
import string

letters = string.ascii_letters
numbers = string.digits

characters = letters + numbers

password = ""

length = int(input("Enter password length: "))

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)