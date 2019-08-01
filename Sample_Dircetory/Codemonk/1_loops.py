# fruits =['apple','mango','grapes']
# for fruit in fruits:
#     print(fruit)
#     print('length of fruit : {0} is {1}'.format(fruit, len(fruit)))


# fruits =['apple','mango','grapes']
# length = len(fruits)
# i = 0
# while i < length:
#     print(len(fruits))
#     print(fruits[i])
#     i = i+1



# for i in range(1, 10):
#     for j in range(1, 11):
#         print("{0} into {1} is {2}".format(i,j,i*j))
#     print("######################")


i =int(input('Please enter any no: '))

if i >= 10:
    if i <= 50:
        print('Its between 10 to 50')
    else:
        print('Its greater than 50')

else:
    print('Its less than 10')
