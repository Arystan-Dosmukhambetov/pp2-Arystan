import re
s = input()
x = re.compile(r"^\d+$")
if x.search(s):
    print("Match")
else:
    print("No match")