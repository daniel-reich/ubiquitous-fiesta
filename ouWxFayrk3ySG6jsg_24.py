
def who_won(board):
    for x in range(len(board)):
​
        #Horizontal
        if len(set(board[x]))==1:
            return board[x][0]
        #Verticals
        if len(set([board[0][x],board[1][x],board[2][x]]))==1:
            return board[0][x]
​
        #Diagonals
    if len(set([row[i] for i,row in enumerate(board)])) ==1:
        return board[0][0]
​
    if len(set([row[-i-1] for i,row in enumerate(board)])) ==1:
        return board[2][0]

