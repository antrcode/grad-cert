# Task 1: Username login (2 marks)

In Task 1, you will write a program that asks the user to enter a username. A successful login occurs when the user enters one of the valid usernames. The program keeps prompting the user until a valid username is provided.

The usernames are given as follows. They are case-sensitive.

Usernames
+----+----+----+----+----+----+----+----+----+----+
| Ava| Leo| Raj| Zoe| Max| Sam| Eli| Mia| Ian| Kim|
+----+----+----+----+----+----+----+----+----+----+

## **Input and output examples**

User inputs are in **bold font** in the following examples.

**Example 1**

Enter username: **Raj**
Login successful. Welcome Raj !

**Example 2**

Enter username: **Rio**
Login incorrect.
Enter username: **Ivy**
Login incorrect.
Enter username: **Sam**
Login successful. Welcome Sam !

# Task 2: Passwords & tries (2 marks)

This task is similar to Task 1, but:

- a password must also be entered
- after three unsuccessful tries, the program terminates.

In Task 2, you will write a program that asks the user to enter a valid username and a valid password. A successful login occurs when the user enters one of the correct usernames and one of the correct passwords. If, after three tries, the user does not provide a correct login, the program terminates.

Given the description above, the program can either terminate with a successful login or after three unsuccessful attempts.

The usernames and passwords are given as follows. They are case-sensitive.

Usernames
+----+----+----+----+----+----+----+----+----+----+
| Ava| Leo| Raj| Zoe| Max| Sam| Eli| Mia| Ian| Kim|
+----+----+----+----+----+----+----+----+----+----+

Passwords
+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| 12345  | abcde  | pass1  | qwert  | aaaaa  | zzzzz  | 11111  | apple  | hello  | admin  |
+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+

## **Input and output examples**

User inputs are in **bold font** in the following examples.

**Example 1**

Enter username: **Raj**
Enter password: **pass1**
Login successful. Welcome Raj !

**Example 2**

Enter username: **Ian**
Enter password: **1234**
Login incorrect. Tries left: 2
Enter username: **Ava**
Enter password: **pass1**
Login successful. Welcome Ava !

**Example 3**

Enter username: **Rio**
Enter password: **opqr**
Login incorrect. Tries left: 2
Enter username: **Ivy**
Enter password: **pass1**
Login incorrect. Tries left: 1
Enter username: **Ona**
Enter password: **aaaaa**
Login incorrect. Tries left: 0

# Task 3: Matching login & robot check (3 marks)
This task is similar to Task 2, but:
- the username and password must match, and
- after three unsuccessful tries, the user is asked to confirm that they are not a robot so they can try to log in again.

In Task 3, you will write a program that asks the user to enter a valid login. In this task, a valid login is a pair of username/password. Each username has a single password associated to it. If, after three tries, the user does not provide a correct login, the program asks whether they are a robot. If they are not a robot, the user is allowed three more tries. If they are a robot, the program terminates.

When asked if they are a robot, the prompt reads "Are you a robot (Y/n)?". If the user inputs "Y" or nothing (i.e. ""), then the program terminates. If the user enters "n", they are given 3 more tries to log in. If the user enters anything else, the prompt "Are you a robot (Y/n)?" is asked again and the user must answer again.

In this task, you may need to:
- use a while loop inside another while loop,
- use lists of lists, and
- use == to compare two lists.

Given the description above, the program can only terminate upon a succesful login or a failed robot check.

The pairs of usernames and passwords are given as follows. They are case-sensitive.

|----------|----------|
| Username | Password |
|----------|----------|
| Ava      | 12345    |
| Leo      | abcde    |
| Raj      | pass1    |
| Zoe      | qwert    |
| Max      | aaaaa    |
| Sam      | zzzzz    |
| Eli      | 11111    |
| Mia      | apple    |
| Ian      | hello    |
| Kim      | admin    | 
|----------|----------|

Because we are asking for a matching pair, inputting username "Ava" with password "abcde", for example, results in a failed login attempt, even though both strings are in this table. Only password "12345" leads to a succesful login for username "Ava".

Input and output examples
User inputs are in bold font in the following examples.

Example 1

Enter username: Lux
Enter password: 12345
Login incorrect. Tries left: 2
Enter username: Kim
Enter password: pass
Login incorrect. Tries left: 1
Enter username: Ravi
Enter password: pass
Login incorrect. Tries left: 0
Are you a robot (Y/n)? lol
Are you a robot (Y/n)? Y


Example 2

Enter username: Ava
Enter password: zzzzz
Login incorrect. Tries left: 2
Enter username: Leo
Enter password: aaaa
Login incorrect. Tries left: 1
Enter username: Ian
Enter password: opqr
Login incorrect. Tries left: 0
Are you a robot (Y/n)? gg ez
Are you a robot (Y/n)? n
Enter username: Zoe
Enter password: zzzzz
Login incorrect. Tries left: 2
Enter username: Zoe
Enter password: qwert
Login successful. Welcome Zoe !


Example 3

