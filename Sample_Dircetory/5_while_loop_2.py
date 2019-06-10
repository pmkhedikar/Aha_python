import random

highest= 10
answere=random.randint(1,highest)

print("Please guess the number between 1 to {} :".format(highest))
guess=0 #initialize the number
while guess < answere:
    print("Guess higher number")
    guess+=1




