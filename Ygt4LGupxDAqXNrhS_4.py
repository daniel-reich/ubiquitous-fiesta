
def spotlight_map(grid):
    if not grid: return []
    row = len(grid); col = len(grid[0]); add = 0; res = [[0 for i in range(col)] for j in range(row)]
    for i in range(row):
        for j in range(col):
            add += grid[i][j]
            if i-1 >= 0:
                add += grid[i-1][j]
                if j-1 >= 0: add += grid[i-1][j-1]
                if j+1 < col: add += grid[i-1][j+1]
            if i+1 < row:
                add += grid[i+1][j]
                if j-1 >= 0: add += grid[i+1][j-1]
                if j+1 < col: add += grid[i+1][j+1]
            if j-1 >= 0: add += grid[i][j-1]
            if j+1 < col: add += grid[i][j+1]
            res[i][j] = add; add = 0
    return res

