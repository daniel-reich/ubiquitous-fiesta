
def crop_hydrated(field):
    w, l = len(field[0]), len(field)
    for r, c in  [(r,c) for r in range(l) for c in range(w) if field[r][c] == 'w']:
        for cr, cc in [(r + dr, c + dc) for dr, dc in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)] ]:
            if 0<=cr<l and 0<=cc<w and field[cr][cc] == 'c':
                field[cr][cc] = 'x'
    return all(all(c != 'c' for c in row) for row in field)

