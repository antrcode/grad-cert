"""
This program allows successful login for a valid username and a valid password.
If an invalid login is given after three tries, the program asks the user whether or not they are a robot.
If they are not a robot (enters "n"), the user is allowed three more tries.
If they are a robot (enters "Y" or nothing ""), the program terminates.
"""

# usernames is a list of valid usernames (case-sensitive)
usernames = ["Ava","Leo","Raj","Zoe","Max","Sam","Eli","Mia","Ian","Kim"]

# passwords is a list of valid passwords (case-sensitive)
passwords = ["12345","abcde","pass1","qwert","aaaaa","zzzzz","11111","apple","hello","admin"]

# combine [username, password] pairs into a list
accounts = []
i = 0
while i < len(usernames):
    accounts.append([usernames[i], passwords[i]])
    i += 1

count = 3 # number of login attempts per round

while True: 
    # loop for login attempts
    while count > 0: 
        enter_user = input("Enter username: ")
        enter_password = input("Enter password: ")

        successful_entry = [enter_user, enter_password] # list for comparison

        if successful_entry in accounts:
            print("Login successful. Welcome", enter_user,"!") # welcome user if login successful
            break

        else:
            count -= 1 # decrease attempt count for each invalid login
            print("Login incorrect. Tries left:", count)

    # terminate program if login successful
    if successful_entry in accounts:
        break

    # after three failed tries, ask user if they are a robot
    while count == 0:
        answer = input("Are you a robot (Y/n)? ")

        # reprompt until valid input
        while answer not in ["Y", "n", ""]:
            answer = input("Are you a robot (Y/n)? ")
        
        else:
            count = 3 # give three more tries if not robot

    # if user inputs "Y" or nothing ("") → user is a robot → terminate program
    if answer in ["Y", ""]:
        break