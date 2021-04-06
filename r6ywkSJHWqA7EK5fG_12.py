
def printgrid(rows, cols):
    return [[j for j in range(i,(cols * rows)+1,rows)] for i in range(1,rows+1)]

