i = 0
password = "password123"
length = len(password)

while i < length:

    if password[i].isnumeric == True:
        number = 1
        print("number")
    elif password[i].isalpha == True:
        if password[i].isupper:
            uppercase = 1
            print("upper")
        else:
            lowercase = 1
            print("lower")
    elif password[i].isalnum == False: 
        symbol = 1
        print("symbol")
    else:
        print("i hate this program")
    i = i + 1
