def fib(n):
    a = 0
    b = 1

    if n == 0:
        print("0")
    else:
        print(a)

        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)

n=int(input("Enter the value for fibonacci series :"))
fib(n)
