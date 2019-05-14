print("Guess number between 1 to 10 :")
guess=int(input())

#if guess < 5:
#    print("please guess the higher number")
#    guess=int(input())
#    if guess == 5:
#        print("Now,you have guessed correct number")
#    else:
#        print("Sorry you have guessed wrong number")
#elif guess > 5:
#    print("please guess the lower number")
#    guess=int(input())
#    if guess == 5:
#        print("Now ,you have guessed correct number")
#    else:
#        print("Sorry you have gussed incorrect number")
#else:
#    print("Great ,you have gussed correct number {0} in first attempt".format(guess))

if guess != 5:
    if guess > 5:
        print("Guess lower")
    else:
        print("Guess higher")
    guess=int(input())
    if guess==5:
        print("You guess correct")
    else:
        print("Sorry ")
else:
    print("You guessed on first attempt")

