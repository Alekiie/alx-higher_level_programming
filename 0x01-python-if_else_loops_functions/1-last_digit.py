#!/usr/bin/python3
import random
number = random.randint(-10, 10)
string = "Last digit of"
if number < 0:
    x = number % -10
elif number >= 0:
   x = number % 10
if(x > 5):
    print(f"{string} {number} is {x} and is greater than 5")
elif(x == 0):
    print(f"{string} {number} is {x} and is 0")
else:
    print(f"{string} {number} is {x} and is less than 6 and not 0")
