
def minesweeper(grid):
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == '?':
                for j in range(-1, 2):
                    for k in range(-1, 2):
                        if x+j>2 or x+j<0:
                            continue
                        elif y+k>2 or y+k<0:
                            continue
                        elif j == 0 and k == 0:
                            continue
                        else:
                            if grid[x+j][y+k] == '#':
                                count +=1
                grid[x][y] = str(count)
                count = 0
    return grid

