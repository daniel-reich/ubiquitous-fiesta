
move = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
def langtons_ant(grd, c, r, n, drn=0):
    for _ in range(n):
        drn = (drn + (1 if grd[r][c] else -1)) % 4
        grd[r][c] = 1 - grd[r][c]
        r += move[drn][0]
        c += move[drn][1]
        if r == -1:
            grd = [[0] * len(grd[0])] + grd
            r = 0
        elif r == len(grd):
            grd += [[0] * len(grd[0])]
        elif c == -1:
            grd = [[0] + row for row in grd]
            c = 0
        elif c == len(grd[0]):
            grd = [row + [0] for row in grd]
    return grd

