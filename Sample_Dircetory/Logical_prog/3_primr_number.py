i = 8
for num in range(2, i):
    if i % num == 0:
        print("{0} is not prime number".format(i))
        break
else:
     print("Its  prime number")
