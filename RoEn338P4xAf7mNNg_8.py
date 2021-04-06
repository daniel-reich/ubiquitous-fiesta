
def shortest_path(grid):
    '''
    Returns the number of moves in the shortest path through the grid as per
    the instructions
    '''
    man_dist = lambda x,y: abs(x[1][0] - y[1][0]) + abs(x[1][1] - y[1][1])
    
    locs = sorted([(grid[i][j],(i,j)) for i in range(len(grid))
                   for j in range(len(grid[0]))
                   if grid[i][j] > '0'])
​
    
​
    return sum(man_dist(a,b) for a,b in zip(locs,locs[1:]))

