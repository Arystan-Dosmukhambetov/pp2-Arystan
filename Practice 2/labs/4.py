n = int(input())
pos = 0

for num in input().split():
    if int(num) > 0:
        pos += 1
print(pos)