
def num_regions(grid):
    ones = set()
    for r, row in enumerate(grid):
        for c, v in enumerate(row):
            if v:
                ones.add((r, c))
    res = 0
    while ones:
        start = ones.pop()
        link = [start]
        while link:
            new_link = []
            for p in link:
                for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    neighbor = (p[0] + i, p[1] + j)
                    if neighbor in ones:
                        new_link.append(neighbor)
                        ones.remove(neighbor)
            link = new_link
        res += 1
    return res

