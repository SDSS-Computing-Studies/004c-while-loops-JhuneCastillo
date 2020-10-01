#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""

import time 

username = str(input("Username: ")).strip()
password = str(input("Password: ")).strip()

username1 = str("admin")
password1 = str("12345")

while username != username1 and password != password1:
    print ("Access denied")
    username = str(input("Username: ")).strip()
    password = str(input("Password: ")).strip()
    
    
if username == username1 and password == password1: 
        print("Access granted")