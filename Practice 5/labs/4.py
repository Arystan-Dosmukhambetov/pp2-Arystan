import re
s = input()
x = re.findall(r"\d", s)
print(*x)