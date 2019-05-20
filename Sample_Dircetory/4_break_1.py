# Program -1 (ignore that item & continue)
#
# shopping_list = ['rice', 'milk' , 'spam','dry fruits']
# for items in shopping_list:
#     if items=='spam':
#         break
#     print(items)


# # Program -2 (Once that item found ignore all other items )
#
# shopping_list = ['rice', 'milk' , 'wheat','dry fruits']
# for items in shopping_list:
#     if items=='spam':
#         break
#     print("Buy " + items)


# Program -3  (if that item found ignore all)

# shopping_list = ['rice', 'milk' , 'wheat', 'spam', 'dry fruits']
# bad_food=''
# for items in shopping_list:
#     if items=='spam':
#         bad_food =items
#         break
# else:
#     print('I will have dinner')
#
# if bad_food == 'spam':
#     print("I am not having dinner today")
#


# # program -4 Modify this loop to stop when i is exactly divisible by 11
#
# for i in range(0, 100, 7):
#         if i > 0 and i % 11 == 0:
#             print(i)
#             break


# Program 5

for i in range (20):
    if i > 0 and i % 3 != 0 and i % 5 !=0:
        print(i)
