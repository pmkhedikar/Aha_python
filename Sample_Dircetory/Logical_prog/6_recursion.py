##Program 1
# import sys
#
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(10)
# print(sys.getrecursionlimit())
#
#
# def greet():
#     print("hello")
#     greet()
#
# greet()


# Prog 2


def fct(n):
    if n==0:
        return 1
    return n * fct(n-1)



result = fct(4)
print(result)