
def tic_tac_toe(board):
    z = [y for c in board for y in c]
    d = len(z)
    for i in range(len(board)):
        if z[i] == z[i+1] and z[i] == z[i+2]:
            return z[i]
        elif z[i] == z[i+3] and z[i] == z[i+6]:
            return z[i]
        
        elif i == 0:
            if z[i] == z[i+4] and z[i] == z[i+8]:
                return z[i]
        else:
            return "Draw"

