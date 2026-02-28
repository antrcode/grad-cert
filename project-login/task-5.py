""" 
This program asks the user to input a string, and then Robbie the robot will choose a keyboard and plan its own actions to type the string using the selected keyboard.
"""

keyboards = [
    ["abcdefghijklm", "nopqrstuvwxyz"], # config 0
    ["789", "456", "123", "0.-"], # config 1
    ["chunk", "vibex", "gymps", "fjord", "waltz"], # config 2
    ["bemix", "vozhd", "grypt", "clunk", "waqfs"] # config 3
]

def check_string(enter_string: str, allowed_char: str) -> bool:
    """
    Check that keys that are not on the keyboard cannot be typed.
    Returns True if all characters are allowed, otherwise False.
    """
    for char in enter_string:
        if char not in allowed_char:
            return False
    return True

def find_key_position(key: str, keyboard: list[str]) -> tuple[int, int]:
    """
    Find the row (r) and column (c) of a key on the keyboard.
    Returns [row, column].
    """
    for r in range(len(keyboard)):
        for c in range(len(keyboard[r])):
            if keyboard[r][c] == key:
                return r, c
    return None

def robbie_movement(enter_string: str, keyboard: list[str]) -> str:
    """
    Compute and returns the sequence of actions Robbie must take to type the string.
    Actions: 'r' = move right, 'l' = move left, 'u' = move up, 'd' = move down, 'p' = press key.
    Robbie always starts at the top left position of the chosen keyboard.
    """
    current_row, current_col = 0, 0 # start at top left position of keyboard
    actions = "" # actions stored as a string

    for char in enter_string:
        target_row, target_col = find_key_position(char, keyboard)

        # move horizontally first
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

        # p to press the key when in correct position
        actions += "p"

    return actions

def calculate_moves(actions: str) -> int:
    """
    Count total number of movement actions (actions are 'r', 'l', 'u', 'd'; 'p' is not counted) Robbie performs in a given action sequence.
    Returns the total number of movements.
    """
    move_count = 0
    for a in actions:
        if a in ["r", "l", "u", "d"]:
            move_count += 1
    return move_count

def get_valid_keyboards(enter_string: str, keyboards: list[list[str]]) -> list[list[str]]:
    """
    Determine which keyboard can be used to type the input string.
    Returns a list of valid keyboards that can type the string.
    """
    valid_keyboards = []
    for keyboard in keyboards:
        allowed_char = "".join(keyboard)
        if check_string(enter_string, allowed_char):
            valid_keyboards.append(keyboard)
    return valid_keyboards

def choose_best_keyboard(enter_string: str, valid_keyboards: list[list[str]]) -> tuple[list[str], str]:
    """
    If the input string can be typed on multiple keyboards, from the valid keyboards, Robbie picks the one that requires the fewest moves, or, if there is a tie, the first best keyboard configuration.
    Returns the best keyboard and corresponding action sequence.
    """
    best_keyboard = valid_keyboards[0]
    best_actions = robbie_movement(enter_string, best_keyboard)
    fewest_moves = calculate_moves(best_actions)

    # compares which keyboard requires the fewest moves
    for keyboard in valid_keyboards[1:]:
        actions = robbie_movement(enter_string, keyboard)
        moves = calculate_moves(actions)
        if moves < fewest_moves:
            best_keyboard = keyboard
            best_actions = actions
            fewest_moves = moves

    return best_keyboard, best_actions

def print_keyboard(keyboard: list[str]):
    """
    Print the chosen keyboard within a box with borders.
    The width of the box is adjusted to the longest row.
    """
    max_len = max(len(row) for row in keyboard)
    border = "-" * (max_len + 4)
    print("Configuration used:")
    print(border)
    for row in keyboard:
        print("| " + row + " |")
    print(border)

# ask user for string input
enter_string = input("Enter a string to type: ")

# find which keyboard(s) can type the given string
valid_keyboards = get_valid_keyboards(enter_string, keyboards)

# if more than one valid keyboard, the one with the fewest moves, or the first best keyboard configuation is chosen
if valid_keyboards:
    best_keyboard, actions = choose_best_keyboard(enter_string, valid_keyboards)
    print_keyboard(best_keyboard)
    print("The robot must perform the following operations:")
    print(actions)
else:
    # if no keyboards can type the string input, error is given
    print("The string cannot be typed out.")