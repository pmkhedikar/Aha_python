#Using cunstructor inheritance :

class A:
    def __init__(self):
        print("Executing class A init")

    def feature1(self):
        print("Executing class A feature 1")


class B():
    def __init__(self):
        super().__init__()
        print("Executing class B init")

    def feature2(self):
        print("Executing class B feature 2")


class C(B,A):
    def __init__(self):
        super().__init__()
        print("Executing class C init")

    def feature2(self):
        print("Executing class C feature 1")

    def feature3(self):
        print("Executing class C feature 3")

obj1=C()
obj1.feature2()