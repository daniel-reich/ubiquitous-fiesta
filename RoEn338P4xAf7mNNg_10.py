
def shortest_path(lst):
    vertical, horizontal = 0, 0
    coords = []
    
    for r in range(len(lst)):
        for c in range(len(lst[0])):
            if lst[r][c] != '0':
                coords.append((lst[r][c], r, c))
    coords.sort()
    
    for (_, r1, c1), (_, r2, c2) in zip(coords, coords[1:]):
        vertical += abs(r1 - r2)
        horizontal += abs(c1 - c2)
    
    return vertical + horizontal

