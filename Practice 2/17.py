n = int(input())
contacts = {}

for _ in range(n):
    num = input()
    if num in contacts:
        contacts[num] += 1
    else:
        contacts[num] = 1

count = 0
for v in contacts.values():
    if v == 3:
        count += 1

print(count)