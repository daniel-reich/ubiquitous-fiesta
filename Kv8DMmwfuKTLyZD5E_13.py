
def make_dartboard(n):
    def right():
        nonlocal i, j
        while j < n-lvl: brd[i][j] = lvl+1; j += 1
        j = j - 1
    def down():
        nonlocal i, j
        while i < n-lvl: brd[i][j] = lvl+1; i += 1
        i = i - 1
    def left():
        nonlocal i, j
        while j >= 0+lvl: brd[i][j] = lvl+1; j -= 1
        j = j + 1
    def up():
        nonlocal i, j
        while i >= 0+lvl: brd[i][j] = lvl+1; i -= 1
        i = i + 1
    def seq():
        nonlocal i, j, lvl
        right(); down(); left();up()
        i += 1; j += 1; lvl += 1
    brd = [[0]*n for i in range(n)]; i = 0; j = 0; lvl = 0
    while not all(e > 0 for r in brd for e in r): seq()
    for r in range(n):
        for e in range(n):
            brd[r][e] = str(brd[r][e])
    return [int(''.join(r)) for r in brd]

