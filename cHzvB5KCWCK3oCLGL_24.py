
def game_of_life(board):
    next_board = [row[:] for row in board]
    for x in range(len(board)):
        for y in range(len(board[0])):
            next_board[x][y] = next_state(board,x,y)
    return displayer(next_board)
​
def displayer(board):
    s = ""
    for a in board:
        for b in a:
            if b == 1: s += "I"
            else: s += "_"
        s+="\n"
    return s[:-1]
​
def next_state(board,x,y):
    counter = 0
    if x>0:
        if board[x-1][y] == 1: counter +=1
        if y > 0 and board[x - 1][y - 1] == 1: counter += 1
        if y < len(board[0])-1 and board[x - 1][y + 1] == 1: counter += 1
    if y>0 and board[x][y-1] == 1: counter +=1
    if y < len(board[0])-1 and board[x][y + 1] == 1: counter += 1
    if x<len(board)-1: 
        if board[x + 1][y] == 1: counter += 1
        if y > 0 and board[x + 1][y - 1] == 1: counter += 1
        if y < len(board[0])-1 and board[x + 1][y + 1] == 1: counter += 1
    if board[x][y] == 1:
        if counter < 2: return 0
        elif counter >= 4: return 0
        else: return 1
    if board[x][y] == 0:
        if counter == 3: return 1
        return 0

