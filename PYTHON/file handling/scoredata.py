import os

#decide what you want to do
print("Do you want to read, edit or delete a score? ")
choice = input("r, e, d")

if choice == "r":
    username = input("Enter the username of the score you wish to view: ")
    myfile = open(username + ".txt","r")
    print(myfile.read())
    myfile.close()
elif choice == "e":
    username = input("Enter the username of the socre you wish to edit: ")
    score = input("Enter the score you wish to add: ")
    myfile = open(username + ".txt", "w")
    myfile.write("score = " + score)
    myfile.close()
    print("Score successfully edited!")
elif choice == "d":
    username = input("Enter the username of the score you wish to delete: ")
    if os.path.exists(username + ".txt"):
        os.remove(username + ".txt")
        print("Score successfully deleted!")
    else:
        print("The score does not exist")
