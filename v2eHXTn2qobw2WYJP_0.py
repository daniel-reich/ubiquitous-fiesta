
def minesweeper_numbers(bd):
    for r in range(len(bd)):
        for c in range(len(bd[0])):
            if bd[r][c] == 1:
                bd[r][c] = 9
                
    for r in range(len(bd)):
        for c in range(len(bd[0])):
            if bd[r][c] == 0:
                bd[r][c] = f(bd, r, c)
    return bd
​
def f(b, x , y):
    cnt = 0
    for x, y in [(x-1, y-1), (x-1, y), (x-1, y+1),
                 (x+1, y-1), (x+1, y), (x+1, y+1),
                 (x, y-1), (x, y+1)]:
        cnt += is_mine(b, x, y)
    return cnt
​
def is_mine(b, x, y):
    if (0 <= x < len(b) and
        0 <= y < len(b) and
        b[x][y] == 9):
        return 1
    return 0

