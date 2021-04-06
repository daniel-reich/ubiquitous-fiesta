
def minesweeper_numbers(b):
    res = []
    if b:
        rows, cols = len(b), len(b[0])
        res = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if b[r][c]:
                    res[r][c] = 9
                else:
                    n_neighbors = 0
                    for i, j in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
                                 (1, -1), (1, 0), (1, 1)]:
                        if (0 <= r + i < rows and 0 <= c + j < cols
                                and b[r + i][c + j]):
                            n_neighbors += 1
                    res[r][c] = n_neighbors
    return res

