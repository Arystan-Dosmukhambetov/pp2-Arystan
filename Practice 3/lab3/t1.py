s = input().strip()
for c in s:
    if int(c) % 2 != 0:
        print("Not valid")
        exit()
print("Valid")