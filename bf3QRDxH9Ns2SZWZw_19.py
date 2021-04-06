
def all_explode(grid):
    pad = ['0' for i in range(len(grid[0])+2)]
    grid = [pad] + [['0'] + row + ['0'] for row in grid] + [pad]
    explode(grid,1,1)
    total = sum([1 for i in grid if 'x' in i or '+' in i])
    return total == 0
​
def explode(grid,row,col):
    diag = [(row+1,col+1),(row+1,col-1),(row-1,col+1),(row-1,col-1)]
    sides = [(row+1,col),(row-1,col),(row,col-1),(row,col+1)]
    if grid[row][col] == '+':
        grid[row][col] = '0'
        for i in sides:
            if grid[i[0]][i[1]] != '0': 
                explode(grid,i[0],i[1])
    else:
        grid[row][col] = '0'
        for i in diag:
            if grid[i[0]][i[1]] != '0': 
                explode(grid,i[0],i[1])      
    return None

