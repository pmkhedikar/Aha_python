class talentica:

    def __init__(self):
        self.name = "Parag"
        self.age = 30

    def update(self):
        self.age = 99

    def compare(self, others):
        if self.age == others.age:
            return True
        else:
            return False


emp1 = talentica()
emp2 = talentica()

emp1.name = "Anuraj"
emp1.age = 32


if emp1.compare(emp2):
    print("They are same")
else:
    print("They are different")

# print(emp1.age)
# print(emp2.age)
# print(emp2.update())
