
def x_and_o(board):
    '''
    Returns (r, c) if X can win by placing an X on the next move as per the
    instructions, otherwise False. r and c are row and col number (from 1 to 3)
    '''
    board = [row.split('|') for row in board]
    winner = lambda x: x.count('X') == 2 and x.count(' ') == 1
    lines = ((0,0,0,1,0,2),(1,0,1,1,1,2),(2,0,2,1,2,2),  # rows
             (0,0,1,0,2,0),(0,1,1,1,2,1),(0,2,1,2,2,2),  # cols
             (0,0,1,1,2,2),(0,2,1,1,2,0)) # diags
​
    for line in lines:
        a,b,c,d,e,f = line
        seq = board[a][b]+board[c][d]+board[e][f]
        if winner(seq):
            for j in range(0,7,2):
                if board[line[j]][line[j+1]] == ' ':
                    return [line[j]+1, line[j+1]+1]
​
    return False

