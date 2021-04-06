
def x_and_o(board):
    def win_test(board):
        if any([1 if row.count("X")==3 else 0 for row in board]):return True
        if any([1 if row.count("X")==3 else 0 for row in [list(i) for i in zip(*board)][::-1]]):return True
        if all([1 if board[y][y]=="X" else 0 for y in range(3) ]):return True
        if all([1 if board [2-y][y]=="X" else 0 for y in range(3) ]):return True
        return False
    board,to_test=[row.split("|") for row in board],[]    
    for y in range(3):
        for x in range(3):
            if board[y][x]==" ":
                to_test.append((y,x))
    for pos in to_test:        
        board[pos[0]][pos[1]]="X"        
        if win_test(board): return [pos[0]+1,pos[1]+1]
        board[pos[0]][pos[1]]=" "
    return False