Enter username: Leo
Enter password: qwer
Login incorrect. Tries left: 2
Enter username: Eli
Enter password: abcd
Login incorrect. Tries left: 1
Enter username: Lux
Enter password: aaaaa
Login incorrect. Tries left: 0
Are you a robot (Y/n)? gg ez
Are you a robot (Y/n)? quit
Are you a robot (Y/n)? n
Enter username: Ona
Enter password: wxyz
Login incorrect. Tries left: 2
Enter username: Ava
Enter password: opqr
Login incorrect. Tries left: 1
Enter username: Raj
Enter password: 4321
Login incorrect. Tries left: 0
Are you a robot (Y/n)? lol
Are you a robot (Y/n)? n
Enter username: Mia
Enter password: wxyz
Login incorrect. Tries left: 2
Enter username: Ian
Enter password: zxcv
Login incorrect. Tries left: 1
Enter username: Ravi
Enter password: pass1
Login incorrect. Tries left: 0
Are you a robot (Y/n)? lol
Are you a robot (Y/n)? 


At the last line of the example above, the user pressed enter without entering anything.

# Task 4: One config (3 marks)

In Task 4, you will write a program that asks the user to input a string and then plans Robbie the robot’s actions to type the string using a keyboard.

Read through the following scenario to get started.

The keyboard has the following layout.

abcdefghijklm
nopqrstuvwxyz

Robbie starts at the top left position (a) and can take the following actions:

u - go up
d - go down
l - go left
r - go right
p - press the key

After pressing a key, Robbie stays on that key. This means:

- it can immediately press the same key again
- to go to another key, Robbie will start from the last key it moved to.

Furthermore, Robbie will always move horizontally (left/right) before moving vertically (up/down) when moving to a key it needs to press.

Robbie's actions are restricted by the limits of the board:

- it cannot take an action that would make it leave the board
- it cannot wrap around the board.

Any key not on the keyboard cannot be typed.

We recommend you store the key configuration of the keyboard as a list of strings. See the following example.

1

2

3

4

5

6

## **Input and output examples**

User inputs are in **bold font** in the following examples.

**Example 1**

Enter a string to type: **k**
The robot must perform the following operations:
rrrrrrrrrrp

**Example 2**

Enter a string to type: **.716**
The string cannot be typed out.

**Example 3**

Enter a string to type: **helpiamsentient**
The robot must perform the following operations:
rrrrrrrplllprrrrrrrpllllllllldprrrrrrupllllllllprrrrrrrrrrrrpllllllldpluplllldprrrrrrprrupllllplllldprrrrrrp

# Task 3: Matching login & robot check (3 marks)

This task is similar to Task 2, but:

- the username and password must match, and
- after three unsuccessful tries, the user is asked to confirm that they are not a robot so they can try to log in again.

In Task 3, you will write a program that asks the user to enter a valid login. In this task, a valid login is a pair of username/password. Each username has a single password associated to it. If, after three tries, the user does not provide a correct login, the program asks whether they are a robot. If they are not a robot, the user is allowed three more tries. If they are a robot, the program terminates.

When asked if they are a robot, the prompt reads `"Are you a robot (Y/n)?"`. If the user inputs `"Y"` or nothing (i.e. `""`), then the program terminates. If the user enters `"n"`, they are given 3 more tries to log in. If the user enters anything else, the prompt `"Are you a robot (Y/n)?"` is asked again and the user must answer again.

In this task, you may need to:

- use a `while` loop inside another `while` loop,
- use lists of lists, and
- use `==` to compare two lists.

Given the description above, the program can only terminate upon a succesful login or a failed robot check.

The pairs of usernames and passwords are given as follows. They are case-sensitive.

|----------|----------|
| Username | Password |
|----------|----------|
| Ava      | 12345    |
| Leo      | abcde    |
| Raj      | pass1    |
| Zoe      | qwert    |
| Max      | aaaaa    |
| Sam      | zzzzz    |
| Eli      | 11111    |
| Mia      | apple    |
| Ian      | hello    |
| Kim      | admin    | 
|----------|----------|

Because we are asking for a matching pair, inputting username "Ava" with password "abcde", for example, results in a failed login attempt, even though both strings are in this table. Only password "12345" leads to a succesful login for username "Ava".

## **Input and output examples**

User inputs are in **bold font** in the following examples.

**Example 1**

Enter username: **Lux**
Enter password: **12345**
Login incorrect. Tries left: 2
Enter username: **Kim**
Enter password: **pass**
Login incorrect. Tries left: 1
Enter username: **Ravi**
Enter password: **pass**
Login incorrect. Tries left: 0
Are you a robot (Y/n)? **lol**
Are you a robot (Y/n)? **Y**

**Example 2**

Enter username: **Ava**
Enter password: **zzzzz**
Login incorrect. Tries left: 2
Enter username: **Leo**
Enter password: **aaaa**
Login incorrect. Tries left: 1
Enter username: **Ian**
Enter password: **opqr**
Login incorrect. Tries left: 0
Are you a robot (Y/n)? **gg ez**
Are you a robot (Y/n)? **n**
Enter username: **Zoe**
Enter password: **zzzzz**
Login incorrect. Tries left: 2
Enter username: **Zoe**
Enter password: **qwert**
Login successful. Welcome Zoe !

