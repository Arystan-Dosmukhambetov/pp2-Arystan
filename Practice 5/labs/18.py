import re
s = input()
p = input()
pattern = re.escape(p)
x = re.findall(pattern, s)
print(len(x))