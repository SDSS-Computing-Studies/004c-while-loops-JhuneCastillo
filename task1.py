#! python3

"""
Count by 2's and display all the numbers, 1 on each line.
Continue until the current value is 20
(2 marks)
Inputs:
none

Outputs:
Example:
2
4
6
8
10
...
"""

import time

targetNum = 22
count = 0

while count != targetNum:
    print(count)
    count = count + 2 
    time.sleep(0.5)
