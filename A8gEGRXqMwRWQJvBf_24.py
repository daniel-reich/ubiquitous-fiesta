
def tic_tac_toe(board):
    chars=["O","X"]
    for char in chars:
        for row in board:    
            if all([1 if char ==elem else 0 for elem in row ]):return char
        for row in zip(*board[::-1]):
            if all([1 if char ==elem else 0 for elem in row ]):return char
        if all([1 if char==board[index][index] else 0 for index in range(3)]):return char
        if all([1 if char==board[2-index][index] else 0 for index in range(3)]):return char
    return "Draw"

