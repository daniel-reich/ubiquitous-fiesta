
def islands_perimeter(grid):
    rows, cols = len(grid), len(grid[0])
    grid = [[0]*(cols+4)]*2 + [[0, 0] + i + [0, 0] for i in grid] + [[0]*(cols+4)]*2
​
    perimeter = 0
    for r in range(1, rows + 3):
        for c in range(1, cols + 3):
            if grid[r][c] == 0:
                for i, j in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                    if grid[r+i][c+j] == 1:
                        perimeter += 1
    return perimeter

