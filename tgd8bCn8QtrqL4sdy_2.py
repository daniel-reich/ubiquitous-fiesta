
def minesweeper(grid):
    '''
    Returns updated grid to show how many mines surround any '?' cells, as
    per the instructions.
    '''
    def mines(grid, i, j):
        '''
        Returns a count of mines surrounding grid[i][j] where a mine is
        identified as a '#'
        '''
        count = 0
        locs = ((i-1,j-1), (i-1,j), (i-1,j+1),(i,j-1),
                (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)) # possible neighbours
​
        for r, c in locs:
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                if grid[r][c] == '#':
                    count += 1
​
        return str(count)
​
    return [[mines(grid,i,j) if grid[i][j] == '?' else grid[i][j] \
             for j in range(len(grid[0]))] for i in range(len(grid))]

