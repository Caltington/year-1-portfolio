def Question(question, correctanswer, answer1, answer2, answer3):
    print(question)
    useranswer = input("A: " + answer1 + "\nB: " + answer2 + "\nC: " + answer3 + "\n")
    if useranswer.upper() == correctanswer:
        print("Answer was correct!")
    else:
        print("Incorrect!")
        print("The answer was " + correctanswer)

print("Welcome to the Christmas Quiz!")
print("Round 1! Christmas Movies\n")
Question("What is the highest rated christmas movie?", "B", "Nightmare Before Christmas", "Meet me in St. Louis", "The shop around the corner" )
Question("What is the most famous Will Ferrell", "C", "The Lego Movie", "Daddy's Home", "Elf")
Question("What is the name of the dog in how the grinch stole christmas?", "A", "Max", "Bob", "Fluffy")
print("End of round 1!\n")
print("Round 2! Christmas Traditions\n")
Question("What is a popular Christmas Eve meal in Japan?", "B", "Sushi", "KFC", "Frog")
Question("In which country is it a tradition for some to eat a small fermented bird on Christmas day?", "C", "Spain", "Russia", "Greenland")
Question("What is the last ornament German families traditionally hang on their christmas tree?", "A", "Pickle", "Rubber Duck", "Candle")