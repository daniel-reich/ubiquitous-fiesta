
def rotate_matrix(mat, turns=1):
    turns =  turns%4
    if turns < 0:
        turns += 4
    if turns == 0:
        return mat 
    for i in range (0,turns):
        mat = rotate_1turn(mat)
    return mat
def rotate_1turn(mat):
    rows = len(mat)
    return [ [mat[rows - j - 1][i] for j in range(0,rows)] 
        for i in range(0,len(mat[0])) ]

