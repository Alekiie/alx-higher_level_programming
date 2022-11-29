#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if (number >0):
    print(f"The number selected is {f}, which is positive")
elif(number==0):
    print("The number selected is 0")
else:
    print(f"The number selected is {number},which is negative")
