#while_loop.py example
i = 1
while i < 6:
    print(i)
    i += 1

#while_break.py example
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# while_continue.py example
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# for_loop.py example
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# for_break.py example
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

# for_continue.py example
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
