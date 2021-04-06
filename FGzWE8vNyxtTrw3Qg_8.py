
def num_regions(grid):
    regions = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                regions += 1
                grid[row][col] = 0
                check(grid,row,col)
    return regions
​
def check(grid,row,col):
    if col + 1 < len(grid[0]):
        if grid[row][col + 1] == 1:
            grid[row][col + 1] = 0
            check(grid,row,col + 1)
    if row + 1 < len(grid):
        if grid[row + 1][col] == 1:
            grid[row + 1][col] = 0
            check(grid,row + 1,col)
    if col - 1 >= 0:
        if grid[row][col - 1] == 1:
            grid[row][col - 1] = 0
            check(grid,row,col - 1)
    if row - 1 >= 0:
        if grid[row - 1][col] == 1:
            grid[row - 1][col] = 0
            check(grid,row - 1,col)
    return None

