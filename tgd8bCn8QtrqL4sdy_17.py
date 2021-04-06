
def minesweeper(grid):
    positions = []
    
    for i in range(3):
        for j in range(3):
            if grid[i][j] == "?":
                positions.append([i, j])
​
    for pos in positions:
        mine_count = 0
​
        for i in range(pos[0] - 1, pos[0] + 2):
            for j in range(pos[1] - 1, pos[1] + 2):
                if (0 <= i <= 2) and (0 <= j <= 2):
                    if grid[i][j] == "#":
                        mine_count += 1
​
        grid[pos[0]][pos[1]] = str(mine_count)
​
    return grid

