class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


# Input
n = int(input())

# Create object and print area
sq = Square(n)
print(sq.area())
