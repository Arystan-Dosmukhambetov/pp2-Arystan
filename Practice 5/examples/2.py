import re

s = "abbb"

if re.fullmatch(r"ab{2,3}", s):
    print("Match")
else:
    print("No match")
