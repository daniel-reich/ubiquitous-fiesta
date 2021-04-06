
def check_board(col, row):
    col, row = ord(col) - 97, 8 - row
    return [[0 if (c, r) == (col, row)
             else 1 if c == col or r == row or abs(c - col) == abs(r - row) else 0
             for c in range(8)]
            for r in range(8)]

