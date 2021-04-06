
def printgrid(rows, cols):
    r = []
    for i in range(1,rows+1):
        r.append([j for j in range(i,rows*cols+1,rows)])
    return r

