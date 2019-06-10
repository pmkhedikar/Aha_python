# #Program 1
# def update(x):
#     print('x', 8)
#
#
# a = 10
# update(15)
#print('a', a)


#program 2
#
# def person(name,age=18):
#     print(name)
#     print(age)
#
# person('parag',24)


# #program 3
#
# def add(a,b):
#     c=a+b
#     return c
#
# add(3,5)  #-by calling it ,it give c
# print(add(3,4)) #- by callling it & print the result


#Program 4

def sum(a, *b):
    print(a)
    print(b)

    c=a
    for i in b:
        c=c+i
    print(c)

sum(3,4)

