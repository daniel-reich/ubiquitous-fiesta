
def min_bombs_needed(grid):
    bomb = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] in ['+','x']:
                check(grid,row,col,grid[row][col])
                bomb += 1 
    return bomb
​
def check(grid,row,col,direc):
    grid[row][col] = '0'
    around = [1,-1]
    if direc == 'x':
        for i in around:
            for j in around:
                if 0 <= row + i < len(grid) and 0 <= col + j < len(grid[0]):
                    if grid[row + i][col + j] in ['+','x']:
                        check(grid,row + i,col + j,grid[row + i][col + j])
    else:
        for i in around:
            if 0 <= row + i < len(grid):
                if grid[row + i][col] in ['+','x']:
                    check(grid,row +i,col,grid[row + i][col])
            if  0 <= col + i < len(grid[0]):
                if grid[row][col + i] in ['+','x']:
                    check(grid,row,col + i,grid[row][col + i])

