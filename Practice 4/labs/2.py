import sys

n = int(input())

def evens(n):
    for i in range(0, n + 1, 2):
        yield i

it = evens(n)
try:
    first = next(it)
    sys.stdout.write(str(first))
    for x in it:
        sys.stdout.write("," + str(x))
except StopIteration:
    pass