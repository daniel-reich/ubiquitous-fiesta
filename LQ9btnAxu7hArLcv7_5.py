
def increment_arr(lst):
    for i,a in enumerate(lst):
        if i == 0:
            continue
        for j,b in enumerate(a): 
            lst[i][j] = lst[i-1][j] + 1
    return lst
            
    
def diagonalize(n:int,s:str):
    mat = []
    mat = [[0 for m in range(n)]for i in range(n)]
    mat[0] = [i for i in range(len(mat[0]))]       
    mat = increment_arr(mat)
    if s == 'ul':
        return mat
    if s == 'll':
        mat = mat[::-1]
        return mat
    if s == 'ur':
        g = [i[::-1] for i in mat]
        return g
    if s == 'lr':
        g = [i[::-1] for i in mat]
        g = g[::-1]
        return g
        
    return mat

