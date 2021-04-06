
def spiral_order(m):
    res = []
    while m:
        res += m[0]
        m = m[1:]
        if not m:
            break
        right_wall = []
        for r, row in enumerate(m):
            right_wall.append(row[-1])
            m[r] = row[:-1]
        res += right_wall
        if not m:
            break
        res += m[-1][::-1]
        m = m[:-1]
        if not m:
            break
        left_wall = []
        for r in range(len(m) - 1, -1, -1):
            left_wall.append(m[r][0])
            m[r] = m[r][1:]
        res += left_wall
    return res

