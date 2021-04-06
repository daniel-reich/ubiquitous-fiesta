
def spotlight_map(grid):
    new_grid = [[0]*len(grid[0]) for _ in range(len(grid))]
​
    pts = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            s = grid[i][j]
            for x, y in pts:
                if 0 <= i+x < len(grid) and 0 <= j+y < len(grid[0]):
                    s += grid[i+x][j+y]
            new_grid[i][j] = s
    return new_grid

