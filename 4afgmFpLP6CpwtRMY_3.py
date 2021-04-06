
def sudoku_validator(x):
    rows, cols, sqrs = [s for s in [set() for _ in range(9)]], [s for s in [set() for _ in range(9)]], [s for s in [set() for _ in range(9)]]
    for i in range(81):
        r, c = i // 9, i % 9
        s = (r // 3) * 3 + (c // 3)
        rows[r].add(x[r][c])
        cols[c].add(x[r][c])
        sqrs[s].add(x[r][c])
    return all(len(v) == 9 for v in rows + cols + sqrs)

