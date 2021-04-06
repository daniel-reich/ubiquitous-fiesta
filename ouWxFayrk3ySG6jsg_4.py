
def who_won(board):
    for j in range(len(board[0])):
        if((board[0][j])==(board[1][j])==(board[2][j])):
            return board[0][j]
        elif(len(set(board[j]))==1):
            return board[j][0]
    if(board[0][0]==board[1][1]==board[2][2]):
        return board[0][0]    
    elif(board[0][2]==board[1][1]==board[2][0]):
        return board[0][2]

