def add_grade():
    name = input("Enter the name of the student: ")
    date = input("Enter the date of test: ")
    test = input("Enter the name of the test: ")
    tutor = input("Enter the tutor that graded the test:")
    score = int(input("Enter the score of the student: "))
    grade = "N/A"
    while grade == "N/A":
        if score > 80 and 101 > score:
            grade = "A*"
        elif score > 70 and 81 > score:
            grade = "A"
        elif score > 60 and 71 > score:
            grade = "B"
        elif score > 50 and 61 > score:
            grade = "C"
        elif score > 40 and 51 > score:
            grade = "D"
        elif score > 0 and 41 > score:
            grade = "Fail"
        else:
            print("Scores can only be between 0 and 100!")
            add_grade()
    with open("GradeFiles.csv", "a") as file:
        file.write("\n" + name + "," + date + "," + test + "," + tutor + "," + str(score) + "," + grade)
    print(name + "'s grade is " + grade)
    run_program()

def read_grade():
    counter = 0
    name = input("Enter the name of the student's grade you wish to view: ")
    with open("GradeFiles.csv", "r") as file:
        line = file.readline()
        while(line):
            data=line.split(",")
            if data[0]==name:
                print(name + "'s grade for " + data[2] + " was "+ data[5] + " with a score of " + data[4] +". This was graded by " + data[3] + " at " + data[1])
                counter = 1
            line=file.readline()
        if counter == 0:
            print("No data found!")
    run_program()

def run_program():
    while True:
        print("Grade Database")
        choice = input("1. Add a grade\n2. Read grade\n3. Exit")
        if choice == "1":
            add_grade()
        elif choice == "2":
            read_grade()
        elif choice == "3":
            exit()
        else:
            print("Please only enter 1, 2 or 3!")

run_program()