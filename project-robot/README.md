Task 1: Rabbytes' age (4 marks)
In Task 1, you will write a program that allows a user to create and store new rabbytes. Each rabbit is identified by a unique name. The program also allows the user to enter a rabbit's age.

Read through the following scenario to get started.


Main menu
The program prompt of the main menu looks like this:

==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
0. Quit.
==================================

If the user inputs 1, 2, 3 or 0, it runs the corresponding function. Otherwise, the prompt is simply printed again. See example 1.

We recommend you create a function for each menu option.

1. Create a Rabbit
Upon inputting 1, the program will then print the prompt.

Input the new rabbit's name:
If the user enters a new name, the program returns to the menu and prints the main prompt.

Otherwise, the program prints

That name is already in the database.
Input the new rabbit's name:
and repeat this until the user inputs a new name. See example 2.

2. Input Age of a Rabbit
Upon inputting 2, the program will then print the prompt.

Input the rabbit's name:
If the user inputs a name (e.g. rabbie) that is already in the database, the program asks for the rabbit's age:

Input the rabbit's name:
rabbie
Input rabbie's age:
2
It then returns to the main menu and prints the main prompt.

If the user inputs a name that does not exist, the program prints

That name is not in the database.
Input the rabbit's name:
until an existing name is provided. See example 3.

We assume that:
- the age input is an integer, 
- the user will only pick option 2 if a rabbit has already been created,
- the user can freely set the age of a rabbit, even if it already has one. It will be updated.

3. List Rabbytes
Upon inputting 3, the program will then print

Rabbytes:
rabbie (42)
not_rabbie (Unknown)
if two rabbytes, rabbie and not_rabbie, have been created before, and if rabbie's age (42) has been input, and not_rabbie's age hasn't. See example 4.

Display the rabbytes in the order they were created.

Examples
User inputs are in bold font in the following examples.

Example 1

==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
0. Quit.
==================================
foo
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
0. Quit.
==================================
0


Example 2

==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
0. Quit.
==================================
1
Input the new rabbit's name:
undercover_robbie
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
0. Quit.
==================================
1
Input the new rabbit's name:
undercover_robbie
That name is already in the database.
Input the new rabbit's name:
robbie_the_rabbit
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
0. Quit.
==================================
0


Example 3

==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
0. Quit.
==================================
1
Input the new rabbit's name:
rabbie
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
0. Quit.
==================================
2
Input the rabbit's name:
bob
That name is not in the database.
Input the rabbit's name:
rabbie
Input rabbie's age:
2
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
0. Quit.
==================================
0


Example 4

==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
0. Quit.
==================================
3
Rabbytes:
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
0. Quit.
==================================
1
Input the new rabbit's name:
rabbie
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
0. Quit.
==================================
1
Input the new rabbit's name:
not_rabbie 
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
0. Quit.
==================================
2
Input the rabbit's name:
rabbie
Input rabbie's age:
42
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
0. Quit.
==================================
3
Rabbytes:
rabbie (42)
not_rabbie (Unknown)
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
0. Quit.
==================================
0

Task 2: Rabbytes' lineage (4 marks)
In Task 2, you will write a program that, on top of the previous options, allows the user to specify a parent/kitten relationship. 

Read through the following scenario to get started.


Main menu
The main prompt now has an extra two options:

==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
0. Quit.
==================================

We recommend you create a function for each menu option, and reuse functions you have written (by improving them if need be) if possible.

4. Create a parental relationship
This menu allows the user to indicate a parental relationship between two rabbytes, by first inputting the name of the parent, then the name of the kitten.

Input the parent's name:
Anakin
Input the kitten's name:
Luke
If either name does not correspond to an existing rabbit, a rabbit with that name is created, as it would be if that name was provided through option 1 of the menu. See example 1.

You do not need to verify any consistency of the input. In particular, you may suppose that the user and the automated tests will:
- ensure that the number of parents is between 0 and 2.
- a rabbit cannot be their own ancester.
However, make no other assumptions as to how rabbytes reproduce.

5. List direct family of a rabbit
This menu asks the user to enter a name, and then displays its parents and kittens.

Input the rabbit's name:
Anakin
Parents of Anakin:
Kittens of Anakin:
Leia
Luke
If the input name is not a known rabbit, the program prints

That name is not in the database.
Input the rabbit's name:  
until a known name is provided. The parents and kittens are then displayed as above. See example 2.

Assume that the user (and the automated tests) will only pick option 5 if a rabbit has already been created.

Display the names of the parents and the kittens in alphabetical order. You may use Python's built-in sorting utilities, see Sorting techniques (Python Software Foundation n.d.).

Examples
User inputs are in bold font in the following examples.

Example 1

==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
0. Quit.
==================================
4
Input the parent's name:
Anakin
Input the kitten's name:
Luke
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
0. Quit.
==================================
1
Input the new rabbit's name:
Leia
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
0. Quit.
==================================
4
Input the parent's name:
Anakin
Input the kitten's name:
Leia
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
0. Quit.
==================================
3
Rabbytes:
Anakin (Unknown)
Luke (Unknown)
Leia (Unknown)
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
0. Quit.
==================================
5
Input the rabbit's name:
Anakin
Parents of Anakin:
Kittens of Anakin:
Leia
Luke
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
0. Quit.
==================================
5
Input the rabbit's name:
Leia
Parents of Leia:
Anakin
Kittens of Leia:
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
0. Quit.
==================================
0


Example 2

==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
0. Quit.
==================================
4
Input the parent's name:
Anakin
Input the kitten's name:
Leia
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
0. Quit.
==================================
5
Input the rabbit's name:
Luke
That name is not in the database.
Input the rabbit's name:
Leia
Parents of Leia:
Anakin
Kittens of Leia:
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
0. Quit.
==================================
0

