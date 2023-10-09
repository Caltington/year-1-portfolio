import random

word = ["cat", "sat", "on", "the", "mat"]
secretword = random.choice(word)
hangman = []

secretwordlen = len(secretword)
for x in range(secretwordlen):
    hangman.append("-")

print("You have 5 guesses")
print("The word is",secretwordlen, "letters long")
win = False
while win == False:
    print(hangman)
    letter = input("Enter a letter or guess the word: ")
    letter = letter.lower()
    if len(letter) == 1:
        for x in range (0, secretwordlen):
            if secretword[x] == letter:
                hangman[x] = letter
            else:
                print("The letter was wrong.")
    else:
        if letter == secretword:
            print("You got it right!")
            win = True
print("Game over")


