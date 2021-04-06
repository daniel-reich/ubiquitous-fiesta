
def harry(po):
    rows, cols = len(po), 0
    if rows > 0:
        cols = len(po[0])
    if cols == 0:
        return -1
    for r in range(rows):
        for c in range(cols):
            if r == 0:
                if c > 0:
                    po[r][c] += po[r][c - 1]
            elif c == 0:
                po[r][c] += po[r - 1][c]
            else:
                po[r][c] += max(po[r][c - 1], po[r - 1][c])
    return po[rows - 1][cols - 1]

