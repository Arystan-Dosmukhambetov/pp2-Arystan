3 types of nums
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100

#Complex:
x = 3+5j
y = 5j
z = -5j

#Random Number. Python does not have a random() function to make a random number, but Python has 
#a built-in module called random that can be used to make random numbers:

import random
print(random.randrange(1, 10))
