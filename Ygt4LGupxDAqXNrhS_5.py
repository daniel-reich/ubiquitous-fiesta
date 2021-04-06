
def spotlight_map(grid):
    rows, cols = len(grid), 0
    if rows > 0:
        cols = len(grid[0])
    if rows < 2 and cols < 2:
        return grid
    res = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            for v, h in [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1),
                         (-1, -1), (-1, 1), (1, -1)]:
                if 0 <= r + v < rows and 0 <= c + h < cols:
                    res[r][c] += grid[r + v][c + h]
    return res

