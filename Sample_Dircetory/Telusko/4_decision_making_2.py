fridge_contents = {'egg': 8, 'mushroom':20, 'pepper':3, 'cheese':2, 'tomato':4, 'apples':13}
try:

    if fridge_contents['orange juice'] > 3:
        print ("Sure lets have some juice")
    except KeyError:
        print ("Aww theres no juice. Lets go shopping")