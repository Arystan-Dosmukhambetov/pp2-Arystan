n = int(input())
arr = list(map(int, input().split()))

squared = [x**2 for x in arr]

print(*squared)