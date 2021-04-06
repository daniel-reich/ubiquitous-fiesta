
def most_overlapped_block(grid_width, points):
    grid = [[0 for _ in range(grid_width)] for __ in range(grid_width)]
    for x, y, dist in points:
        row = y - 1
        col = x - 1
        for r in range(max(0, row-dist), min(grid_width, row+dist+1)):
            for c in range(max(0, col-dist), min(grid_width, col+dist+1)):
                if abs(r - row) + abs(c - col) <= dist:
                    grid[r][c] += 1
    return max([max(row) for row in grid])

