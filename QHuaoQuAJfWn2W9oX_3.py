
import string
def check_board(row, col):
    # Create matrix
    cb = []
    for y in range(0, 8):
        cb.append([0 for x in range(0, 8)])
    # Translate the input
    row = string.ascii_letters.index(row)
    col = len(cb) - col
    # Horizontal
    for i in range(0, len(cb)):
        cb[col][i] = 1
    # Vertical
    for i in range(0, len(cb)):
        cb[i][row] = 1
    # Diagonal 1
    x, y = row - row, col - row
    for i in range(len(cb)):
        if y + i < 0 or x + i < 0: continue
        try:
            cb[y + i][x + i] = 1
        except IndexError:
            continue
    # Diagonal 2
    x, y = row + col, col - col
    for i in range(len(cb)):
        if y + i <0 or x - i < 0: continue
        try:
            cb[y + i][x - i] = 1
        except IndexError:
            continue
    cb[col][row] = 0  # Marks the queen
    return cb