Task 3: Rabbytes' extended universe (2 marks)
Read through the following scenario to get started.


Main menu
The main prompt now has an extra option:

==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
6. Find Cousins of a Rabbit.
0. Quit.
==================================

We recommend you create a function for each menu option, and reuse functions you have written (by improving them if need be) if possible.

6. Find cousins of a rabbit
This menu allows the user to list the cousins of a rabbit. A cousin is a kitten of a sibling of a parent.

Input the rabbit's name:
cousin1
Cousins of cousin1:
cousin2
Similar to menu option 5, it asks the user for a name again

That name is not in the database.
Input the rabbit's name:
until it corresponds to one in the database. See example 1.

Display the names of the cousins in alphabetical order. You may use Python's built-in sorting utilities, see Sorting techniques (Python Software Foundation n.d.).

A rabbit cannot be its own cousin. Every other rabbit can.

Examples
User inputs are in bold font in the following examples.

Example 1

==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
6. Find Cousins of a Rabbit.
0. Quit.
==================================
4
Input the parent's name:
grandma
Input the kitten's name:
dad1
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
6. Find Cousins of a Rabbit.
0. Quit.
==================================
4
Input the parent's name:
grandma
Input the kitten's name:
dad2
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
6. Find Cousins of a Rabbit.
0. Quit.
==================================
4
Input the parent's name:
dad1
Input the kitten's name:
cousin1
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
6. Find Cousins of a Rabbit.
0. Quit.
==================================
4
Input the parent's name:
dad2
Input the kitten's name:
cousin2
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
6. Find Cousins of a Rabbit.
0. Quit.
==================================
6
Input the rabbit's name:
cousin1
Cousins of cousin1:
cousin2
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
6. Find Cousins of a Rabbit.
0. Quit.
==================================
0

Task 4: Items and containers (2 marks)
In Task 4, you will write a program that reads items and containers from files items.csv and containers.csv, and prints the list of items.

For this and following tasks, do not create files or write into existing files.

As in previous assignments, you are allowed to use any standard Python feature and module. In particular, sorted can be useful here.

We recommend that you read all tasks to plan the design of your program in order to minimise the refactoring effort between tasks.

Read through the following scenario to get started.


Items
An item has:

a name, and

a weight.

We recommend you create a class to represent items.

Containers
A container has: 

a name,

an empty weight, i.e. their weight when they are empty, and

a weight capacity, i.e. the maximum combined weight that the container can hold.

- Two copies of the same item or container can exist. If two items or containers have the same name, then they have the same characteristics (e.g. weight).
- Throughout the assignment, all weights and weight-related measures (i.e. weight capacities) are non-negative integers.

We recommend you create a class to represent containers.

Expected output
In the output below, notice "47 items". This is because the containers are included in this count.

There are no user inputs in the following example.

Initialised 47 items including 15 containers.

Items:
A normal cheese platter (weight: 1000)
A rock (weight: 1)
Bhagya's publications (weight: 8002)
Charlie's unread emails (weight: 247)
Chloe's half baked ideas (weight: 5)
Chloe's late assignments (weight: 999999)
Crimpy's destroyed cat toys (weight: 27)
Ed's forum posts (weight: 678)
Elena's fishing count (weight: 3500)
Fibonnaci's rabbytes family tree (weight: 144)
Fibonnaci's recursive call count (weight: 10946)
Gabe's Steam game library (weight: 0)
Hui's Hidden Hamster Hoard (weight: 3141)
Lifi's browser tabs (weight: 1337)
Liz's brain cell cluster (weight: 3)
Michael's stack of unmarked assignments (weight: 10000)
Paul's cringe tiktok compilation (weight: 23)
Paul's missing aura points (weight: 22)
Paul's only frontal lobe (weight: 9)
Pierre's daily cheese wheel (weight: 100)
Pierre's funny meme collection (weight: 0)
Pierre's meme collection (weight: 9001)
Pierre's outdated meme collection (weight: 9001)
Pierre's secret meme collection (weight: 420)
Rehan's Book collection (weight: 7005)
Robbie's final drop of sanity (weight: 0)
Robbie's shower thoughts (weight: 150)
Sam's water pouch (weight: 1)
Tan's Tamagotchi Support Group (weight: 410)
Taylor's ex-lovers list (weight: 999)
Vanessa's hit list (weight: 299)
Vanessa's secret gold stash (weight: 2028)

Containers:
A backpack (total weight: 40, empty weight: 40, capacity: 0/5000)
A carrybag for pets (total weight: 50, empty weight: 50, capacity: 0/2000)
A coles shopping bag (total weight: 1, empty weight: 1, capacity: 0/1000)
A container (total weight: 100, empty weight: 100, capacity: 0/250000)
A delicate flower vase (total weight: 5, empty weight: 5, capacity: 0/25)
A full bag of chips (total weight: 2, empty weight: 2, capacity: 0/5)
A large pouch (total weight: 3, empty weight: 3, capacity: 0/80)
A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
A small pouch (total weight: 1, empty weight: 1, capacity: 0/20)
A suitcase (total weight: 100, empty weight: 100, capacity: 0/20000)
A wheelbarrow (total weight: 100, empty weight: 100, capacity: 0/10000)
A woolworths shopping bag (total weight: 1, empty weight: 1, capacity: 0/1200)
Joey's water bowl (total weight: 2, empty weight: 2, capacity: 0/20)
One of those blue ikea tote bags (total weight: 3, empty weight: 3, capacity: 0/8000)

Task 5: Looting items (5 marks)
Read through the following scenario to get started.


