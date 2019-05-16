# print("Guess number between 1 to 10 :")
# guess=int(input())

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

# if guess != 5:
#     guess=int(input())
#     if guess==5:
#         print("You guess correct")
#     else:
#         print("Sorry ")
# else:
#     if guess > 5:
#         print("Guess lower")
#     else:
#         print("Guess higher")
#     print("You guessed on first attempt")

a=int(input("Enter your age :"))
if (a<18) and (a>65):
    print("Your are eligible for work")
else:
    print("You have to wait for {} years".format(18 - a))







