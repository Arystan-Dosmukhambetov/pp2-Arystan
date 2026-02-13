class Bird:
    def fly(self):
        print("Flying")

class Penguin(Bird):
    def fly(self):
        print("Cannot fly")

p = Penguin()
p.fly()
