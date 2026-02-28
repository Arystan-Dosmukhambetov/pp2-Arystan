# 1. Generator: squares up to N

def squares_up_to_n(n):
    for i in range(n + 1):
        yield i * i


print("1) Squares up to N")
N = 5
for value in squares_up_to_n(N):
    print(value)
print()


# 2. Even numbers from 0 to n (comma separated)

def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i


print("2) Even numbers from 0 to n")
n = int(input("Enter n for even numbers: "))
print(",".join(str(x) for x in even_numbers(n)))
print()


# 3. Numbers divisible by 3 and 4 between 0 and n

def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


print("3) Numbers divisible by 3 and 4")
for value in divisible_by_3_and_4(n):
    print(value, end=" ")
print("\n")


# 4. Generator squares(a, b)

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i


print("4) Squares from a to b")
a = 1
b = 5
for value in squares(a, b):
    print(value)
print()


# 5. Countdown generator from n to 0

def countdown(n):
    for i in range(n, -1, -1):
        yield i


print("5) Countdown from n to 0")
for value in countdown(5):
    print(value)
