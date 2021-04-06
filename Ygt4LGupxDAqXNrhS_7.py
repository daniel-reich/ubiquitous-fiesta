
def spotlight_map(grid):
    if not grid:
        return grid
    else:
        rows = len(grid)
        spotlight_grid = []
        total_sum = 0
    
        for _ in range(0, rows):
            spotlight_grid.append([])
    
        for i in grid:
            i.insert(0,0)
            i.append(0)
        grid[:0] = ([[0] * len(grid[0])])
        grid.append([0] * len(grid[0]))
    
        for i, row_item in enumerate(grid):
            if row_item != grid[0]:
                for n, col_item in enumerate(grid[i]):
                    if n != 0 and n != len(grid[i])-1:
                        for x in range(-1,2):
                            total_sum += grid[i+x][n] + grid[i+x][n-1] + grid[i+x][n+1]
    
                        spotlight_grid[i-1].append(total_sum)
                        total_sum = 0
    
        return spotlight_grid

