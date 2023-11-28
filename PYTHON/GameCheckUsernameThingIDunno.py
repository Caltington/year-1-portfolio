def UsernameCheck():
    Integer = 0
    Capital = 0
    for x in username:
        if x.isnumeric() == True:
            Integer = 1
        else:
            Integer + 0

        if x.isupper() == True:
            Capital = 1
        else:
            Capital + 0

    if Capital >= 1 and Integer >= 1:
        with open("GameChoice.csv", "r") as file:
            line = file.readline()
            while(line):
                data=line.split(",")
                if data[0] == username:
                    print("Username is taken!")
                    Start()
                else:
                    print("Username is valid!")
                    Option()
    else:
        print("Invalid username")
        Start()

def StoreData():
    with open("GameChoice.csv", "a") as file:
        file.write(username + "," + option + "\n")
    print("Data stored")
    Start()

def Option():
    global option
    print("Select Chess, Billiards or Darts!")
    OptionInput = input("1. Chess\n2. Billiards\n3. Darts\n")
    if OptionInput == "1":
        print("Chess was selected")
        option = "chess"
    elif OptionInput == "2":
        print("Billiards was selected")
        option = "billiards"
    elif OptionInput == "3":
        print("Darts was selected")
        option = "darts"
    else:
        print("Value was not 1, 2 or 3!")
        print("Try again!")
        Option()
    StoreData()

def Start():
    global username
    global OptionInput
    username = input("Enter a username: ")
    UsernameCheck()    
Start()