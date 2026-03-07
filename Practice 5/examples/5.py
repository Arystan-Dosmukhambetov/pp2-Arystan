import re

s = "axxxb"

if re.fullmatch(r"a.*b", s):
    print("Match")
else:
    print("No match")
