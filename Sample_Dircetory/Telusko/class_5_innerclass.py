class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.ram = 8
            self.comp = 'Dell'
            self.procc = 'i5'

        def show(self):
            print(self.ram, self.comp, self.procc)


s1 = student('Anuraj', 110)
s2 = student('Ishan', 120)

# print(s1.name)
s2.show()
