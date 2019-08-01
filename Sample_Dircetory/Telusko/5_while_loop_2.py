import random

highest = 20
answere = random.randint(1, highest)
print(answere)

print("Please guess the number between 1 to {} :".format(highest))
guess = 5 #initialize the number
while guess < answere:
    guess += 1
    print("Guess higher number")



