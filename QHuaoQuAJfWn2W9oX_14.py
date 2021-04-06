
def check_board(col, row):
    qr, qc = (8 - row), (ord(col) - ord('a'))
    board = [[0]*8 for _ in range(8)]
    for r in range(8):
        for c in range(8):
            if (r, c) != (qr, qc) and (qr == r or qc == c or abs(r - qr) == abs(c - qc)):
                board[r][c] = 1
    return board

