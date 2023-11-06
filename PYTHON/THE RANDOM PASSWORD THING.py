import random
import string

length = random.randint(14, 16)
password = ""

while len(password) < length:
    choices = string.ascii_letters + string.digits + '!@#$%^&*()_'
    character = random.choice(choices)
    password = password + character

with open("passwords.txt", "a") as file:
    file.write(password + "\n")
    print(password, "was generated and added to the list!")