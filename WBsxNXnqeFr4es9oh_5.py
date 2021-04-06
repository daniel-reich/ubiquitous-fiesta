
import math
def clockwise_cipher(message):
    gs = math.ceil(len(message) ** 0.5)
    order = math.ceil(gs / 2)
    grid = [[' '] * gs for _ in range(gs)]
    coords = []
    output = ''
    for j in range(order):
        gsb = gs - (j * 2)
        for i in range(gsb - 1):
            p1 = [j, i + j]
            p2 = [i + j, gsb - 1 + j]
            p3 = [gsb - 1 + j, gsb - 1 - i + j]
            p4 = [gsb - 1 - i + j, j]
            coords += p1, p2, p3, p4
    if gs ** 2 == len(message):
        coords += [[order - 1, order - 1]]
​
    for i in range(len(message)):
        c1 = coords[i][0]
        c2 = coords[i][1]
        grid[c1][c2] = message[i]
​
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            output += grid[i][j]
    return output

