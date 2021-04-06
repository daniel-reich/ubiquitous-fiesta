
def transpose_matrix(mtx):
    trans = [[mtx[j][i] for j in range(len(mtx))]
              for i in range(len(mtx[0]))]   
    low = []
    for r in trans:
        for w in r:
            low.append(w)
    return ' '.join(low)

