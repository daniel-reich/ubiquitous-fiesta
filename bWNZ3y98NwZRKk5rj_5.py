
solution = {(0, 1): 2, (0, 2): 1, (1, 2): 0,  # first row
            (3, 4): 5, (3, 5): 4, (4, 5): 3,  # second row
            (6, 7): 8, (6, 8): 7, (7, 8): 6,  # third row
            (0, 3): 6, (0, 6): 3, (3, 6): 0,  # first column
            (1, 4): 7, (1, 7): 4, (4, 7): 1,  # second column
            (2, 5): 8, (2, 8): 5, (5, 8): 2,  # third column
            (0, 8): 4, (4, 8): 0, (0, 4): 8,  # diagonal top left to bottom right
            (2, 4): 6, (4, 6): 2, (2, 6): 4,  # diagonal top right to bottom left
            }
​
def block_player(a, b):
    return solution[(a, b)]

