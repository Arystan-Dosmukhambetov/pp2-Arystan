import re
s = input() 
x = re.findall(r"\b\w{3}\b",s)
print(len(x))
