def HighScore():
    file = open("gamerscore.csv", "r")
    line = file.readline()
    while(line):
        data =line.split(",")
        score = int(data[1])
        if score>=7963:
            print("Handle: ",data[0])
        line=file.readline()
    file.close()

def LowScore():
    file = open("gamerscore.csv", "r")
    line = file.readline()
    while(line):
        data =line.split(",")
        score = int(data[1])
        if 6000>=score:
            print("Handle: ",data[0])
        line=file.readline()
    file.close()

def DataInput():
    file = open("gamerscore.csv", "r")
    line = file.readline()
    try:
        SearchScore = int(input("Please enter a Score: "))
    except:
        print("Please only enter numbers!")
        DataInput()

    while(line):
        data=line.split(",")
        score = data[1]
        if int(score) < SearchScore:
            print("Handle: ",data[0])
            print("Gamerscore ",data[1])
        line=file.readline()    

while True:
    choice = input("1. View scores of 7963 or above\n2. View scores of 6000 and below\n3. To search scores below a number")
    if choice == "1":
        HighScore()
    elif choice == "2":
        LowScore()
    elif choice == "3":
        DataInput()
    else:
        print("Please enter 1, 2 or 3! ")