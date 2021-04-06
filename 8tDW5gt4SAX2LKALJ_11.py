
def min_bombs_needed(grid):
​
    def hov(grid, row, col, x, y):
        if grid[x][y] == '0':
            return
        if grid[x][y] == 'x':
            return dia(grid, row, col, x, y)
        grid[x][y] = '0'
​
        if x != 0:
            hov(grid, row, col, x-1, y)
        if x < row-1:
            hov(grid, row, col, x+1, y)
        if y != 0:
            hov(grid, row, col, x, y-1)
        if y != col-1:
            hov(grid, row, col, x, y+1)
​
    def dia(grid, row, col, x, y):
        if grid[x][y] == '0':
            return
        if grid[x][y] == '+':
            return hov(grid, row, col, x, y)
        grid[x][y] = '0'
​
        if x != 0 and y != 0:
            dia(grid, row, col, x-1, y-1)
        if x < row-1 and y != col-1:
            dia(grid, row, col, x+1, y+1)
        if x != 0 and y != col-1:
            dia(grid, row, col, x-1, y+1)
        if x < row-1 and y != 0:
            dia(grid, row, col, x+1, y-1)
​
    row = len(grid)
    col = len(grid[0])
    cnt = 0
​
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '+':
                hov(grid, row, col, i, j)
                cnt += 1
            if grid[i][j] == 'x':
                dia(grid, row, col, i, j)
                cnt += 1
​
    return cnt

