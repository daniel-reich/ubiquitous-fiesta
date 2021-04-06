
def hot_brick(time_span):
    n = 10
    res = [[25] * n for _ in range(n - 1)] + [[90] * n]
    contiguous = [[0] * n for _ in range(n - 1)]
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1),
                 (-1, -1), (1, 1), (1, -1), (-1, 1)]
    right_neighbors = [tpl for tpl in neighbors
                       if tpl not in [(-1, -1), (0, -1), (1, -1)]]
    down_neighbors = [tpl for tpl in neighbors
                      if tpl not in [(-1, -1), (-1, 0), (-1, 1)]]
    for _ in range(time_span):
​
        for r in range(1, n - 1):
            for c in range(1, n - 1):
                contiguous[r][c] = sum(res[r + tpl[0]][c + tpl[1]]
                                       for tpl in neighbors)
            contiguous[r][0] = (sum(res[r + tpl[0]][tpl[1]]
                                    for tpl in right_neighbors) + 25 * 3)
            contiguous[r][n - 1] = contiguous[r][0]
​
        for c in range(1, n - 1):
            contiguous[0][c] = (sum(res[tpl[0]][c + tpl[1]]
                                    for tpl in down_neighbors) + 25 * 3)
        contiguous[0][0] = (res[0][1] + res[1][1] + res[1][0] + 25 * 5)
        contiguous[0][n - 1] = contiguous[0][0]
​
        for r in range(n - 1):
            for c in range(n):
                res[r][c] = round((contiguous[r][c] + res[r][c]) / 9)
​
    return res

