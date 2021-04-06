
def minesweeper(grid):
    rows = len(grid)
    cols = len(grid[0])
​
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '?':
                mines = 0
                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        if 0 <= r+i < rows and 0 <= c+j < cols and grid[r+i][c+j] == '#':
                            mines += 1
                grid[r][c] = str(mines)
    return grid

