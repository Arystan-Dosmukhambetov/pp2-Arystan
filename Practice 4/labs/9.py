n = int(input())

def powers_of_two(n):
    for i in range(n + 1):
        yield 2 ** i

print(*powers_of_two(n))