After reading all items and containers, do not print them, but instead ask the user for a container to pick for the adventure. For example,

Enter the name of the container: A backpack
Main menu
Then, a menu with three options will be shown repeatedly. The program prompt of the main menu looks like:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1. Loot item.
Upon entering 1, the program will then ask for the name of an item to loot. If the item can fit in the container given the remaining capacity, the program indicates so, as shown in the following.

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A rock
Success! Item "A rock" stored in container "A backpack".

If, instead, the remaining capacity is not sufficient to store the item, the item is not looted:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Fibonnaci's recursive call count
Failure! Item "Fibonnaci's recursive call count" NOT stored in container "A backpack".

If the item's name is not one of the known items, then the user is asked for the name again:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A smaller Fibonnaci's recursive call count
"A smaller Fibonnaci's recursive call count" not found. Try again.
Enter the name of the item: Fibonnaci's rabbytes family tree
Success! Item "Fibonnaci's rabbytes family tree" stored in container "A backpack".

See Example 1 below for a complete example.

Consider using exceptions (including custom ones) to handle the case where a container cannot store an item.

2. List looted items.
Upon entering 2, the program will then print the container and the list of content, in the order they have been looted:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A backpack (total weight: 186, empty weight: 40, capacity: 146/5000)
   A rock (weight: 1)
   Fibonnaci's rabbytes family tree (weight: 144)
   A rock (weight: 1)

Notice how the total weight and capacity of the backpack are updated based on the contents.

Examples
User inputs are in bold font in the following examples.

Example 1

Initialised 47 items including 15 containers.

Enter the name of the container: A backpack
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A rock
Success! Item "A rock" stored in container "A backpack".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Fibonnaci's recursive call count
Failure! Item "Fibonnaci's recursive call count" NOT stored in container "A backpack".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A backpack (total weight: 41, empty weight: 40, capacity: 1/5000)
   A rock (weight: 1)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A smaller Fibonnaci's recursive call count
"A smaller Fibonnaci's recursive call count" not found. Try again.
Enter the name of the item: Fibonnaci's rabbytes family tree
Success! Item "Fibonnaci's rabbytes family tree" stored in container "A backpack".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A backpack (total weight: 185, empty weight: 40, capacity: 145/5000)
   A rock (weight: 1)
   Fibonnaci's rabbytes family tree (weight: 144)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A rock
Success! Item "A rock" stored in container "A backpack".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A backpack (total weight: 186, empty weight: 40, capacity: 146/5000)
   A rock (weight: 1)
   Fibonnaci's rabbytes family tree (weight: 144)
   A rock (weight: 1)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
0


Example 2

Initialised 47 items including 15 containers.

Enter the name of the container: A bag
"A bag" not found. Try again.
Enter the name of the container: A rock
"A rock" not found. Try again.
Enter the name of the container: Joey's water bowl
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Paul's only frontal lobe
Success! Item "Paul's only frontal lobe" stored in container "Joey's water bowl".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Liz's brain cell cluster
Success! Item "Liz's brain cell cluster" stored in container "Joey's water bowl".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Paul's only frontal lobe
Failure! Item "Paul's only frontal lobe" NOT stored in container "Joey's water bowl".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Liz's brain cell cluster
Success! Item "Liz's brain cell cluster" stored in container "Joey's water bowl".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Joey's water bowl (total weight: 17, empty weight: 2, capacity: 15/20)
   Paul's only frontal lobe (weight: 9)
   Liz's brain cell cluster (weight: 3)
   Liz's brain cell cluster (weight: 3)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Chloe's half baked ideas
Success! Item "Chloe's half baked ideas" stored in container "Joey's water bowl".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Sam's water pouch
Failure! Item "Sam's water pouch" NOT stored in container "Joey's water bowl".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Pierre's funny meme collection
Success! Item "Pierre's funny meme collection" stored in container "Joey's water bowl".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Joey's water bowl (total weight: 22, empty weight: 2, capacity: 20/20)
   Paul's only frontal lobe (weight: 9)
   Liz's brain cell cluster (weight: 3)
   Liz's brain cell cluster (weight: 3)
   Chloe's half baked ideas (weight: 5)
   Pierre's funny meme collection (weight: 0)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
0

Task 6: Multiple compartments (3 marks)
Read through the following scenario to get started.


An additional file, multi_containers.csv, now provides the description of containers that have multiple compartments, each behaving like an independent container. The menu itself does not change.

Container with multiple compartments
The empty weight of a container with multiple compartments is the sum of the empty weights of the compartments.

When looting an item, the item can be looted if it fits in one compartment. If it fits in multiple compartments, it is placed in the first one (in the order listed in the file). Once an item is placed in a compartment, it is not moved, even if that would allow looting more items.

Displaying a container with multiple compartments now shows the items stored in each compartment:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A coles shopping cart (total weight: 3720, empty weight: 43, capacity: 0/0)
   A coles shopping bag (total weight: 1001, empty weight: 1, capacity: 1000/1000)
      A normal cheese platter (weight: 1000)
   A backpack (total weight: 2717, empty weight: 40, capacity: 2677/5000)
      Taylor's ex-lovers list (weight: 999)
      Ed's forum posts (weight: 678)
      A normal cheese platter (weight: 1000)
   A woolworths shopping bag (total weight: 1, empty weight: 1, capacity: 0/1200)
   A coles shopping bag (total weight: 1, empty weight: 1, capacity: 0/1000)

See Example 1 for a complete example.

Consider using classes and inheritance in your program.

Your program must retain the same functionality as in Task 5, which is to say that it should be possible to select at the beginning of the program either a standard container, or a container with multiple compartments. See Example 2.

