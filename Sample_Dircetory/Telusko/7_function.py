import math
from math import pi


# n = int(input("Enter any number :"))
n = 10

def countdown(n):
    if n < 0:
        print("Blastoff")
    else:
        return n-1


print(countdown(n))



# signal_power = float(input("Enter the signal power "))
# noise_power = float(input("Enter the noise power"))
# ratio = float(signal_power / noise_power)
# decibels = 10 * math.log10(ratio)
# print(decibels)


# R =float(input("Enter the radius of triangle"))
# print("Area of triangle is {0}".format(math.sqrt(R)*pi))
