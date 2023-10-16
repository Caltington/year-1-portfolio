#made by callum the great
NameList = []
AmountList = []
NewAmountList = []
MeasurementList = []

#Function to create a recipe file
def create_recipe():
    recipe_name = input("Recipe name: ")
    try:
        recipe_people = input("Serving ammount: ")
        int(recipe_people)
    except ValueError:
        print("Please enter a number!")
        create_recipe()
    try:
        IngredientsRequired = int(input("Enter the number of ingredients required: "))
    except ValueError:
        print("Please enter a number!")
        create_recipe()
    IngredientsCreated = 0
    while IngredientsRequired > IngredientsCreated:
        IngredientName = input("Enter the name of the ingredient: ")
        try:
            IngredientAmount = int(input("Enter the amount of the ingredient: "))
        except ValueError:
            print("Please enter a number!")
        IngredientMeasurement = input("Enter the measurement of the ingredient: ")
        NameList.append(IngredientName)
        IngredientAmount = int(IngredientAmount) / int(recipe_people)
        print()
        AmountList.append(str(IngredientAmount))
        MeasurementList.append(IngredientMeasurement)
        IngredientsCreated = IngredientsCreated + 1
    myfile = open(recipe_name + "names.txt", "w")
    myfile.writelines("\n".join(NameList))
    myfile.close()
    myfile = open(recipe_name + "amounts.txt", "w")
    myfile.writelines("\n".join(AmountList))
    myfile.close()
    myfile = open(recipe_name + "measurements.txt", "w")
    myfile.writelines("\n".join(MeasurementList))
    myfile.close()

#Function to retrieve and display a recipe file
def use_recipe():
    try:
        file_name = input("File name: ")
        with open(file_name + "names.txt", "r") as file:
            NameList = [line.rstrip() for line in file]
        with open(file_name + "amounts.txt", "r") as file:
            AmountList = [line.rstrip() for line in file]
        with open(file_name + "measurements.txt", "r") as file:
            MeasurementList = [line.rstrip() for line in file]
        PeopleRequired = int(input("Enter the amount of people the recipe is for: "))
        for x in AmountList:
            NewAmount = x
            NewAmount = int(float(NewAmount)) * PeopleRequired
            NewAmountList.append(NewAmount)
        print("To create",file_name,"you need: ")
        counter = 0
        for x in NameList:
            print(NewAmountList[counter],MeasurementList[counter],"of",x)
            counter = counter + 1
        

    except FileNotFoundError:
        print("File not found.")
    except FileExistsError:
        print("File does not exist.")

#Function to begin the program, repeats if fails
def run_program():
    while True:
        choice = input("1. Create a recipe\n2. Use a recipe\n3. Exit\nChoice: ")
        if choice == "1":
            create_recipe()
        elif choice == "2":
            use_recipe()
        elif choice == "3":
            exit()
        else:
            print("Please use 1, 2 or 3.")

run_program()