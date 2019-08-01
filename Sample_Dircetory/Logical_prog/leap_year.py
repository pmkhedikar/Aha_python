def leap_year(n):
    if (n % 4 == 0) and ((n % 100 !=0) or (n % 400 == 0)):
        print("{0} is leap year".format(n))
    else:
        print("{0} is not leap year ".format(n))


year = int(input('Enter the year :'))
leap_year(year)



# def is_leap(year):
#     if (year % 4 == 0) and (year % 100 != 0) and (year % 400 == 0):
#         return leap= False
#     else:
#         return leap = True
#
# year = int(input())
# is_leap(year)
