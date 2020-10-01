##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Acces denied
"""

import time 

username = str(input("Username: ")).strip()
password = str(input("Password: ")).strip()

username1 = str("admin")
password1 = str("12345")
countTries = 0

while username != username1 and password != password1:
    print ("Access denied")
    countTries = countTries + 1
    if countTries > 2:
        break
    username = str(input("Username: ")).strip()
    password = str(input("Password: ")).strip()
    
    
if username == username1 and password == password1: 
        print("Access granted")