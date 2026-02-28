import math


# 1. Convert degree to radian
print("1) Degree to Radian")
degree = 15
radian = degree * (math.pi / 180)
print("Input degree:", degree)
print("Output radian:", round(radian, 6))
print()


# 2. Area of a trapezoid
print("2) Area of Trapezoid")
height = 5
base1 = 5
base2 = 6

area_trapezoid = (base1 + base2) / 2 * height
print("Height:", height)
print("Base, first value:", base1)
print("Base, second value:", base2)
print("Expected Output:", area_trapezoid)
print()


# 3. Area of regular polygon
print("3) Area of Regular Polygon")
n = 4
side = 25

area_polygon = (n * side * side) / (4 * math.tan(math.pi / n))
print("Input number of sides:", n)
print("Input the length of a side:", side)
print("The area of the polygon is:", int(area_polygon))
print()


# 4. Area of parallelogram
print("4) Area of Parallelogram")
base = 5
height_para = 6

area_parallelogram = base * height_para
print("Length of base:", base)
print("Height of parallelogram:", height_para)
print("Expected Output:", float(area_parallelogram))
