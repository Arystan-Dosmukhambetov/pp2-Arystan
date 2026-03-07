import re
s = input()
x = re.search(r"Name: ([^,]+), Age: (\S+)" , s)
print(x.group(1), x.group(2))
