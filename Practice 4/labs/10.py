lst = input().split()
n = int(input())

def limited_cycle(lst, n):
    for _ in range(n):
        for item in lst:
            yield item

print(*limited_cycle(lst, n))