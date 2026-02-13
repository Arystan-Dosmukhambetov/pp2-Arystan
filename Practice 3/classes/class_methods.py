class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(self.brand, "is driving")

c = Car("Toyota")
c.drive()
