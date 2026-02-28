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
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
    
    def is_container(self) -> bool:
        """ Returns True if this item is a container. """
        return False
    
    def is_magic(self) -> bool:
        """ Returns True if this is a magic container. """
        return False

    def total_weight(self) -> int:
        """ Total weight of normal item is just its own weight. """
        return self.weight


class Container(Item):
    """
    Container class represents a container that can hold items.

    Instance Variables:
        name (str): Name of the container.
        empty_weight (int): Weight of the container when empty.
        capacity (int): Maximum total weight of items placed inside container.
        contents (List[Item]): List of items currently inside the container.
    """
    def __init__(self, name: str, empty_weight: int, capacity: int):
        self.name = name
        self.empty_weight = empty_weight
        self.capacity = capacity
        self.contents = []
    
    def is_container(self) -> bool:
        """ Returns True if this item is a container. """
        return True
    
    def has_subcontainers(self) -> bool:
        """ Returns True if this container has subcontainers. """
        return False

    def total_weight(self) -> int:
        """ 
        Returns total weight of the container including its contents.
        If an item inside is a container, its own total weight is included.
        """
        contents_weight = 0
        for item in self.contents:
            if item.is_container():
                contents_weight += item.total_weight()
            else:
                contents_weight += item.weight
        return self.empty_weight + contents_weight

    def remaining_capacity(self) -> int: 
        """ 
        Returns remaining weight capacity of the container.
        Magic container contents do not increase the weight. 
        """
        used_capacity = 0
        for item in self.contents:
            if item.is_container():
                if item.is_magic():
                    used_capacity += item.empty_weight  # magic containers don't add content weight
                else:
                    used_capacity += item.total_weight()  # regular containers add full weight
            else:
                used_capacity += item.weight
        return self.capacity - used_capacity
    
    def loot(self, item: Item) -> bool:
        """
        Loot an item into this container.
        Containers are copied when stored to avoid nesting the same object.
        """
        # make a stored copy if looting a container
        if item.is_container():

            # if magic multicontainer
            if type(item) == MagicMultiContainer:
                sub_list = []
                for sc in item.subcontainers:
                    new_sc = SubContainer(sc.name, sc.empty_weight, sc.capacity)
                    sub_list.append(new_sc)
                temp_multi = MultiContainer("temp", sub_list)
                item_to_store = MagicMultiContainer(item.name, temp_multi)

            # if regular multicontainer
            elif type(item) == MultiContainer:
                sub_list = []
                for sc in item.subcontainers:
                    new_sc = SubContainer(sc.name, sc.empty_weight, sc.capacity)
                    sub_list.append(new_sc)
                item_to_store = MultiContainer(item.name, sub_list)

            # if magic single container
            elif type(item) == MagicContainer:
                base_cont = Container(item.name, item.empty_weight, item.capacity)
                item_to_store = MagicContainer(item.name, base_cont)

            # if normal container / subcontainer
            else:  
                item_to_store = type(item)(item.name, item.empty_weight, item.capacity)
        
        else:
            item_to_store = item

        # determine weight to check
        if item_to_store.is_container():
            if item_to_store.is_magic():
                item_weight = item_to_store.empty_weight
            else:
                item_weight = item_to_store.total_weight()
        else:
            item_weight = item_to_store.weight

        # try current container 
        if item_weight <= self.remaining_capacity():
            self.contents.append(item_to_store)
            return True

        # try magic containers if no subcontainers
        if not self.has_subcontainers():
                for stored_item in self.contents:
                    if stored_item.is_container() and stored_item.is_magic():
                        if stored_item.loot(item_to_store):
                            return True
                return False

        # try nested containers
        for stored_item in self.contents:
            if stored_item.is_container() and stored_item.loot(item_to_store):
                    return True

        # could not loot anywhere
        return False
    
    def contains_container(self, target) -> bool:
        """ 
        Returns True if this container or an of its subcontainers contains the target container.
        """
        # check direct match
        if self is target:
            return True
        
        # check nested subcontainers (for MultiContainers)
        for sc in self.get_subcontainers():
            if sc.contains_container(target):
                return True

        return False
    
    def get_subcontainers(self) -> list:
        """ 
        Returns list of subcontainers. 
        Returns empty list for regular containers that do not have subcontainers. 
        """
        return []

