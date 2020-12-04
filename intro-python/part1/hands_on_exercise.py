"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print("Pi is a", type(pi), "with a value of", pi)


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i > 50:
    print("i is greater than 50!")
elif i < 50:
    print("i is less than 50!")
else:
    print("i is equal to 50!")


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
print("The fruit is {}".format(picked_fruit))


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def timesNums(num1, num2):
    results = num1 * num2
    return results



# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",timesNums(12,96) )

print("48 x 17 =", timesNums(48, 17))

print("196523 x 87323 =", timesNums(196523, 87323))
