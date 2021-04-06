
def simulate_grass(g, x, y):
    res = [[c for c in row] for row in g]
    rows, cols = len(res), len(res[0])
    dirt = set((r, c) for r in range(rows) for c in range(cols)
               if res[r][c] == 'o')
    grass = set()
    if (x, y) in dirt:
        grass.add((x, y))
        dirt -= {(x, y)}
        neighbors = [(x, y)]
        while neighbors:
            new_neighbors = []
            for r, c in neighbors:
                for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_rc = (r + i, c + j)
                    if new_rc in dirt:
                        grass.add(new_rc)
                        new_neighbors.append(new_rc)
                        dirt -= {new_rc}
            neighbors = new_neighbors
    for r, c in grass:
        res[r][c] = '+'
    return [''.join(row) for row in res]

