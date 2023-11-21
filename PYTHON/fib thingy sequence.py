a = 1
b = 1
total = 0

amount = int(input("How many places do you wish to view? "))
x = 1
mylist = []
while amount+1 > x:
    number = a + b
    print(str(number))
    a = b
    b = number
    x = x + 1
    total = number + total

reverse = input("Do you wish to view this in reverse?\n1. Y 2. N ")
if reverse == "Y":
    x = 0
    a = 1
    b = 1
    while amount > x:
        number = a + b
        mylist.append(str(number))
        a = b
        b = number
        x = x + 1
    mylist.reverse()
    for y in mylist:
        print(y)

choice = input("Do you wish to view the total?\n1. Y 2. N ")
if choice == "Y":
    print("The total is " + str(total))