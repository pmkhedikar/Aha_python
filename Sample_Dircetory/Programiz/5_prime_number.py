n = int(input("Enter any no :"))

if n > 1:
    for i in range (2,n):
        if n % i == 0:
            print("{0} is not prime no".format(n))
            break
    else:
        print("{0} is prime no".format(n))
