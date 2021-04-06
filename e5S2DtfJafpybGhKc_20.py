
def rotate(mat):
    l = len(mat)
    return [[mat[i][j] for i in range(l-1,-1,-1)] for j in range(l)]