Examples
User inputs are in bold font in the following examples.

Example 1

Initialised 52 items including 20 containers.

Enter the name of the container: A coles shopping cart
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A coles shopping cart (total weight: 43, empty weight: 43, capacity: 0/0)
   A coles shopping bag (total weight: 1, empty weight: 1, capacity: 0/1000)
   A backpack (total weight: 40, empty weight: 40, capacity: 0/5000)
   A woolworths shopping bag (total weight: 1, empty weight: 1, capacity: 0/1200)
   A coles shopping bag (total weight: 1, empty weight: 1, capacity: 0/1000)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Pierre's outdated meme collection
Failure! Item "Pierre's outdated meme collection" NOT stored in container "A coles shopping cart".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: 1
"1" not found. Try again.
Enter the name of the item: A normal cheese platter
Success! Item "A normal cheese platter" stored in container "A coles shopping cart".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Taylor's ex-lovers list
Success! Item "Taylor's ex-lovers list" stored in container "A coles shopping cart".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Ed's forum posts
Success! Item "Ed's forum posts" stored in container "A coles shopping cart".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A coles shopping cart (total weight: 2720, empty weight: 43, capacity: 0/0)
   A coles shopping bag (total weight: 1001, empty weight: 1, capacity: 1000/1000)
      A normal cheese platter (weight: 1000)
   A backpack (total weight: 1717, empty weight: 40, capacity: 1677/5000)
      Taylor's ex-lovers list (weight: 999)
      Ed's forum posts (weight: 678)
   A woolworths shopping bag (total weight: 1, empty weight: 1, capacity: 0/1200)
   A coles shopping bag (total weight: 1, empty weight: 1, capacity: 0/1000)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Elena's fishing count
Failure! Item "Elena's fishing count" NOT stored in container "A coles shopping cart".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A normal cheese platter
Success! Item "A normal cheese platter" stored in container "A coles shopping cart".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A coles shopping cart (total weight: 3720, empty weight: 43, capacity: 0/0)
   A coles shopping bag (total weight: 1001, empty weight: 1, capacity: 1000/1000)
      A normal cheese platter (weight: 1000)
   A backpack (total weight: 2717, empty weight: 40, capacity: 2677/5000)
      Taylor's ex-lovers list (weight: 999)
      Ed's forum posts (weight: 678)
      A normal cheese platter (weight: 1000)
   A woolworths shopping bag (total weight: 1, empty weight: 1, capacity: 0/1200)
   A coles shopping bag (total weight: 1, empty weight: 1, capacity: 0/1000)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
0

Example 2

Initialised 52 items including 20 containers.

Enter the name of the container: A pouch
"A pouch" not found. Try again.
Enter the name of the container: A suitcase
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A rock
Success! Item "A rock" stored in container "A suitcase".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A suitcase (total weight: 101, empty weight: 100, capacity: 1/20000)
   A rock (weight: 1)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
0

Task 7: Magic containers (6 marks)
Read through the following scenario to get started.


An additional file, magic_containers.csv, now provides the description of containers that behave like containers with a single compartment, but that do no increase in weight if items are stored in them. They still have a maximum capacity, though.

Magic containers
Displaying a magic container looks like:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Bag of Holding (total weight: 40, empty weight: 40, capacity: 4910/5000)
   A normal cheese platter (weight: 1000)
   Elena's fishing count (weight: 3500)
   Tan's Tamagotchi Support Group (weight: 410)
   Pierre's funny meme collection (weight: 0)

The total weight remains equal to the empty way. The capacity is computed as for a non-magical container. See Example 1 for a complete example.

Your program must retain the same functionality as in Task 6, which is to say that it should be possible to select at the beginning any of the containers covered so far. See Example 2.

Examples
User inputs are in bold font in the following examples.

Example 1

Initialised 57 items including 25 containers.

Enter the name of the container: Bag of Holding
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Bag of Holding (total weight: 40, empty weight: 40, capacity: 0/5000)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A normal cheese platter
Success! Item "A normal cheese platter" stored in container "Bag of Holding".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Bag of Holding (total weight: 40, empty weight: 40, capacity: 1000/5000)
   A normal cheese platter (weight: 1000)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Elena's fishing count
Success! Item "Elena's fishing count" stored in container "Bag of Holding".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Vanessa's secret gold stash
Failure! Item "Vanessa's secret gold stash" NOT stored in container "Bag of Holding".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Bag of Holding (total weight: 40, empty weight: 40, capacity: 4500/5000)
   A normal cheese platter (weight: 1000)
   Elena's fishing count (weight: 3500)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Tan's Tamagotchi Support Group
Success! Item "Tan's Tamagotchi Support Group" stored in container "Bag of Holding".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Pierre's funny meme collection
Success! Item "Pierre's funny meme collection" stored in container "Bag of Holding".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Bag of Holding (total weight: 40, empty weight: 40, capacity: 4910/5000)
   A normal cheese platter (weight: 1000)
   Elena's fishing count (weight: 3500)
   Tan's Tamagotchi Support Group (weight: 410)
   Pierre's funny meme collection (weight: 0)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
0


Example 2

Initialised 57 items including 25 containers.

Enter the name of the container: A lab coat
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A lab coat (total weight: 0, empty weight: 0, capacity: 0/0)
   A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
   A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
   A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Gabe's Steam game library
Success! Item "Gabe's Steam game library" stored in container "A lab coat".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Robbie's final drop of sanity
Success! Item "Robbie's final drop of sanity" stored in container "A lab coat".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A lab coat (total weight: 0, empty weight: 0, capacity: 0/0)
   A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
      Gabe's Steam game library (weight: 0)
      Robbie's final drop of sanity (weight: 0)
   A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
   A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Robbie's shower thoughts
