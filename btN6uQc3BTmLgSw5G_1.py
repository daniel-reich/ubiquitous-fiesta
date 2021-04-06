
def spiral_matrix(side, s):
    s = '{:+<{}}'.format(s, side**2)[:side**2]
    arr = [[''] * side for _ in range(side)]
    k = side//2
    r, c = (k, k) if side%2 else (k-1, k-1)
​
    direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
    arr[r][c] = s[0]
    move, d, pos = 1, 0, 1
​
    while True:
        for _ in range(2):
            for m in range(move):
                i, j = direction[d%4]
                r, c = r+i, c+j
                arr[r][c] = s[pos]
                pos += 1
                if pos == len(s):
                    return arr
            d += 1
        move += 1

