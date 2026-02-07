n = int(input())
numers = list(map(int, input().split()))
max = numers[0]
for i in numers:
    if i>max:
        max = i
    else :
        continue
print(max)