Success! Item "Robbie's shower thoughts" stored in container "A lab coat".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A lab coat (total weight: 150, empty weight: 0, capacity: 0/0)
   A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
      Gabe's Steam game library (weight: 0)
      Robbie's final drop of sanity (weight: 0)
   A medium pocket (total weight: 150, empty weight: 0, capacity: 150/200)
      Robbie's shower thoughts (weight: 150)
   A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
0

Task 8: Magic multiple compartments (5 marks)
Read through the following scenario to get started.


An additional file, magic_multi_containers.csv, now provides the description of containers that behave like containers with multiple compartments, and, like the other magic containers, do no increase in weight if items are stored in them. Each compartment still has a maximum capacity.

Magic containers with multiple compartments
Displaying a magic container looks like:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Professor Farnsworth's Lab Coat (total weight: 0, empty weight: 0, capacity: 0/0)
   A small pocket (total weight: 100, empty weight: 0, capacity: 100/100)
      Pierre's daily cheese wheel (weight: 100)
      Gabe's Steam game library (weight: 0)
      Robbie's final drop of sanity (weight: 0)
   A medium pocket (total weight: 186, empty weight: 0, capacity: 186/200)
      Paul's only frontal lobe (weight: 9)
      Robbie's shower thoughts (weight: 150)
      Crimpy's destroyed cat toys (weight: 27)
   A small pocket (total weight: 27, empty weight: 0, capacity: 27/100)
      Crimpy's destroyed cat toys (weight: 27)
==================================

The total weight remains equal to the empty way. The capacity is computed as for a non-magical container with multiple compartments, which is that it is computed and displayed at the compartment level. See Example 1 for a complete example.

Your program must retain the same functionality as in Task 7, which is to say that it should be possible to select at the beginning any of the containers covered so far. See Example 2.

Examples
User inputs are in bold font in the following examples.

Example 1

Initialised 60 items including 28 containers.

Enter the name of the container: Professor Farnsworth's Lab Coat
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Professor Farnsworth's Lab Coat (total weight: 0, empty weight: 0, capacity: 0/0)
   A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
   A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
   A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Pierre's daily cheese wheel
Success! Item "Pierre's daily cheese wheel" stored in container "Professor Farnsworth's Lab Coat".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Gabe's Steam game library
Success! Item "Gabe's Steam game library" stored in container "Professor Farnsworth's Lab Coat".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Professor Farnsworth's Lab Coat (total weight: 0, empty weight: 0, capacity: 0/0)
   A small pocket (total weight: 100, empty weight: 0, capacity: 100/100)
      Pierre's daily cheese wheel (weight: 100)
      Gabe's Steam game library (weight: 0)
   A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
   A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Paul's only frontal lobe
Success! Item "Paul's only frontal lobe" stored in container "Professor Farnsworth's Lab Coat".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Professor Farnsworth's Lab Coat (total weight: 0, empty weight: 0, capacity: 0/0)
   A small pocket (total weight: 100, empty weight: 0, capacity: 100/100)
      Pierre's daily cheese wheel (weight: 100)
      Gabe's Steam game library (weight: 0)
   A medium pocket (total weight: 9, empty weight: 0, capacity: 9/200)
      Paul's only frontal lobe (weight: 9)
   A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Robbie's final drop of sanity
Success! Item "Robbie's final drop of sanity" stored in container "Professor Farnsworth's Lab Coat".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Professor Farnsworth's Lab Coat (total weight: 0, empty weight: 0, capacity: 0/0)
   A small pocket (total weight: 100, empty weight: 0, capacity: 100/100)
      Pierre's daily cheese wheel (weight: 100)
      Gabe's Steam game library (weight: 0)
      Robbie's final drop of sanity (weight: 0)
   A medium pocket (total weight: 9, empty weight: 0, capacity: 9/200)
      Paul's only frontal lobe (weight: 9)
   A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Robbie's shower thoughts
Success! Item "Robbie's shower thoughts" stored in container "Professor Farnsworth's Lab Coat".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Professor Farnsworth's Lab Coat (total weight: 0, empty weight: 0, capacity: 0/0)
   A small pocket (total weight: 100, empty weight: 0, capacity: 100/100)
      Pierre's daily cheese wheel (weight: 100)
      Gabe's Steam game library (weight: 0)
      Robbie's final drop of sanity (weight: 0)
   A medium pocket (total weight: 159, empty weight: 0, capacity: 159/200)
      Paul's only frontal lobe (weight: 9)
      Robbie's shower thoughts (weight: 150)
   A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Crimpy's destroyed cat toys
Success! Item "Crimpy's destroyed cat toys" stored in container "Professor Farnsworth's Lab Coat".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Professor Farnsworth's Lab Coat (total weight: 0, empty weight: 0, capacity: 0/0)
   A small pocket (total weight: 100, empty weight: 0, capacity: 100/100)
      Pierre's daily cheese wheel (weight: 100)
      Gabe's Steam game library (weight: 0)
      Robbie's final drop of sanity (weight: 0)
   A medium pocket (total weight: 186, empty weight: 0, capacity: 186/200)
      Paul's only frontal lobe (weight: 9)
      Robbie's shower thoughts (weight: 150)
      Crimpy's destroyed cat toys (weight: 27)
   A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Crimpy's destroyed cat toys
