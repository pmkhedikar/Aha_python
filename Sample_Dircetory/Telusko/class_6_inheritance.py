class A:
    def feature1(self):
        print("Executing feature 1")
    def feature2(self):
        print("Executing feature 2")


class B(A):    # Once u pass the A it can used all the methods in class A ,B is child of A
    def feature3(self):
        print("Executing feature 3")
    def feature4(self):
        print("Executing feature 4")

class C(B):   # Its can use method from class A & class B
    def feature5(self):
        print("Executing feature 5")


class D(A):   # Multiple inheritance fetching method from classes A,B,C
    def feature5(self):
        print("Executing feature 5")



obj1 = A()
obj2 = A()
obj3 = B()
obj4 = C()


obj1.feature1()
obj2.feature1()
obj3.feature3()
obj3.feature1()
obj4.feature5()

