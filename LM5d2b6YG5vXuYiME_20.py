
def can_enter_cave(screen):
    # rotate the map so that it is traversed top to bottom (makes it easier to think).
    screen = [list(elem) for elem  in list(zip(*screen))]
    # Assume nowhere is reachable:
    is_reachable = [[0 for elem in row] for row in screen]
​
    for iteration in range(len(screen) - 2):
        for row in range(len(screen)):
            for col in range(len(screen[row])):
                if row == 0:  # First row test
                    if screen[row][col] == 0:
                        is_reachable[row][col] = 1
                else:  # All other rows
                    if screen[row][col] == 0 and is_reachable[row - 1][col] == 1:  # Look back
                        is_reachable[row][col] = 1
                    elif row < len(screen) - 1 and screen[row][col] == 0 and is_reachable[row + 1][col] == 1:  # Look forwards
                        is_reachable[row][col] = 1
                    for col2 in range(len(screen[row])):
                        try:
                            if screen[row][col2] == 0 and is_reachable[row][col2 - 1] == 1:
                                is_reachable[row][col2] = 1
                            elif screen[row][col2] == 0 and is_reachable[row][col2 + 1] == 1:
                                is_reachable[row][col2] = 1
                        except IndexError:
                            pass
​
    return any(is_reachable[-1])

