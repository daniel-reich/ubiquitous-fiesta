
def move(mat):
    def inner(d):
        nonlocal w, h, x, y
        if d == "up": y = (y-1) % h
        elif d == "down": y = (y+1) % h
        elif d == "left": x = (x-1) % w
        elif d == "right": x = (x+1) % w
        else:
            res = [[0]*w for _ in range(h)]
            res[y][x] = 1
            return res
        return inner
​
    w, h = len(mat[0]), len(mat)
    i = sum(mat, []).index(1)
    x, y = i%w, i // w
    return inner

