#! python3
"""
Have the user enter a number.
Display the multiples of that number, up to 12 times that number:
All numbers should be on the same line.
(2 marks)

inputs:
int number

outputs:
multiples of that number on one line

example:
Enter a number: 4
4 8 12 16 20 24 28 32 36 40 44 48
"""

import time

x = int(input("Enter a number: "))

targetNum = x * 13
count = 1
newNum = x

while newNum != targetNum:
    print(newNum, end=(" "))
    count = count + 1
    newNum = x * count 