
def spiral_transposition(lst):
    minrow, mincol = 0, 0,
    maxrow, maxcol = len(lst)-1, len(lst[0])-1
    step, lout, stepmax = 0, [], (maxrow+1)*(maxcol+1)
    while step < stepmax:
        for y in range(mincol, maxcol+1):
            lout.append(lst[minrow][y])
            step += 1
        minrow += 1
        for x in range(minrow, maxrow+1):
            lout.append(lst[x][maxcol])
            step += 1
        maxcol -= 1
        for y in range(maxcol, mincol-1, -1):
            lout.append(lst[maxrow][y])
            step += 1
        maxrow -= 1
        for x in range(maxrow, minrow-1, -1):
            lout.append(lst[x][mincol])
            step+=1
        mincol += 1
    return lout

