import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Read input
r = int(input())

# Create Circle object and print area
c = Circle(r)
print(f"{c.area():.2f}")
