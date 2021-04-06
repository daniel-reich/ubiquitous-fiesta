
def rec_tint(i, j, grid, n_rows, n_cols, n_regions, tint = None):
    if grid[i][j] != 1:
        return(n_regions)
    if tint == None:
        n_regions += 1 
    tint = n_regions
    grid[i][j] = tint
    if i > 0: n_regions = rec_tint(i - 1, j, grid, n_rows, n_cols, n_regions, tint)
    if i < n_rows - 1: n_regions = rec_tint(i + 1, j, grid, n_rows, n_cols, n_regions, tint)
    if j > 0: n_regions = rec_tint(i, j - 1, grid, n_rows, n_cols, n_regions, tint)
    if j < n_cols - 1: n_regions = rec_tint(i, j + 1, grid, n_rows, n_cols, n_regions, tint)
    return(n_regions)
    
def num_regions(grid):
    n_rows = len(grid)
    n_cols = len(grid[0])
    n_regions = 1
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == 1:
                n_regions = rec_tint(i, j, grid,
                                     n_rows, n_cols, n_regions)
    return(n_regions - 1)

