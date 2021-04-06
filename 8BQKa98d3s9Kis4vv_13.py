
def final(r, c, i):
    arr = [[0 for _ in range(c)] for _ in range(r)]
    for op in i:
        vec, rc = op[-1], int(op[:-1])
        for ix in range(r if vec=='c' else c):
            if vec=='r':
                arr[rc][ix] += 1
            else:
                arr[ix][rc] += 1
    return arr

