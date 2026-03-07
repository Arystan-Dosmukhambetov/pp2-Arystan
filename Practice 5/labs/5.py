import re
s = input()
x = re.search(r"^[A-Za-z].*\d$", s)
if x:
    print("Yes")
else:
    print("No")