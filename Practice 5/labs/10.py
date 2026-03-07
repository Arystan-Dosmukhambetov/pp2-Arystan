import re
s = input()
x = re.search("cat|dog", s)
if x:
    print("Yes")
else:
    print("No")