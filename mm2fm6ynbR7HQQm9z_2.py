
s = "-ABCDEFGH"
def knights_jump(sqr):
    r, c = s.index(sqr[0]), int(sqr[1])
    res = []
    for i, j in [(-2, 1), (-2, -1), (-1, 2), (-1, -2),
                 (2, 1), (2, -1), (1, 2), (1, -2)]:
        row, col = r + i, c + j
        if 0 < row < 9 and 0 < col < 9:
            res.append([row, col])
    res.sort(key=lambda p: (p[1], p[0]))
    return ",".join(s[p[0]] + str(p[1]) for p in res)

