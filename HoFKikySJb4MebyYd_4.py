
def transform_matrix(lst):
    cols = {i: sum(x) for i,x in enumerate(zip(*lst))}
    rows = {i: sum(x) for i,x in enumerate(lst)}
    mat = [[0 for y in range(len(lst[0]))]for x in range(len(lst))]
​
    for i,x in enumerate(lst):
        for j,y in enumerate(x):
            total = (rows[i] - y) + (cols[j] - y)
            mat[i][j] = total
    return mat

