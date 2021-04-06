
def minesweeper(grid):
    moves = [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
    for x in range(3):
        for y in range(3):
            if grid[x][y] == '?':
                neighbors = sum([1 for a,b in moves if (0 <= x+a < 3 and 0 <= y+b < 3) and grid[a+x][y+b] == '#'])
                grid[x][y] = str(neighbors)
    return grid

