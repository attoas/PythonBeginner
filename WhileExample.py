correctNumber = 10
userGuess = 0
while userGuess != correctNumber:
    userGuess = int(input("Please guess a number : "))
    if userGuess > correctNumber:
        print("Too Large")
    elif userGuess < correctNumber:
        # print("True move")
        print("Too Small")
    elif userGuess == correctNumber:
        print("Correct !!")