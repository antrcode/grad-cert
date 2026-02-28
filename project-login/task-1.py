"""
This program asks the user to enter a username.
If username is valid then a successful login occurs.
"""

# usernames is the list of all valid usernames
usernames = ["Ava","Leo","Raj","Zoe","Max","Sam","Eli","Mia","Ian","Kim"]

# keep prompting the user until valid username is provided
while True:
    enter_user = input("Enter username: ")

    if enter_user in usernames:
        print("Login successful. Welcome", enter_user,"!")
        break # exit loop after given valid username
    else:
        print("Login incorrect.") # inform user of invalid input