
import numpy as np
def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]
def rotate_matrix(mat, turns=1):
    if turns==1:
        return rotated(mat)
    if turns==2:
        return [i[::-1]for i in mat][::-1]
    if turns==3:
        return rotated(mat)[::-1]
    if turns==4:
        return mat
    if turns==-1:
        return [i[::-1]for i in rotated(mat)][::-1]
    if turns==-5:
        a=list(zip(*mat))[::-1]
        return [list(i) for i in a]
    else:
        n=-turns%len(mat)
        a=(mat[:n]+mat[n:])[::-1]
        b=np.array(a).T.tolist()
        return b

