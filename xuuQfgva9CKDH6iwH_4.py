
def simulate_grass(g, x, y):
    H, W = len(g), len(g[0])
    if g[x][y] != 'o':
        return g
    g = [list(r) for r in g]
    queue = [(x, y)]
    while len(queue) > 0:
        x, y = queue.pop(0)
        g[y][x] = '+'
        for x2, y2 in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
            if 0 <= x2 < W and 0 <= y2 < H and g[y2][x2] == 'o' and (x2, y2) not in queue:
                queue.append((x2, y2))
    return [''.join(r) for r in g]

