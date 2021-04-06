
def x_and_o(board):
    combinations = [{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]
    board = sum([x.split('|') for x in board], [])
    moves = [i + 1 for i, x in enumerate(board) if 'X' == x]
    nxt = [sum(x.difference(moves)) for x in combinations if  len(x.difference(moves)) == 1]
    
    for x in nxt:
        if ' ' == board[x-1]:
            return [(x-1)//3+1,(x-1) % 3 + 1]
​
    return False

