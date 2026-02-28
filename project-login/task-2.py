"""
This program allows successful login for a valid username and a valid password.
If an invalid login is given after three tries, the program will terminate.
"""

# usernames is a list of valid usernames (case-sensitive)
usernames = ["Ava","Leo","Raj","Zoe","Max","Sam","Eli","Mia","Ian","Kim"]

# passwords is a list of valid passwords (case-sensitive)
passwords = ["12345","abcde","pass1","qwert","aaaaa","zzzzz","11111","apple","hello","admin"]

count = 3 # number of attempts allowed

while count > 0:
    enter_user = input("Enter username: ")
    enter_password = input("Enter password: ")

    # check if entered user and password are valid
    if (enter_user in usernames) and (enter_password in passwords):
        print("Login successful. Welcome", enter_user,"!")
        break # exit loop after successful login

    else:
        count -= 1 # decrease attempt count for invalid inputs
        print("Login incorrect. Tries left:", count)
    