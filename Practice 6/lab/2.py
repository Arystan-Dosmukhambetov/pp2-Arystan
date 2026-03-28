n = int(input())
nums = map(int, input().split())

evens = filter(lambda x: x % 2 == 0, nums)
print(len(list(evens)))
