#variables
i = 0
lowercase = False
uppercase = False
symbol = False
number = False
total = 0

#password checker

#password input and length
password = input("Enter a password: ")
length = len(password)

#validation check
while 6 > length or length > 12:
    if 6 > length:
        print("Password is too short!")
        password = input("Enter a password: ")
        length = len(password)
    else:
        print("Password is too long!")
        password = input("Enter a password: ")
        length = len(password)
print("Password is accapetable!")

#strength check
while i < length:
    if password[i].isnumeric() == True:
        number = True
    elif password[i].isalpha() == True:
        if password[i].isupper():
            uppercase = True
        else:
            lowercase = True
    elif password[i].isalnum() == False: 
        symbol = True
    else:
        print("i hate this program")
    i = i + 1

if lowercase == True:
    total = total + 1
if uppercase == True:
    total = total + 1
if symbol == True:
    total = total + 1
if number == True:
    total = total + 1

if total == 1:
    print("Password is WEAK")
elif total == 2:
    print("Password is MEDIUM")
elif total >= 3:
    print("Password is STRONG")
elif total == 0:
    print("no clue what happened here")