# subcontainer for multi-container compartments
class SubContainer(Container):
    """ 
    A subcontainer inside a multi-container. 
    """
    pass

class MultiContainer(Container):
    """ 
    Multicontainer class represents a container that has multiple compartments (subcontainers). 

    Instance variables:
        name (str): Name of multicontainer.
        subcontainers (List[SubContainer]): List of subcontainers.
        empty_weight (int): Sum of empty weights of all subcontainers.
        capacity (int): Total capacity (0 since all items go into subcontainers).
        contents (List[Item]): Not used as multicontainers do not store items directly.
    """
    def __init__(self, name: str, subcontainers: list[SubContainer]):
        self.name = name
        self.subcontainers = subcontainers 
        self.empty_weight = sum(sc.empty_weight for sc in subcontainers)
        self.capacity = 0
        self.contents = [] # multicontainer does not store items directly
    
    def has_subcontainers(self) -> bool:
        """ Returns True if this container has subcontainers. """
        return True

    def total_weight(self) -> int:
        """ Total weight including all subcontainer and their contents. """
        total = self.empty_weight
        for sc in self.subcontainers:
            for i in sc.contents:
                if i.is_container():
                    total += i.total_weight()
                else:
                    total += i.weight
        return total

    def remaining_capacity(self) -> int:
        """ Returns total remaining capacities of all subcontainers. """
        return sum(sc.remaining_capacity() for sc in self.subcontainers)

    def loot(self, item: Item) -> bool:
        """
        Try to loot item into this multi-container.
        Loot each subcontainer in order (preorder depth-first).
        """
        # handle self-looting by creating a copy
        if (item.is_container() and 
            item.name == self.name and 
            type(item) == type(self)):
            # Create a deep copy with EMPTY subcontainers
            sub_list = []
            for sc in self.subcontainers:
                new_sc = SubContainer(sc.name, sc.empty_weight, sc.capacity)
                sub_list.append(new_sc)
            item_to_loot = MultiContainer(self.name, sub_list)
        else:
            item_to_loot = item
        
        # try each subcontainer in order
        for sc in self.subcontainers:
            if sc is item_to_loot:
                continue
            if item_to_loot.is_container() and item_to_loot.contains_container(sc):
                continue
            if sc.loot(item_to_loot):
                return True

        return False
    
    def get_subcontainers(self):
        """ Returns list of subcontainers. """
        return self.subcontainers

class MagicContainer(Container):
    """
    A magic container behaves like container with a single compartment, but total weight does not increase when items are looted into it.

    Instance variables:
        name (str): Name of magic container.
        empty_weight (int): Weight of the base container.
        capacity (int): Maximum combined weight the container can hold.
        contents (List[Item]): Items stored in this container (weight does not count).
    """
    def __init__(self, name: str, base_container: Container):
        super().__init__(name, base_container.empty_weight, base_container.capacity)
        self.contents = []
    
    def is_magic(self) -> bool:
        """ Returns True if this is a magic container. """
        return True

    def total_weight(self) -> int:
        """ Total weight is equal to empty_weight. """
        return self.empty_weight

class MagicMultiContainer(MultiContainer):
    """ A magic multicontainer behaves like multicontainer, but total weight does not increase when items are looted into it. """
    def __init__(self, name:str, base_multi: MultiContainer):
        sub_list = []
        for sc in base_multi.subcontainers:
            sub_list.append(SubContainer(sc.name, sc.empty_weight, sc.capacity))
        super().__init__(name, sub_list)
    
    def is_magic(self) -> bool:
        """Returns True if this is a magic container."""
        return True

    def total_weight(self) -> int:
        """ Total weight is equal to empty_weight. """
        return self.empty_weight

    def loot(self, item: Item) -> bool:
        """
        Loot into magic multi-container.
        Same as MultiContainer but weight does not affect parent.
        Loot each subcontainer in order (preorder depth-first).
        """
        # handle self-looting by creating a copy
        if (item.is_container() and 
            item.name == self.name and 
            type(item) == type(self)):
            # Create a deep copy with EMPTY subcontainers
            sub_list = []
            for sc in self.subcontainers:
                new_sc = SubContainer(sc.name, sc.empty_weight, sc.capacity)
                sub_list.append(new_sc)
            temp_multi = MultiContainer("temp", sub_list)
            item_to_loot = MagicMultiContainer(self.name, temp_multi)
        else:
            item_to_loot = item
        
        # try each subcontainer in order
        for sc in self.subcontainers:
            if sc is item_to_loot:
                continue
            if item_to_loot.is_container() and item_to_loot.contains_container(sc):
                continue
            if sc.loot(item_to_loot):
                return True
        
        return False

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
            items.append(container)  # Containers are also items

