
def bell(n):
    res = [[1]]
    for r in range(1, n):
        row = [res[r - 1][-1]] + [0] * r
        for c in range(1, len(row)):
            row[c] = row[c - 1] + res[r - 1][c - 1]
        res.append(row)
    return res[-1][-1]

