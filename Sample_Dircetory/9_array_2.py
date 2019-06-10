# #program 1
# from array import *
#
# user_arr =array('i',[])
#
# n=int(input("please enter the length of array :"))
#
# for i in range(n):
#     x =int(input("please enter the values :"))
#     user_arr.append(x)
#
# for j in user_arr:
#     print(j)


#program 2

from array import *

pre_arr =array('i',(2,4,6,8,10))

user_arr= int(input("Please enter the value of array : "))
pre_arr.append(user_arr)

print(pre_arr)

for i in pre_arr:
    print(i)



