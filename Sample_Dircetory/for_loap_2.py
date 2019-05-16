#for i in range (0,10):
#    print(i)
#for i in range (0, len(number)):
#    print (number[i])
    
number ="1,22,3,4,45678"
CleanNumber=''

for char in number:
    if char in '12674':
        print(char)
        
#        CleanNumber= CleanNumber +char

#NewCleanNumber=int(CleanNumber)
#print("the new number is {0}".format(CleanNumber))

for state in ["Small","Beautiful","Green"]:
    print("The parrot is "+ state)

for i in range (0,50,5):
    print(i)

for i in range(1,13):
    for j in range(1,11):
        print("{0} into {1} is {2}".format(i,j,i*j))
    print("*****************")
