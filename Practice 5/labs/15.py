import re
s = input()
x = re.sub(r"\d" , lambda w: w.group() * 2, s)
print (x)