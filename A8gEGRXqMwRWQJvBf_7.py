
def tic_tac_toe(board):
    for i in board:
        if board[0][1]==board[1][1]==board[2][1]=="O":
            return "O"
        elif board[0][0]==board[1][0]==board[2][0]=="X":
            return "X"
        if board[0][0] == board[1][1] == board[2][2]=="X":
            return "X"
        elif board[0][0] == board[1][1] == board[2][2]=="O":
            return "O"
        if i.count("X") ==3:
            return "X"
        elif i.count("O") ==3:
            return "O"
        else:
            return  "Draw"

