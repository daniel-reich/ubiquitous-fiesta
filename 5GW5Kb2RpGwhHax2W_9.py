
def spiral_transposition(lst):
    w, h = len(lst[0]), len(lst)
​
    is_blocked = lambda r, c, dr, dc: not(0<=r+dr<h and 0<=c+dc<w and lst[r+dr][c+dc] >= 0)
​
    r, c, dr, dc, res, done = 0, 0, 0, 1, [], False
    while True:
        res.append(lst[r][c])
        lst[r][c] = -1
        if is_blocked(r, c, dr, dc):
            dr, dc = dc, -dr
            if is_blocked(r, c, dr, dc):
                return res
        r,c = r+dr, c+dc

