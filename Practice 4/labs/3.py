import sys

n = int(input())

def divisible(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

it = divisible(n)
first = True
for x in it:
    if first:
        sys.stdout.write(str(x))
        first = False
    else:
        sys.stdout.write(" " + str(x))