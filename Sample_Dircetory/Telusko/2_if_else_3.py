n = int(input("Enter any no: "))

if n % 2 != 0:
    print('Its odd no')
elif(n % 2 == 00) and (2 <= n <= 5):
    print('Its even no between 2 to 5')
elif (n % 2 == 00) and (6 <= n <= 20):
    print("Its even no between 6 to 20")
elif n == 0:
    print("{0} is even no".format(n))
else:
    print('Its even no more than 20')

