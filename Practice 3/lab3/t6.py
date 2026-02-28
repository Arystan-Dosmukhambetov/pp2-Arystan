class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Input
l, w = map(int, input().split())

# Create object and print area
rect = Rectangle(l, w)
print(rect.area())
