n = int(input())
nums = map(int, input().split())

print(sum(x*x for x in nums))
