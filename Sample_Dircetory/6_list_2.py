menu=[]
menu.append(['rice','dal','buttermilk'])
menu.append(['dal' ,'spam'])
menu.append(['rice','sproutes','spam'])

for meal in menu:
    if not 'spam' in meal:
        print(meal)
        for items in meal:
            print(items)

