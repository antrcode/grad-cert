"""
This program allows a user to create and store new rabbytes. Each rabbit has a unique name. 
The program also allows the user to enter a rabbit's age, and list all rabbits in the database.
"""

# dictionary to store each rabbit's name and age
rabbits = {} # key = rabbit's name (string), value = age (int)

def main_menu() -> None:
    """ 
    Main menu of the program. User can input 1,2,3, or 0 and it runs the corresponding function. Otherwise, the prompt is simply printed again. 
    """

    # display menu options
    print("==================================")
    print("Enter your choice:")
    print("1. Create a Rabbit.")
    print("2. Input Age of a Rabbit.")
    print("3. List Rabbytes.")
    print("0. Quit.")
    print("==================================")

    option = input()

    if option == "1":
        create_rabbit()
    elif option == "2":
        input_age()
    elif option == "3":
        list_rabbytes()
    elif option == "0":
        return # quit program
    else:
        main_menu()
        
    main_menu() # redisplay menu if invalid input given (i.e. input is not options 1,2,3, or 0)

def create_rabbit() -> None:
    """ 
    Prompts the user to enter a new rabbit's name. 
    If name is unique, it is added to the dictionary with no age yet (None).
    If name is already exists, the user is notified and prompted again.
    When a valid name is entered, the function returns to the main menu.
    """
    print("Input the new rabbit's name:")
    name = input()

    # check if the rabbit name already exists in the dictionary
    if name not in rabbits:
        # rabbit's name is added with unknown age
        rabbits[name] = None
        return
    else:
        # notify user if name already exists
        print("That name is already in the database.")
        create_rabbit()

def input_age() -> None:
    """ 
    Prompts the user to input the age of a rabbit that already exists in the database.
    If the name exists, the program will ask for the user to input the age.
    If the name does not exist, the user is notified and prompted again.
    """
    print("Input the rabbit's name:")
    name = input()

    # check if the rabbit name exists in the dictionary
    if name in rabbits:
        print(f"Input {name}'s age:")
        age = int(input()) # age is an integer
        rabbits[name] = age # update rabbit's age
        return
    else:
        # notify user if name does not exist
        print("That name is not in the database")
        input_age()
        
def list_rabbytes() -> None:
    """ 
    Prints list of all rabbits and their age.
    If a rabbit has no age, "Unknown" is displayed. 
    """
    print("Rabbytes:")
    for name, age in rabbits.items():
        # display age as unknown if no age is set
        age_display = age if age is not None else "Unknown"
        print(f"{name} ({age_display})")

# test program
if __name__ == "__main__":
    main_menu()