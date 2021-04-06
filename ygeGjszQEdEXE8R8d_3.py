
def move(mat):
    matt = [[c for c in row] for row in mat]
    rows, cols = len(matt), len(matt[0])
​
    def f(txt):
        if txt == 'stop':
            return matt
        rr, cc = 0, 0
        for r_idx, row in enumerate(matt):
            if 1 in row:
                rr = r_idx
                cc = row.index(1)
                break
        new_r, new_c = rr, cc
        if txt == 'up':
            new_r = (rr - 1) % rows
        elif txt == 'down':
            new_r = (rr + 1) % rows
        elif txt == 'left':
            new_c = (cc - 1) % cols
        elif txt == 'right':
            new_c = (cc + 1) % cols
        matt[rr][cc] = 0
        matt[new_r][new_c] = 1
        return f
    return f

