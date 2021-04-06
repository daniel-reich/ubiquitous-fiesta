
from random import randrange as rand
import copy
​
def get_one_pos(M, H, W):
    for r in range(H):
        for c in range(W):
            if M[r][c] == 1:
                return r, c
​
def move(mat):
    return lambda x: move_it(copy.deepcopy(mat), x)
​
def move_it(Matrix, op):
    H, W = len(Matrix), len(Matrix[0])
    r1, c1 = get_one_pos(Matrix, H, W)
    if op == 'stop':
        return Matrix
    elif op == 'up':
        Matrix[r1][c1] = 0
        Matrix[(r1 - 1) % H][c1] = 1
    elif op == 'down':
        Matrix[r1][c1] = 0
        Matrix[(r1 + 1) % H][c1] = 1
    elif op == 'left':
        Matrix[r1][c1] = 0
        Matrix[r1][(c1 - 1) % W] = 1
    elif op == 'right':
        Matrix[r1][c1] = 0
        Matrix[r1][(c1 + 1) % W] = 1
    return lambda x: move_it(Matrix[:], x)

