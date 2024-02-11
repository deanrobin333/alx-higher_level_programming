#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

o_number = number
if number < 0:
    number = number * -1
    last = (number % 10) * -1
else:
    last = number % 10

if last == 0:
    print(f"Last digit of {number} is {last} and is 0")
elif last < 6:
    print(f"Last digit of {o_number} is {last} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last} and is greater than 5")
