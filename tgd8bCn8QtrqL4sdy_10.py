
def minesweeper(grid):
    is_mine = lambda x,y: 0<=x<len(grid[0]) and 0<=y<len(grid) and grid[x][y] == '#'
    rtn = [row[:] for row in grid]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '?':
                rtn[r][c] = str(sum(is_mine(r+i, c+j) for i,j in [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]))
    return rtn

