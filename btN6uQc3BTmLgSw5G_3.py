
def spiral_matrix(n, s):
    res = [[''] * n for _ in range(n)]
    if len(s) < n * n:
        s += '+' * (n * n - len(s))
    rc = cc = n // 2 if n % 2 else (n - 1) // 2
    res[rc][cc], res[rc][cc + 1] = s[0], s[1]
    res[rc + 1][cc + 1], res[rc + 1][cc] = s[2], s[3]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    idx_dirs, r, c = 2, rc + 1, cc
    for i in range(4, n * n):
        if idx_dirs == 0:
            if not res[r + 1][c]:
                idx_dirs = (idx_dirs + 1) % 4
        elif idx_dirs == 1:
            if not res[r][c - 1]:
                idx_dirs = (idx_dirs + 1) % 4
        elif idx_dirs == 2:
            if not res[r - 1][c]:
                idx_dirs = (idx_dirs + 1) % 4
        elif idx_dirs == 3:
            if not res[r][c + 1]:
                idx_dirs = (idx_dirs + 1) % 4
        r, c = r + dirs[idx_dirs][0], c + dirs[idx_dirs][1]
        res[r][c] = s[i]
    return res

