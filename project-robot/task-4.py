"""
This program reads item and container information from CSV files (items.csv and containers.csv) and displays a list of all items and containers.

Each item has:
    - a name 
    - weight
Each container has 
    - a name 
    - an empty weight
    - a weight capacity

Containers can hold items, and their total weight is the sum of their empty weight plus weights of contained items.
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

# print summary of total items and containers
print(f"Initialised {len(items) + len(containers)} items including {len(containers)} containers.\n")

# print all items in alphabetical order
print("Items:")
items_dict = {i.name: i for i in items}
for item_name in sorted(items_dict.keys()):
    i = items_dict[item_name]
    print(f"{i.name} (weight: {i.weight})")
print()

# print all containers in alphabetical order
print("Containers:")
containers_dict = {c.name: c for c in containers}
for container_name in sorted(containers_dict.keys()):
    c = containers_dict[container_name]
    used_weight = sum(item.weight for item in c.contents)
    print(f"{c.name} (total weight: {c.total_weight()}, empty weight: {c.empty_weight}, capacity: {used_weight}/{c.capacity})")
print()