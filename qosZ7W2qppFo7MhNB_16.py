
def hex_distance(grid):
    p = []; c = len(grid); mid = (c + 1) / 2
    for [m, i] in list(zip(*[grid, range(c)])):
        grid[i] = ''.join([k for k in m if k != ' '])
    [p.append([i, abs(mid - (i + 1)) * 0.5 + j]) if le == 'x' else 0 for [m, i] in
     list(zip(*[grid, range(c)])) for [le, j] in list(zip(*[m, range(len(m))]))]
    li, co = abs(p[1][0] - p[0][0]), abs(p[1][1] - p[0][1])
    return round(li + co - min(li / 2, co))

