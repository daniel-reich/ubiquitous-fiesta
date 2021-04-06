
def spotlight_map(grid):
    y = len(grid)
    try:
        x = len(grid[0])
    except IndexError:
        return []
    new_grid = []
    for o in range(y):
        new_grid.append([])
        for p in range(x):
            new_grid[o].append(0)
    for y_span in range(y):
        for x_span in range(x):
            current_tile_total = 0
            for i in range(3):
                for j in range(3):
                    replace_y = i + y_span - 1
                    replace_x = j + x_span - 1
​
                    if replace_y < 0 or replace_y >= y:
                        continue
                    elif replace_x < 0 or replace_x >= x:
                        continue
                    else:
                        current_tile_total = grid[replace_y][replace_x] + current_tile_total
            new_grid[y_span][x_span] = current_tile_total
    return(new_grid)

