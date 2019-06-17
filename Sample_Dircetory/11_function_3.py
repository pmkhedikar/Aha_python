

def even_odd(lst):

    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst = int(input("Please enter the no:"))

even,odd =even_odd(lst)

print("Even : {} and odd : {}".format(even,odd))