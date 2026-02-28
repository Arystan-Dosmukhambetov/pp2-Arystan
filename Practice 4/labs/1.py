n = int(input())

def squares(n):
    for i in range(1, n + 1):
        yield i * i

for x in squares(n):
    print(x)