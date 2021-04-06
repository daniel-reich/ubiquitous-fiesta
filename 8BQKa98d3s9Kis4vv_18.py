
def final(r, c, i):
    mat = []
    ops = i
    
    for i in range(r):
        mat.append([0 for i in range(c)])   
    
​
    for i in ops:
        indx, tpe = list(i)
        if tpe == 'r':
            mat[int(indx)] = [i + 1 for i in mat[int(indx)]]
        else:
            for row in range(r):
                mat[row][int(indx)] = mat[row][int(indx)] + 1
    return mat

