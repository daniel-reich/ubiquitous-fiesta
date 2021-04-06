
import numpy as np
​
def tic_tac_toe(board):
    lines = np.vstack((board, np.rot90(board), np.diag(board), np.diag(np.rot90(board)))).tolist()
    for i in lines:
        if i in (['X', 'X', 'X'], ['O', 'O', 'O']):
            return i[0]
    return 'Draw'

