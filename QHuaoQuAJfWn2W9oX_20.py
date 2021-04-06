
def check_board(col, row):
    icol = ord(col) - ord('a')
    irow = 8 - row
    bd = [[0]*8 for i in range(8)]
    for r in range(8):
        for c in range(8):
            if r == irow and c == icol:
                pass
            elif abs(irow-r) == abs(icol-c):
                bd[r][c] = 1
            elif irow == r:
                bd[r][c] = 1
            elif icol == c:
                bd[r][c] = 1
    return bd

