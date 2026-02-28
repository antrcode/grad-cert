"""
This program allows a user to select a container, and then "loot" valid items into it.

After a valid container is selected, the user can:
    1. Loot an item into the selected container if it fits.
    2. List all items currently looted in the container.
    3. Quit the program.
"""

# lists to store all items and containers
items = []
containers = []

# classes
class Item:
    """
    Item class represents an item with a name and weight.

    Instance Variables:
        name(str): The name of the item.
        weight(int): The weight of the item.
    """
    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight

class Container:
    """
    Container class represents a container that can hold items.

    Instance Variables:
        name (str): Name of the container.
        empty_weight (int): Weight of the container when empty.
        capacity (int): Maximum total weight of items placed inside container.
        contents (List[Item]): List of items currently inside the container.
    """
    def __init__(self, name: str, empty_weight: int, capacity: int) -> None:
        self.name = name
        self.empty_weight = empty_weight
        self.capacity = capacity
        self.contents = []

    def total_weight(self) -> int:
        """ Returns total weight = empty weight + weight of contained items. """
        return self.empty_weight + sum(item.weight for item in self.contents)

    def remaining_capacity(self) -> int: 
        """ Returns remaining weight capacity = capacity - weight of contained items. """
        used_weight = sum(item.weight for item in self.contents)
        return self.capacity - used_weight

# read items.csv
with open("items.csv", "r") as fileref:
    for line in fileref.readlines()[1:]: # skip header
        line = line.strip()
        if line:
            name, weight = line.split(",")
            items.append(Item(name, int(weight)))

# read containers.csv
with open("containers.csv", "r") as fileref:
    for line in fileref.readlines()[1:]: # skip header
        line = line.strip()
        if line:
            name, empty_weight, capacity = line.split(",")
            container = Container(name, int(empty_weight), int(capacity))
            containers.append(container)

# dictionaries for efficient lookup 
items_dict = {item.name: item for item in items}
containers_dict = {c.name: c for c in containers}

# functions
def select_container():
    """
    Prompts the user to select a container.
    If name of container is not found, the user is prompted again.
    """
    container_name = input("Enter the name of the container: ")

    if container_name in containers_dict:
        return containers_dict[container_name]
    
    # if container not found:
    print(f'"{container_name}" not found. Try again.')
    return select_container()

def main_menu(container) -> None:
    """ 
    Main menu of the program.

    Options:
        1 - Loot item
        2 - List looted items
        0 - Quit program

    An invalid input redisplays the menu.
    """
    # display menu options:
    print("==================================")
    print("Enter your choice:")
    print("1. Loot item.")
    print("2. List looted items.")
    print("0. Quit.")
    print("==================================")

    option = input()

    if option == "1":
        loot_item(container)
    elif option == "2":
        loot_list(container)
    elif option == "0":
        return # quit program
    else:
        main_menu(container) # redisplay menu if invalid input given

def loot_item(container) -> None:
    """
    Prompts the user to enter the name of an item to loot into the container.
    If the item exists and fits, it is added to the container.
    If the item exists but does not fit, it is not looted.
    If the item does not exist, the user is prompted again.
    """
    name = input("Enter the name of the item: ")
    
    # search for item by name
    found_item = items_dict.get(name)

    # when item is not found, prompt to re-try
    if not found_item:
        print(f'"{name}" not found. Try again.')
        return loot_item(container)

    # check if item can fit into container
    if found_item.weight <= container.remaining_capacity():
        container.contents.append(found_item)
        print(f'Success! Item "{found_item.name}" stored in container "{container.name}".')
    else:
        print(f'Failure! Item "{found_item.name}" NOT stored in container "{container.name}".')

    # return to main menu
    main_menu(container)

def loot_list(container) -> None:
    """
    Prints all items currently stored in a container.
    """
    used_weight = sum(item.weight for item in container.contents)

    print(f"{container.name} (total weight: {container.total_weight()}, empty weight: {container.empty_weight}, capacity: {used_weight}/{container.capacity})")
    
    for item in container.contents:
        print(f"   {item.name} (weight: {item.weight})")

    # return to main menu
    main_menu(container)

# print summary of total items and containers
print(f"Initialised {len(items) + len(containers)} items including {len(containers)} containers.\n")

# test program
if __name__ == "__main__":
    selected_container = select_container() # user selects a container
    main_menu(selected_container) # main menu started after container is selected