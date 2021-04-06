
def count_wins(board, player):
    win = player * 3
    cnt = 0
    for i in range(3):
        if board[i] == win:
            cnt += 1
        if board[0][i]+board[1][i]+board[2][i] == win:
            cnt += 1
    diag = [board[i][i] for i in range(3)]
    if diag == win:
        cnt += 1
    diag = [board[i][2-i] for i in range(3)]
    if diag == win:
        cnt += 1
    return cnt
​
def validate_tic_tac_toe(board):
    flat = board[0] + board[1] + board[2]
    cntO = flat.count('O')
    cntX = flat.count('X')
    if not cntX in [cntO, cntO+1]:
        return False    # number of marks not valid
    winsO = count_wins(board, 'O')
    winsX = count_wins(board, 'X')
    if winsO * winsX > 0:
        return False    # there can be only one winning player
    return True

