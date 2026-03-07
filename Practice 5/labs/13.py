import re
s = input()
x = re.findall(r"\w+", s)
print(len(x))