# #Program 1
# def person(name,**data):
#     print(name)
#     print(data)
#
#     for i in data:
#         print(i)
#
# person("Parag",age=30,address="baner,pune",mobile=98987)


#Program 2

# a= 10
#
# def function_created():
#     #global a
#     a=55
#     print("inside function:",a)
#
# function_created()
# print("outside function:",a)


#using local & global variable inside the function

a=10
b=15

def something():
    a=7
    print(a)
    x= globals()['a']
    print(x)
    globals()['a']=14

something()
print(a)