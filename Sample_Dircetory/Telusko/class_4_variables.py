class Car:
    wheels = 4

    def __init__(self):
        self.mil = 12
        self.comp = "BMW"


Car.wheels = 6

c1 = Car()
c2 = Car()

c1.comp = "Audi"

print(c1.comp, Car.wheels)
print(c2.comp, Car.wheels)
