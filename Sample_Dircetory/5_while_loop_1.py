# for i in range (10):
#     print("In for loop the value of i is {0}".format(i))


# j =0  #initialize the value
# while j<10:
#     print("In while loop the value of i is {0}".format(j))
#     j= j+1  #looping condition


exit_door=['north','south']
enter_direction =''

while enter_direction not in exit_door:
    enter_direction=input('Please enter the direction : ')
    if enter_direction=='quite':
        print("Game over ..Thank you ! ")
        break
    else:
        print("Please go ahead door is open there !")

print("Please go ahead door is open there !")
