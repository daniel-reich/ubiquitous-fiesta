
import numpy as np
def win(mod_board):
    return any([all(map(lambda x: x == 'X',mod_board[i])) for i in range(3)]) or\
    any([all(map(lambda x: x == 'X',np.transpose(mod_board)[i])) for i in range(3)]) or\
    all([mod_board[i][i] == 'X' for i in range(3)]) or\
    all([mod_board[i][2-i] == 'X' for i in range(3)])
​
def x_and_o(board):
    mod_board = np.reshape([board[i][j] for i in range(3) for j in [0,2,4]],(3,3))
    pos = [[i,j] for i in range(3) for j in range(3)]
    pos_ = [[i,j] for i in range(1,4) for j in range(1,4)]
    for i in range(9):
        p = pos[i]
        mod_ = mod_board.copy()
        if mod_board[p[0]][p[1]] == ' ':
            mod_[p[0]][p[1]] = 'X'
            if win(mod_):
                return pos_[i]
    return False

