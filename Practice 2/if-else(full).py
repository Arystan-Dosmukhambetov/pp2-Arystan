#if_statement.py example
a = 33
b = 200

if b > a:
    print("b is greater than a")


#if_else.py example
a = 33
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


#if_elif_else.py example
a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


#short_hand_if.py example
a = 200
b = 33

print("A") if a > b else print("B")
