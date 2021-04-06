
def islands_perimeter(grid):
    rows, cols = len(grid), len(grid[0])
    land = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]:
                land.add((r, c))
    perimeter = 0
    for r, c in land:
        neighbours = 0
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (r + i, c + j) in land:
                neighbours += 1
        perimeter += 4 - neighbours
    return perimeter