Success! Item "Crimpy's destroyed cat toys" stored in container "Professor Farnsworth's Lab Coat".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Professor Farnsworth's Lab Coat (total weight: 0, empty weight: 0, capacity: 0/0)
   A small pocket (total weight: 100, empty weight: 0, capacity: 100/100)
      Pierre's daily cheese wheel (weight: 100)
      Gabe's Steam game library (weight: 0)
      Robbie's final drop of sanity (weight: 0)
   A medium pocket (total weight: 186, empty weight: 0, capacity: 186/200)
      Paul's only frontal lobe (weight: 9)
      Robbie's shower thoughts (weight: 150)
      Crimpy's destroyed cat toys (weight: 27)
   A small pocket (total weight: 27, empty weight: 0, capacity: 27/100)
      Crimpy's destroyed cat toys (weight: 27)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
0


Example 2

Initialised 60 items including 28 containers.

Enter the name of the container: Hermione's Satchel
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Hermione's Satchel (total weight: 3, empty weight: 3, capacity: 0/80)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Fibonnaci's rabbytes family tree
Failure! Item "Fibonnaci's rabbytes family tree" NOT stored in container "Hermione's Satchel".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Sam's water pouch
Success! Item "Sam's water pouch" stored in container "Hermione's Satchel".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Hermione's Satchel (total weight: 3, empty weight: 3, capacity: 1/80)
   Sam's water pouch (weight: 1)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
0

Task 9: Containers are items too (4 marks)
Read through the following scenario to get started.


Expand your program so that:

Containers can be looted and stored just like other items.

When looting and storing an item (including containers), it is placed in the first possible container:

if it can be stored in the current container, it is,

otherwise, containers (and other containers within) placed in the current container are tested in the order in which they were stored to determine if the item can be stored there, and

any container inside the current container is tested before any container at the same level as the current container.

Items more than one level inside a container affect the weight of all containers containing this item (but a magic container will also affect this). This means that if item X is put in non-magic container B, itself inside non-magic container A, then the weight of X both applies to A and B, and they both must have enough capacity. However, if B is magic, then the weight of X only applies to B. See Examples 1 and 2.

This type of recursive search is called a preorder depth-first search.

Examples
User inputs are in bold font in the following examples.

Example 1

Initialised 60 items including 28 containers.

Enter the name of the container: One of those blue ikea tote bags
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A container
Success! Item "A container" stored in container "One of those blue ikea tote bags".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
One of those blue ikea tote bags (total weight: 103, empty weight: 3, capacity: 100/8000)
   A container (total weight: 100, empty weight: 100, capacity: 0/250000)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Hui's Hidden Hamster Hoard
Success! Item "Hui's Hidden Hamster Hoard" stored in container "One of those blue ikea tote bags".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
One of those blue ikea tote bags (total weight: 3244, empty weight: 3, capacity: 3241/8000)
   A container (total weight: 100, empty weight: 100, capacity: 0/250000)
   Hui's Hidden Hamster Hoard (weight: 3141)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Fibonnaci's recursive call count
Failure! Item "Fibonnaci's recursive call count" NOT stored in container "One of those blue ikea tote bags".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Rehan's Book collection
Failure! Item "Rehan's Book collection" NOT stored in container "One of those blue ikea tote bags".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
One of those blue ikea tote bags (total weight: 3244, empty weight: 3, capacity: 3241/8000)
   A container (total weight: 100, empty weight: 100, capacity: 0/250000)
   Hui's Hidden Hamster Hoard (weight: 3141)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
0


Example 2

Initialised 60 items including 28 containers.

Enter the name of the container: A small pouch
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Bag of Holding
Failure! Item "Bag of Holding" NOT stored in container "A small pouch".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Hermione's Satchel
Success! Item "Hermione's Satchel" stored in container "A small pouch".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A small pouch (total weight: 4, empty weight: 1, capacity: 3/20)
   Hermione's Satchel (total weight: 3, empty weight: 3, capacity: 0/80)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Paul's only frontal lobe
Success! Item "Paul's only frontal lobe" stored in container "A small pouch".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A small pouch (total weight: 13, empty weight: 1, capacity: 12/20)
   Hermione's Satchel (total weight: 3, empty weight: 3, capacity: 0/80)
   Paul's only frontal lobe (weight: 9)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Paul's only frontal lobe
Success! Item "Paul's only frontal lobe" stored in container "A small pouch".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A small pouch (total weight: 13, empty weight: 1, capacity: 12/20)
   Hermione's Satchel (total weight: 3, empty weight: 3, capacity: 9/80)
      Paul's only frontal lobe (weight: 9)
   Paul's only frontal lobe (weight: 9)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Chloe's half baked ideas
Success! Item "Chloe's half baked ideas" stored in container "A small pouch".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Liz's brain cell cluster
Success! Item "Liz's brain cell cluster" stored in container "A small pouch".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A small pouch (total weight: 21, empty weight: 1, capacity: 20/20)
   Hermione's Satchel (total weight: 3, empty weight: 3, capacity: 9/80)
      Paul's only frontal lobe (weight: 9)
   Paul's only frontal lobe (weight: 9)
   Chloe's half baked ideas (weight: 5)
   Liz's brain cell cluster (weight: 3)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Gabe's Steam game library
Success! Item "Gabe's Steam game library" stored in container "A small pouch".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A small pouch (total weight: 21, empty weight: 1, capacity: 20/20)
   Hermione's Satchel (total weight: 3, empty weight: 3, capacity: 9/80)
      Paul's only frontal lobe (weight: 9)
   Paul's only frontal lobe (weight: 9)
   Chloe's half baked ideas (weight: 5)
   Liz's brain cell cluster (weight: 3)
   Gabe's Steam game library (weight: 0)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Robbie's shower thoughts
