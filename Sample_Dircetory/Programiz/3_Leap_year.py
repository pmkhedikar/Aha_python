#find leap year

year = int(input("Please enter the year:"))

if (year % 4 == 0)  and(year % 400 == 0 or year % 100 != 0):
    print("{0} is leap year".format(year))

else:
    print("{0} is not leap year".format(year))



# if (year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print("{0} is a leap year".format(year))
#        else:
#            print("{0} is not a leap year".format(year))
#    else:
#        print("{0} is a leap year".format(year))
# else:
#    print("{0} is not a leap year".format(year))