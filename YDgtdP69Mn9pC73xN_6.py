
def num_grid(grid):
​
    mines = []
​
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            if grid[x][y] == "#":
                mines.append((x, y))
            else:
                grid[x][y] = 0
​
    for x, y in mines:
        for x_addition in range(-1, 2):
            for y_addition in range(-1, 2):
                if x_addition !=0 or y_addition !=0:
                    if x + x_addition >= 0 and y + y_addition >= 0:
                        try:
                            grid[x + x_addition][y + y_addition] += 1
                        except:
                            pass
​
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            grid[x][y] = str(grid[x][y])
​
    return grid

