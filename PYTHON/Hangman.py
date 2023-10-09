import random
# word = random.choice(["Eggs", "Frog", "Volcano", "Keyboard", "Python", "Program"])
word = "python"
wordguess = word
attempts = 0
maxattempts = 6
complete = False
print("This word has", len(word), "letters.")
while complete == False:
    choice = input("Pick a letter or guess the word. You have "+ str(maxattempts - attempts) + " guesses!")
    choice = choice.lower()
    if len(choice) == 1:
        if  word.find(choice) != -1:
            wordguess = wordguess.replace(choice, "")
            print ("You got a letter! Well done!")
        else:
            attempts = attempts + 1
    elif len(choice) != 1 and choice != word:
        print ("That is not a letter in the word, or the word its self!")
        attempts = attempts + 1
    if choice == word:
        print ("Well Done! The word was " + word)
        complete = True
    if wordguess == "":
        print ("Well done! The word was " + word)
        complete = True
    if attempts == maxattempts:
        complete = True
        print ("Too bad, you didn't win!")
