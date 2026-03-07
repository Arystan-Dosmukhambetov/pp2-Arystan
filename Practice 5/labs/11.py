import re
s = input()
x = re.findall(r"[A-Z]", s)
print(len(x))