
def tic_tac_toe(board):
    empty = []
    for i in board:
        if len(set(i)) == 1:
            return i[0]
    for x in range(len(board)-1):
        for y in range(len(board)):
            if  board[0][0] == board[1][1] == board[2][2]:
                return board[0][0]
            elif  board[x][y] != board[x+1][y]:
                return "Draw"
            
            elif board[x][y] == board[x+1][y] == board[x+2][y]:
                return board[x][y]

