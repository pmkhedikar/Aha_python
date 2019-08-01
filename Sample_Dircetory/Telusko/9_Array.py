# Program 1

from array import *

val = array('i', [2, 5, 19, -5])

newarray = array(val.typecode, (a * a for a in val))

for i in newarray:
    print(i)

# #Program 2
#
# from array import *
# val= array('i', [2,5,19,-5])
#
# newarray = array(val.typecode,(a*a for a in val))
#
# i=0
# while i < len(newarray):
#     print(newarray[i])
#     i=i+1
