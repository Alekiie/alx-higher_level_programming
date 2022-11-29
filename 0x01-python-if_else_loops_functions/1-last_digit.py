#!/usr/bin/python3
import random
number = random.randint(-10, 10)
x = int(repr(number[0]))
string1 = "Last digit of"
string2 = "is"
if(x > 5):
    print(f"{string1} {number} {string2} {x} and is greater than 5")
elif(x == 0):
    print(f"{string1} {number} {string2} {x} and is 0")
else:
    print(f"{string1} {number} {string2} {x} and is less than 6 and not 0")
