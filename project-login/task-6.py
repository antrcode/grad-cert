""" This program asks the user to input a string, and then Robbie the robot will choose a keyboard and plan its own actions to type the string using the selected keyboard. Robbie is able to wrap around the keyboard. """

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
    Compute and print the sequence of actions Robbie must take to type the string on a given keyboard.
    Robbie is able to wrap around the keyboard; wraps are preferred over normal moves in the case of a tie.
    Actions: 'r' = move right, 'l' = move left, 'u' = move up, 'd' = move down, 'p' = press key, 'w' = wrap occurred.
    """
    current_row, current_col = 0, 0  # start at top left position of keyboard
    actions = "" # actions stored as a string
    num_rows = len(keyboard) # number of rows in a keyboard (used for vertical movement)

    for char in enter_string:
        target_row, target_col = find_key_position(char, keyboard)
        row_length = len(keyboard[current_row])

        # move horizontally first
        # calculate how far the target is to the right or left (including wrap distance)
        if target_col >= current_col:
            right_dist = target_col - current_col
            left_dist = current_col + (row_length - target_col)  # wrap left
        else:
            left_dist = current_col - target_col
            right_dist = target_col + (row_length - current_col)  # wrap right

        # shortest path chosen; if tie, prefer wrapping
        if right_dist == left_dist: 
            if current_col + right_dist >= row_length:  # wrap right
                for _ in range(right_dist):
                    current_col += 1
                    if current_col >= row_length: # if wrap past right end
                        current_col = 0
                        actions += "r" + "w" # right action + wrap
                    else:
                        actions += "r" 
            else:  # wrapping left
                for _ in range(left_dist):
                    current_col -= 1
                    if current_col < 0: # if wrap past left end
                        current_col = row_length - 1
                        actions += "l" + "w" # left action + wrap
                    else:
                        actions += "l"
        elif right_dist < left_dist: 
            # move right (shorter distance)
            for _ in range(right_dist):
                current_col += 1
                if current_col >= row_length:
                    current_col = 0
                    actions += "r" + "w"
                else: 
                    actions += "r"
        else:
            # move left (shorter distance)
            for _ in range(left_dist):
                current_col -= 1
                if current_col < 0:
                    current_col = row_length - 1
                    actions += "l" + "w"
                else:
                    actions += "l"

        # move vertically
        # calculate distance to move up or down (including wrap)
        if target_row >= current_row:
            down_dist = target_row - current_row
            up_dist = current_row + (num_rows - target_row)  # wrapping up
        else:
            up_dist = current_row - target_row
            down_dist = target_row + (num_rows - current_row)  # wrapping down

        # shortest path chosen; if tie, prefer wrapping
        if down_dist == up_dist:
            if current_row + down_dist >= num_rows:  # wrap down
                for _ in range(down_dist):
                    current_row += 1
                    if current_row >= num_rows:
                        current_row = 0
                        actions += "d" + "w"
                    else:
                        actions += "d"
            else:  # wrap up
                for _ in range(up_dist):
                    current_row -= 1
                    if current_row < 0:
                        current_row = num_rows - 1
                        actions += "u" + "w"
                    else:
                        actions += "u"
        elif down_dist < up_dist:
            # move down (shorter distance)
            for _ in range(down_dist):
                current_row += 1
                if current_row >= num_rows:
                    current_row = 0
                    actions += "d" + "w"
                else:
                    actions += "d"
        else:
            # move up (shorter distance)
            for _ in range(up_dist):
                current_row -= 1
                if current_row < 0:
                    current_row = num_rows - 1
                    actions += "u" + "w"
                else:
                    actions += "u"

        # p to press key when in correct position
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
    Returns a list of valid keyboard layouts that can type the string.
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