Failure! Item "Robbie's shower thoughts" NOT stored in container "A small pouch".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A small pouch (total weight: 21, empty weight: 1, capacity: 20/20)
   Hermione's Satchel (total weight: 3, empty weight: 3, capacity: 9/80)
      Paul's only frontal lobe (weight: 9)
   Paul's only frontal lobe (weight: 9)
   Chloe's half baked ideas (weight: 5)
   Liz's brain cell cluster (weight: 3)
   Gabe's Steam game library (weight: 0)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Vanessa's hit list
Failure! Item "Vanessa's hit list" NOT stored in container "A small pouch".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Bag of Holding
Success! Item "Bag of Holding" stored in container "A small pouch".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A small pouch (total weight: 21, empty weight: 1, capacity: 20/20)
   Hermione's Satchel (total weight: 3, empty weight: 3, capacity: 49/80)
      Paul's only frontal lobe (weight: 9)
      Bag of Holding (total weight: 40, empty weight: 40, capacity: 0/5000)
   Paul's only frontal lobe (weight: 9)
   Chloe's half baked ideas (weight: 5)
   Liz's brain cell cluster (weight: 3)
   Gabe's Steam game library (weight: 0)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Vanessa's hit list
Success! Item "Vanessa's hit list" stored in container "A small pouch".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A small pouch (total weight: 21, empty weight: 1, capacity: 20/20)
   Hermione's Satchel (total weight: 3, empty weight: 3, capacity: 49/80)
      Paul's only frontal lobe (weight: 9)
      Bag of Holding (total weight: 40, empty weight: 40, capacity: 299/5000)
         Vanessa's hit list (weight: 299)
   Paul's only frontal lobe (weight: 9)
   Chloe's half baked ideas (weight: 5)
   Liz's brain cell cluster (weight: 3)
   Gabe's Steam game library (weight: 0)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Arnaud's Oven of Crispiness
Success! Item "Arnaud's Oven of Crispiness" stored in container "A small pouch".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Lifi's browser tabs
Success! Item "Lifi's browser tabs" stored in container "A small pouch".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A small pouch (total weight: 21, empty weight: 1, capacity: 20/20)
   Hermione's Satchel (total weight: 3, empty weight: 3, capacity: 49/80)
      Paul's only frontal lobe (weight: 9)
      Bag of Holding (total weight: 40, empty weight: 40, capacity: 1736/5000)
         Vanessa's hit list (weight: 299)
         Arnaud's Oven of Crispiness (total weight: 100, empty weight: 100, capacity: 0/250000)
         Lifi's browser tabs (weight: 1337)
   Paul's only frontal lobe (weight: 9)
   Chloe's half baked ideas (weight: 5)
   Liz's brain cell cluster (weight: 3)
   Gabe's Steam game library (weight: 0)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Pierre's outdated meme collection
Success! Item "Pierre's outdated meme collection" stored in container "A small pouch".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A small pouch (total weight: 21, empty weight: 1, capacity: 20/20)
   Hermione's Satchel (total weight: 3, empty weight: 3, capacity: 49/80)
      Paul's only frontal lobe (weight: 9)
      Bag of Holding (total weight: 40, empty weight: 40, capacity: 1736/5000)
         Vanessa's hit list (weight: 299)
         Arnaud's Oven of Crispiness (total weight: 100, empty weight: 100, capacity: 9001/250000)
            Pierre's outdated meme collection (weight: 9001)
         Lifi's browser tabs (weight: 1337)
   Paul's only frontal lobe (weight: 9)
   Chloe's half baked ideas (weight: 5)
   Liz's brain cell cluster (weight: 3)
   Gabe's Steam game library (weight: 0)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
0


Example 3

Initialised 60 items including 28 containers.

Enter the name of the container: The Stomach of that Penguin from Madagascar
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A small pouch
Success! Item "A small pouch" stored in container "The Stomach of that Penguin from Madagascar".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Rambo's Cargo Pants
Success! Item "Rambo's Cargo Pants" stored in container "The Stomach of that Penguin from Madagascar".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
The Stomach of that Penguin from Madagascar (total weight: 3, empty weight: 3, capacity: 1/80)
   A small pouch (total weight: 1, empty weight: 1, capacity: 0/20)
   Rambo's Cargo Pants (total weight: 0, empty weight: 0, capacity: 0/0)
      A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
      A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Robbie's shower thoughts
Success! Item "Robbie's shower thoughts" stored in container "The Stomach of that Penguin from Madagascar".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Pierre's daily cheese wheel
Success! Item "Pierre's daily cheese wheel" stored in container "The Stomach of that Penguin from Madagascar".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
The Stomach of that Penguin from Madagascar (total weight: 3, empty weight: 3, capacity: 1/80)
   A small pouch (total weight: 1, empty weight: 1, capacity: 0/20)
   Rambo's Cargo Pants (total weight: 0, empty weight: 0, capacity: 0/0)
      A small pocket (total weight: 100, empty weight: 0, capacity: 100/100)
         Pierre's daily cheese wheel (weight: 100)
      A medium pocket (total weight: 150, empty weight: 0, capacity: 150/200)
         Robbie's shower thoughts (weight: 150)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
      A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Paul's cringe tiktok compilation
Success! Item "Paul's cringe tiktok compilation" stored in container "The Stomach of that Penguin from Madagascar".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Crimpy's destroyed cat toys
Success! Item "Crimpy's destroyed cat toys" stored in container "The Stomach of that Penguin from Madagascar".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
The Stomach of that Penguin from Madagascar (total weight: 3, empty weight: 3, capacity: 51/80)
   A small pouch (total weight: 1, empty weight: 1, capacity: 0/20)
   Rambo's Cargo Pants (total weight: 0, empty weight: 0, capacity: 0/0)
      A small pocket (total weight: 100, empty weight: 0, capacity: 100/100)
         Pierre's daily cheese wheel (weight: 100)
      A medium pocket (total weight: 150, empty weight: 0, capacity: 150/200)
         Robbie's shower thoughts (weight: 150)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
      A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
   Paul's cringe tiktok compilation (weight: 23)
   Crimpy's destroyed cat toys (weight: 27)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Paul's missing aura points
