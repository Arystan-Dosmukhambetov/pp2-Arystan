import re

s = "abbb"

if re.fullmatch(r"ab*", s):
    print("Match")
else:
    print("No match")
