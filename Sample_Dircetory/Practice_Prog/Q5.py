# Question:Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


class New_String(str):
    def __init__(self):
        self.s = ''

    def getstring(self):
        self.s = input("Enter the string: ")

    def print_string(self):
        print(self.s.upper())
        print("Lower case:{0}".format(self.s.lower()))


string1 = New_String()
string1.getstring()
string1.print_string()
