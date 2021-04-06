
def cannot_capture(board):
    deltas = [(1,-2), (1,2), (-1,-2), (-1,2), (2,-1), (2,1), (-2,-1), (-2,1)]
    for row, row_val in enumerate(board):
        for col, col_val in enumerate(row_val):
            if col_val:
                for delta in deltas:
                    if row-delta[0] >= 0 and row-delta[0] < 8 and col-delta[1] >=0 and col-delta[1] < 8:
                        if board[row-delta[0]][col-delta[1]] == 1:
                            return False
    return True

