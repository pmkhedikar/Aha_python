import  math
from math import pi
from math import *

name = input("please enter you name:  ")
age = int(input("How old are you, {0}: ".format(name)))
print(age)

if age >= 18:
    print('Your are eligible for Voting')
else:
    print("please come later after {0} years".format(18 - age))

print(math.pi)
print(pi)


