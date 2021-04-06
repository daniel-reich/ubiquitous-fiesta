
def transpose_matrix(mtx):
    return ' '.join([mtx[j][i] for i in range(len(mtx[0]))for j in range(len(mtx))])

