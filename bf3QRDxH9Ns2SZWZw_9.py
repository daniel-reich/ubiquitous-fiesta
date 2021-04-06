
def verify(dire,grid, act, new, i, lin, col):
    for j in dire:
        nr, nc = i[0] + j[0], i[1] + j[1]
        if 0 <= nr <= lin and 0 <= nc <= col and (nr, nc) not in act:
            if grid[nr][nc] != '0': new.append((nr, nc))
    return new
​
def all_explode(grid):
    bombs, lin, col, new, act = dict(), len(grid)-1, len(grid[0])-1, [(0,0)], {(0,0):True}
    pls, tim = [(-1,0),(1,0),(0,-1),(0,1)], [(-1,-1),(-1,1),(1,-1),(1,1)]
    for  i in range(lin+1):
        for j in range(col+1):
            if grid[i][j] != '0': bombs[(i,j)] = True
    while new:
        tests = new.copy(); new=[]
        for i in tests:
            if grid[i[0]][i[1]] == '+': new = verify(pls,grid, act, new, i, lin, col)
            else: new = verify(tim,grid, act, new, i, lin, col)
        for i in new: act[i] = True
    return True if act.keys() == bombs.keys() else False