Success! Item "Paul's missing aura points" stored in container "The Stomach of that Penguin from Madagascar".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
The Stomach of that Penguin from Madagascar (total weight: 3, empty weight: 3, capacity: 73/80)
   A small pouch (total weight: 1, empty weight: 1, capacity: 0/20)
   Rambo's Cargo Pants (total weight: 0, empty weight: 0, capacity: 0/0)
      A small pocket (total weight: 100, empty weight: 0, capacity: 100/100)
         Pierre's daily cheese wheel (weight: 100)
      A medium pocket (total weight: 150, empty weight: 0, capacity: 150/200)
         Robbie's shower thoughts (weight: 150)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
      A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
   Paul's cringe tiktok compilation (weight: 23)
   Crimpy's destroyed cat toys (weight: 27)
   Paul's missing aura points (weight: 22)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Paul's only frontal lobe
Success! Item "Paul's only frontal lobe" stored in container "The Stomach of that Penguin from Madagascar".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
The Stomach of that Penguin from Madagascar (total weight: 3, empty weight: 3, capacity: 73/80)
   A small pouch (total weight: 1, empty weight: 1, capacity: 0/20)
   Rambo's Cargo Pants (total weight: 0, empty weight: 0, capacity: 0/0)
      A small pocket (total weight: 100, empty weight: 0, capacity: 100/100)
         Pierre's daily cheese wheel (weight: 100)
      A medium pocket (total weight: 159, empty weight: 0, capacity: 159/200)
         Robbie's shower thoughts (weight: 150)
         Paul's only frontal lobe (weight: 9)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
      A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
   Paul's cringe tiktok compilation (weight: 23)
   Crimpy's destroyed cat toys (weight: 27)
   Paul's missing aura points (weight: 22)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Robbie's final drop of sanity
Success! Item "Robbie's final drop of sanity" stored in container "The Stomach of that Penguin from Madagascar".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
The Stomach of that Penguin from Madagascar (total weight: 3, empty weight: 3, capacity: 73/80)
   A small pouch (total weight: 1, empty weight: 1, capacity: 0/20)
   Rambo's Cargo Pants (total weight: 0, empty weight: 0, capacity: 0/0)
      A small pocket (total weight: 100, empty weight: 0, capacity: 100/100)
         Pierre's daily cheese wheel (weight: 100)
      A medium pocket (total weight: 159, empty weight: 0, capacity: 159/200)
         Robbie's shower thoughts (weight: 150)
         Paul's only frontal lobe (weight: 9)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
      A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
   Paul's cringe tiktok compilation (weight: 23)
   Crimpy's destroyed cat toys (weight: 27)
   Paul's missing aura points (weight: 22)
   Robbie's final drop of sanity (weight: 0)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A small pouch
Success! Item "A small pouch" stored in container "The Stomach of that Penguin from Madagascar".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
The Stomach of that Penguin from Madagascar (total weight: 3, empty weight: 3, capacity: 74/80)
   A small pouch (total weight: 1, empty weight: 1, capacity: 0/20)
   Rambo's Cargo Pants (total weight: 0, empty weight: 0, capacity: 0/0)
      A small pocket (total weight: 100, empty weight: 0, capacity: 100/100)
         Pierre's daily cheese wheel (weight: 100)
      A medium pocket (total weight: 159, empty weight: 0, capacity: 159/200)
         Robbie's shower thoughts (weight: 150)
         Paul's only frontal lobe (weight: 9)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
      A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
   Paul's cringe tiktok compilation (weight: 23)
   Crimpy's destroyed cat toys (weight: 27)
   Paul's missing aura points (weight: 22)
   Robbie's final drop of sanity (weight: 0)
   A small pouch (total weight: 1, empty weight: 1, capacity: 0/20)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Handy Haversack
Success! Item "Handy Haversack" stored in container "The Stomach of that Penguin from Madagascar".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
The Stomach of that Penguin from Madagascar (total weight: 3, empty weight: 3, capacity: 79/80)
   A small pouch (total weight: 1, empty weight: 1, capacity: 0/20)
   Rambo's Cargo Pants (total weight: 0, empty weight: 0, capacity: 0/0)
      A small pocket (total weight: 100, empty weight: 0, capacity: 100/100)
         Pierre's daily cheese wheel (weight: 100)
      A medium pocket (total weight: 159, empty weight: 0, capacity: 159/200)
         Robbie's shower thoughts (weight: 150)
         Paul's only frontal lobe (weight: 9)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
      A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
      A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
   Paul's cringe tiktok compilation (weight: 23)
   Crimpy's destroyed cat toys (weight: 27)
   Paul's missing aura points (weight: 22)
   Robbie's final drop of sanity (weight: 0)
   A small pouch (total weight: 1, empty weight: 1, capacity: 0/20)
   Handy Haversack (total weight: 5, empty weight: 5, capacity: 0/0)
      A small pouch (total weight: 1, empty weight: 1, capacity: 0/20)
      A large pouch (total weight: 3, empty weight: 3, capacity: 0/80)
      A small pouch (total weight: 1, empty weight: 1, capacity: 0/20)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Vanessa's hit list
Failure! Item "Vanessa's hit list" NOT stored in container "The Stomach of that Penguin from Madagascar".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
0
