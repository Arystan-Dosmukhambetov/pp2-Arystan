class Animal:
    type = "Mammal"

    def __init__(self, name):
        self.name = name

a = Animal("Dog")
print(a.name)
print(a.type)
