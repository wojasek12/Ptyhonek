import random

randomGuess = random.randint(1, 9)

guess = False

while(not guess):
    number = int(raw_input("Strzelaj mordo pomiedzy 1 a 9: "))
    if number > randomGuess:
        print("NIZEJ")
    elif number < randomGuess:
        print("Wincyj")
    else:
        print("Trafiles!")