**Example 3**

Enter username: **Leo**
Enter password: **qwer**
Login incorrect. Tries left: 2
Enter username: **Eli**
Enter password: **abcd**
Login incorrect. Tries left: 1
Enter username: **Lux**
Enter password: **aaaaa**
Login incorrect. Tries left: 0
Are you a robot (Y/n)? **gg ez**
Are you a robot (Y/n)? **quit**
Are you a robot (Y/n)? **n**
Enter username: **Ona**
Enter password: **wxyz**
Login incorrect. Tries left: 2
Enter username: **Ava**
Enter password: **opqr**
Login incorrect. Tries left: 1
Enter username: **Raj**
Enter password: **4321**
Login incorrect. Tries left: 0
Are you a robot (Y/n)? **lol**
Are you a robot (Y/n)? **n**
Enter username: **Mia**
Enter password: **wxyz**
Login incorrect. Tries left: 2
Enter username: **Ian**
Enter password: **zxcv**
Login incorrect. Tries left: 1
Enter username: **Ravi**
Enter password: **pass1**
Login incorrect. Tries left: 0
Are you a robot (Y/n)? **lol**
Are you a robot (Y/n)?

# Task 5: Many configs (4 marks)

In Task 5, you will write a program that asks the user to input a string, and then Robbie the robot will choose a keyboard and plan its own actions to type the string using the selected keyboard.

Read through the following scenario to get started.

For a given input string:

- If there is a single keyboard on which in can be typed, then Robbie picks that one.
- If it can be typed on multiple keyboards, Robbie picks a single keyboard as follows:
    - The one that requires the fewest moves, or, if there is a tie,
    - The first best keyboard configuration (in the order we give them).
- Finally, there may not be a keyboard that can type that string.

The keyboards have the following configurations.

**Configuration 0**

abcdefghijklm
nopqrstuvwxyz

**Configuration 1**

789
456
123
0.-

**Configuration 2**

chunk
vibex
gymps
fjord
waltz

**Configuration 3**

bemix
vozhd
grypt
clunk
waqfs

Robbie starts at the top left position of the chosen keyboard.

## **Input and output examples**

User inputs are in **bold font** in the following examples.

**Example 1**

Enter a string to type: **k**
Configuration used:
---------
| chunk |
| vibex |
| gymps |
| fjord |
| waltz |
---------
The robot must perform the following operations:
rrrrp

**Example 2**

Enter a string to type: **.716**
Configuration used:
-------
| 789 |
| 456 |
| 123 |
| 0.- |
-------
The robot must perform the following operations:
rdddpluuupddprrup

**Example 3**

Enter a string to type: **y**
Configuration used:
---------
| chunk |
| vibex |
| gymps |
| fjord |
| waltz |
---------
The robot must perform the following operations:
rddp

**Example 4**

Enter a string to type: **(╯°□°)╯︵ ┻━┻**
The string cannot be typed out.

# Task 6: Many configs & wrap (6 marks)

In Task 6, you will write a program that asks the user to input a string, and then Robbie the robot will choose a keyboard and plan its own actions to type the string using the selected keyboard. This time, Robbie is also able to wrap around the keyboard

Read through the following scenario to get started.

For example:

- In the row "abcde", Robbie can move from 'a' to 'e' in 1 move to the left. This move is encoded as "lw", where "w" marks a wrap (horizontal or vertical).
- In the row "abcde", Robbie can move from 'e' to 'a' in 1 move to the right. This move is encoded as "rw".
- The same applies for columns. The character 'w' is also used to mark vertical wrapping.
- Proud of this new technique, and for style points, Robbie uses wrapping whenever it does not increase the number of moves required. This means that, for example, in the row "ab", to go from 'a' to 'b', Robbie will always prefer doing "lw" than "r" ('w' does not count as a move).

The other rules and keyboard configurations are the same as in Task 5.

For a given input string, the best keyboard may not be the same as for Task 5, now that wrapping is possible.

## **Input and output examples**

User inputs are in **bold font** in the following examples.

**Example 1**

Enter a string to type: **k**
Configuration used:
---------
| chunk |
| vibex |
| gymps |
| fjord |
| waltz |
---------
The robot must perform the following operations:
lwp

**Example 2**

Enter a string to type: **.716**
Configuration used:
-------
| 789 |
| 456 |
| 123 |
| 0.- |
-------
The robot must perform the following operations:
ruwpldwpuwuplwup

**Example 3**

Enter a string to type: **y**
Configuration used:
-----------------
| abcdefghijklm |
| nopqrstuvwxyz |
-----------------
The robot must perform the following operations:
lwluwp

**Example 4**

Enter a string to type: **(╯°□°)╯︵ ┻━┻**
The string cannot be typed out.