n = int(input())
arr = list(map(int, input().split()))
prev = []

for x in arr:
    if x in prev:
        print("NO")
    else:
        print("YES")
        prev.append(x)