
def langtons_ant(grid, col, row, n, direction=0):
    # directions: 0 - north, 1 - east, 2 - south, 3 - west
    h, w = len(grid), len(grid[0])
    assert h == w, "We expect a square grid?? " + str(h) + " " + str(w)
    for _ in range(n):
        direction = (direction + 1) % 4 if grid[row][col] == 1 else (direction - 1)  % 4
        grid[row][col] = 1 - grid[row][col]
        if direction == 0:
            # go north:
            if row == 0:
                # we have to expand the grid to the north, ant is in (new) row 0:
                grid = [[0] * w] + grid
                h += 1
            else:
                row -= 1
        elif direction == 2:
            # go south:
            if row == h - 1:
                # we have to expand the grid to the south, ant is in (new) row h-1:
                grid = grid + [[0] * w]
                h += 1
                row += 1
            else:
                row += 1
        elif direction == 1:
            # go east:
            if col == w - 1:
                # we have to expand the grid to the east, ant is in (new) col w-1:
                grid = [row + [0] for row in grid]
                w += 1
                col += 1
            else:
                col += 1
        elif direction == 3:
            # go west:
            if col == 0:
                grid = [[0] + row for row in grid]
                w += 1
            else:
                col -= 1
    return grid

