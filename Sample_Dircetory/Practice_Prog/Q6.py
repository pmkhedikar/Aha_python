#Question:    Write a method which can calculate square value of number


def cub(n):
    return n**3


n = int(input("Enter the any no: "))
print("The cube of {0} is {1}".format(n, cub(n)))