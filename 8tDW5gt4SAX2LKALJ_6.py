
def min_bombs_needed(grid):
    def blowup_plus(grid, x, y):
        grid[x][y] = '0'
        for k in range(-1, 2):
            if k == 0:
                continue
            elif (x+k)<0 or (x+k)>=(len(grid)):
                continue
            else:
                if grid[x+k][y] == '0':
                    continue
                elif grid[x+k][y] == '+':
                    blowup_plus(grid, x+k, y)
                           
        for p in range(-1, 2):
            if p == 0:
                continue
            elif (y+p)<0 or (y+p)>=(len(grid[x])):
                continue
            else:
                if grid[x][y+p] == '0':
                    continue
                elif grid[x][y+p] == '+':
                    blowup_plus(grid, x, y+p)
        return blowup_plus
        
    def blowup_x(grid, x, y):
        grid[x][y] = '0'
        for k in range(-1, 2):
            for p in range(-1, 2):
                if k == 0 or p == 0:
                    continue
                elif (x+k)<0 or (x+k)>=(len(grid)):
                    continue
                elif (y+p)<0 or (y+p)>=(len(grid[x])):
                    continue
                else:
                    if grid[x+k][y+p] == '0':
                        continue
                    elif grid[x+k][y+p] == 'x':
                        blowup_x(grid, x+k, y+p)
        return blowup_x
                           
        
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == '+':
                count += 1
                blowup_plus(grid, x, y)
            if grid[x][y] == 'x':
                count += 1
                blowup_x(grid, x, y)
    return count

