"""
This program allows a user to create and store new rabbytes. Each rabbit has a unique name. 
The program also allows the user to enter a rabbit's age, create a parental relationship, list all rabbits in the database, and list a rabbit's direct and indirect family.
"""

# dictionary to store all rabbit information (name, age, parent, kitten)
rabbits: dict[str, dict] = {}

def main_menu() -> None:
    """ 
    Main menu of the program. User can input numbers between 0 and 6 (inclusive) and it runs the corresponding function. Otherwise, the prompt is simply printed again. 
    """

    # display menu options
    print("==================================")
    print("Enter your choice:")
    print("1. Create a Rabbit.")
    print("2. Input Age of a Rabbit.")
    print("3. List Rabbytes.")
    print("4. Create a Parental Relationship.")
    print("5. List Direct Family of a Rabbit.")
    print("6. Find Cousins of a Rabbit.")
    print("0. Quit.")
    print("==================================")

    option = input()

    if option == "1":
        create_rabbit()
    elif option == "2":
        input_age()
    elif option == "3":
        list_rabbytes()
    elif option == "4":
        create_rel()
    elif option == "5":
        list_family()
    elif option == "6":
        find_cousins()
    elif option == "0":
        return # quit program
    else:
        main_menu()
    
    main_menu() # redisplay menu if invalid input given 

def create_rabbit() -> None:
    """ 
    Prompts the user to enter a new rabbit's name. 
    If name is unique, it is added to the dictionary with no age yet (None).
    If name is already exists, the user is notified and prompted again.
    When a valid name is entered, the function returns to the main menu.
    """
    print("Input the new rabbit's name:")
    name = input()

    # if name is unique (does not exist), added to dictionary with unknown age
    if name not in rabbits:
        rabbits[name] = {"age": None, "parents": [], "kittens": []}
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
        rabbits[name]["age"] = age # update rabbit's age
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
    for name, info in rabbits.items():
        # display age as unknown if no age is set
        age_display = info["age"] if info["age"] is not None else "Unknown"
        print(f"{name} ({age_display})")

def create_rel() -> None:
    """
    Create parent-kitten relationship.
    Name of parent is asked first, and then name of child (rabbit).
    If either name don't exist, a rabbit with that name is created.
    """
    print("Input the parent's name:")
    parent = input()

    # if parent name doesn't exist, rabbit with that name is created
    if parent not in rabbits:
        rabbits[parent] = {"age": None, "parents": [], "kittens": []}

    print("Input the kitten's name:")
    kitten = input()
    
    # if kiten name doesn't exist, rabbit with that name is created
    if kitten not in rabbits:
        rabbits[kitten] = {"age": None, "parents": [], "kittens": []}

    # add relationship if it's not already present
    if kitten not in rabbits[parent]["kittens"]:
        rabbits[parent]["kittens"].append(kitten)
    if parent not in rabbits[kitten]["parents"]:
        rabbits[kitten]["parents"].append(parent)


def list_family() -> None:
    """
    Displays the parents and kittens of a given rabbit.
    """
    print("Input the rabbit's name:")
    name = input()

    if name in rabbits:
        parents = sorted(rabbits[name]["parents"])
        kittens = sorted(rabbits[name]["kittens"])

        print(f"Parents of {name}:")
        if parents:
            for p in parents:
                print(p)
        print(f"Kittens of {name}:")
        if kittens:
            for k in kittens:
                print(k)
        return
    else:
        print("That name is not in the database.")
        list_family()

def find_cousins() -> None:
    """
    Displays the cousins of a rabbit. A cousin is a kitten of a sibling of a parent.
    """
    print("Input the rabbit's name:")
    name = input()

    if name not in rabbits:
        print("That name is not in the database.")
        return find_cousins()
            
    cousins = set() # use a set to avoid duplicates

    # get rabbit's parents
    parents = rabbits[name].get("parents", [])

    # for each parent, find the parent's siblings (aunts/uncles)
    for parent_name in parents:
        parent = rabbits.get(parent_name)
        if parent:
            grandparents = parent.get("parents", [])

            for grandparent_name in grandparents:
                grandparent = rabbits.get(grandparent_name)
                if grandparent:
                    siblings = grandparent.get("kittens", [])
                    for sibling_name in siblings:
                        if sibling_name != parent_name:
                            sibling = rabbits.get(sibling_name)
                            if sibling:
                                cousins.update(sibling["kittens"])

    print(f"Cousins of {name}:")

    if cousins:
        print(f"{','.join(sorted(cousins))}")
    return
    find_cousins()

if __name__ == "__main__":
    main_menu()