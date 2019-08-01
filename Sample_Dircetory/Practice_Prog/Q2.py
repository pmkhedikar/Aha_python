# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8
# Then, the output should be: 40320


def fct(n):
    f = 1
    for i in range(1, n + 1):
        f = i * f
    return f


n = int(input("Please enter any number for factorial :"))
print(fct(n))



# def fact(n):
#     if n ==0:
#         return 1
#     return n * fact(n-1)
# n = int(input("Please enter any number for factorial :"))
# print(fact(n))
