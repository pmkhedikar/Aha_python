def div(a, b):
    print(a/b)


def smart_div(ftn):
    def inner_div(a, b):
        if a < b:
            a, b =b, a   #Swapping logic
        return ftn(a, b)

    return inner_div


div = smart_div(div)

div(60, 50)



