
def who_won(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O" or board[i][j] == "X":
                t = True
    if t:
        tout = [board[0][2] + board[1][1] + board[2][0], board[0][0] + board[1][1] + board[2][2]]
        for i in range(3):
            b = ""
            c = ""
            for j in range(3):
                b += board[j][i]
                c += board[i][j]
            tout.append(b)
            tout.append(c)
        for t in tout:
            if t[0] == t[1] == t[2]:
                return t[0]

