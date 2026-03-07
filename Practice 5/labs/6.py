import re
s = input()
x = re.search(r"\S+@\S+\.\S+", s)
if x:
    print(x.group())
else:
    print("No email")