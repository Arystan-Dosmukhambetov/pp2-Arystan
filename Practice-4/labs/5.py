n = int(input())

def countdown(n):
    for i in range(n, -1, -1):
        yield i

for x in countdown(n):
    print(x)