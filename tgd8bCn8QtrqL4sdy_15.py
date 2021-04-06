
def minesweeper(grid):
    quest = [[i,j] for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '?']
    mines = [[i,j] for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '#']
    count = 0
    for q in quest:    
        for m in mines:    
            if ((m[0] - q[0])**2 + abs(m[1] - q[1])**2)**0.5 <= 2**0.5:
                count += 1
        grid[q[0]][q[1]] = str(count)
        count = 0
    return grid

