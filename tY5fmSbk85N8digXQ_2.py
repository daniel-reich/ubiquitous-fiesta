
def ones_infection(mtx):
    memx = []
    memy = []
    n_r = len(mtx)
    n_c = len(mtx[0])
    
    for row in range(n_r):
        for col in range(n_c):
            if mtx[row][col] == 1:
                memy.append(row)
                memx.append(col)
​
    for y in range(n_r):
        if y in memy:
            for i in range(n_c):
                mtx[y][i] = 1
    for x in range(n_c):
        if x in memx:
            for i in range(n_r):
                mtx[i][x] = 1
    return mtx

