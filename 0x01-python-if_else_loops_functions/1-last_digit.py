#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
test = number
if test < 0:
    test *= -1
    test = test % 10
    test *= -1
else:
    test = test % 10

if test == 0:
    print(f"Last digit of {number} is {test} and is 0")
elif test > 5:
    print(f"Last digit of {number} is {test} and is greater than 5")
else:
    print(f"Last digit of {number} is {test} and is less than 6 and not 0")