# read multi_containers.csv
with open("multi_containers.csv", "r") as fileref:
    for line in fileref.readlines()[1:]: # skip header
        line = line.strip()
        if line:
            parts = [p.strip() for p in line.split(",")]
            name = parts[0]
            sub_names = parts[1:]

            sub_list = []
            for sub in sub_names:
                found_container = None
                for c in containers:
                    if c.name == sub:
                        found_container = c
                        break
                if found_container is not None:
                    sub_list.append(SubContainer(found_container.name, found_container.empty_weight, found_container.capacity))

            multi = MultiContainer(name, sub_list)
            containers.append(multi)
            items.append(multi)  # Containers are also items

# read magic_containers.csv
with open("magic_containers.csv", "r") as fileref:
    for line in fileref.readlines()[1:]: # skip header
        line = line.strip()
        if line:
            name, base_name = [p.strip() for p in line.split(",")]

            base_container = None
            for c in containers:
                if c.name == base_name:
                    base_container = c
                    break
            
            if base_container:
                magic = MagicContainer(name, base_container)
                containers.append(magic)
                items.append(magic)  # Containers are also items

# read magic_multi_containers.csv
with open("magic_multi_containers.csv", "r") as fileref:
    for line in fileref.readlines()[1:]: # skip header
        line = line.strip()
        if line:
            name, base_name = [p.strip() for p in line.split(",")]
            base_multi = None
            for c in containers:
                if c.has_subcontainers() and c.name == base_name:
                    base_multi = c
                    break
            if base_multi:
                magic_multi = MagicMultiContainer(name, base_multi)
                containers.append(magic_multi)
                items.append(magic_multi)  # containers are also items

# functions
def select_container() -> Container:
    """
    Prompts the user to select a container.
    If name of container is not found, the user is prompted again.
    """
    container_name = input("Enter the name of the container: ")
    for c in containers:
        if c.name == container_name:
            return c
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
    # display menu options
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

def loot_item(container):
    """
    Prompts the user to enter the name of an item to loot into the container.
    If the item exists and fits, it is added to the container.
    If the item exists but does not fit, it is not looted.
    If the item does not exist, the user is prompted again.
    """
    name = input("Enter the name of the item: ")
    
    # search for item by name
    found_item = None
    for item in items:
        if item.name == name:
            found_item = item
            break

    # when item is not found
    if not found_item:
        print(f'"{name}" not found. Try again.')
        return loot_item(container)

    # check if item can fit into container
    if container.loot(found_item):
        print(f'Success! Item "{found_item.name}" stored in container "{container.name}".')
    else:
        print(f'Failure! Item "{found_item.name}" NOT stored in container "{container.name}".')

    # return to main menu
    main_menu(container)

def print_contents(container, indent: int = 0):
    """ Recursively print contents of a container with indentation. """
    indent_str = "   " * indent

    # print container
    used_capacity = sum(item.empty_weight if item.is_container() else item.weight for item in container.contents)
    
    print(f"{indent_str}{container.name} (total weight: {container.total_weight()}, empty weight: {container.empty_weight}, capacity: {used_capacity}/{container.capacity})")

    # print contents
    for item in container.contents:
        if item.is_container():
            print_contents(item, indent + 1)
        else:
            print(f"{indent_str}   {item.name} (weight: {item.weight})")

    # print subcontainers (multicontainer)
    if container.has_subcontainers():
        for sc in container.get_subcontainers():
            print_contents(sc, indent + 1)

def loot_list(container) -> None:
    """ Prints looted items in a container by calling print_contents. """
    print_contents(container)
    main_menu(container)

# print summary of total items and containers
print(f"Initialised {len(items)} items including {len(containers)} containers.\n")

# test program
if __name__ == "__main__":
    selected_container = select_container() # user selects a container
    main_menu(selected_container) # main menu started after container is selected