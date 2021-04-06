
def is_magic(square):
    ln = len(square)
    for r in square:
        if len(r) != ln:
            return False
    big = ln**2
    for i in range(ln):
        for j in range(ln):
            if square[i][j] > big:
                return False
    los = []
    los += [sum(r) for r in square]
    los += [sum(r) for r in map(list, zip(*square))]
    d1 = 0
    for i in range(ln):
        d1 += square[i][i]
    los.append(d1)
    d2 = 0
    for i in range(ln-1,-1,-1):
        d2 += square[i][i]
    los.append(d2)
    return len(set(los)) == 1

