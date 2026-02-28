a, b = map(int, input().split())

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

for x in squares(a, b):
    print(x)