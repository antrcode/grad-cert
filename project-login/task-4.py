"""
This program asks the user to input a string and then plans Robbie the robot's actions to type the string using a keyboard.
"""

keyboard = \
["abcdefghijklm",
 "nopqrstuvwxyz"]

allowed_char = "".join(keyboard)

def check_string(enter_string: str, allowed_char: str) -> bool:
    """
    Check that keys that are not on the keyboard cannot be typed.
    Returns True if all characters are allowed, otherwise False.
    """
    for char in enter_string:
        if char not in allowed_char:
            print("The string cannot be typed out.")
            return False
    return True

def find_key_position(key: str) -> tuple[int, int]:
    """
    Find the row (r) and column (c) of a key on the keyboard.
    Returns [row, column].
    """
    for r in range(len(keyboard)):
        for c in range(len(keyboard[r])):
            if keyboard[r][c] == key:
                return r, c
    return None

def robbie_movement(enter_string: str) -> str:
    """
    Compute and print the sequence of actions Robbie must take to type the string.
    Robbie will always move horizontally (left/right) before moving vertically (up/down) when moving to a key it needs to press.
    Actions: 'r' = move right, 'l' = move left, 'u' = move up, 'd' = move down, 'p' = press key.
    """
    # start at top left position (a)
    current_row, current_col = 0, 0
    actions = "" # actions stored as a string

    for char in enter_string:
        target_row, target_col = find_key_position(char)

        # move horizontal first
        while current_col < target_col:
            actions += "r"
            current_col += 1
        while current_col > target_col:
            actions += "l"
            current_col -= 1

        # then move vertically next
        while current_row < target_row:
            actions += "d"
            current_row += 1
        while current_row > target_row:
            actions += "u"
            current_row -= 1

        # p to press the key
        actions += "p"

    return actions

# ask user for string input
enter_string = input("Enter a string to type: ")

# validate the input and generate robbie's actions
if check_string(enter_string, allowed_char):
    actions = robbie_movement(enter_string)
    print("The robot must perform the following operations:")
    print(actions)