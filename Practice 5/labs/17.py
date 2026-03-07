import re
s = input()
x = re.findall(r"\d{2}/\d{2}/\d{4}", s)
print(len(x))