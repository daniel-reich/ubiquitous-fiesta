
def spotlight_map(grid):
    d = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            d[(i,j)] = grid[i][j]
    a = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]
    
    for loc in d.keys():
        ctr = 0
        for k in range(len(a)):
            if (loc[0]+a[k][0],loc[1]+a[k][1]) in d:
                ctr += d[(loc[0]+a[k][0],loc[1]+a[k][1])]
        grid[loc[0]][loc[1]] = ctr    
    
    return grid

