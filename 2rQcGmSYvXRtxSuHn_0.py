
def rotate_matrix(mat, turn=1):
    if not turn%4: return mat
    return [list(reversed(i)) for i in zip(*rotate_matrix(mat, turn%4-1))]

