
def deadly_virus(grid, n):
    v_set, rows, cols = set(), len(grid), len(grid[0])
    for r, row in enumerate(grid):
        for c, v in enumerate(row):
            if v == "V":
                v_set.add((r, c))
    for _ in range(n):
        new_set = set()
        for p in v_set:
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r = p[0] + i
                c = p[1] + j
                if -1 < r < rows and -1 < c < cols:
                    new_set.add((r, c))
        v_set.update(new_set)
    res = [["P"] * cols for _ in range(rows)]
    for r, c in v_set:
        res[r][c] = "V"
    return res

