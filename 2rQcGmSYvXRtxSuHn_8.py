
def anticlockwise(M):
    new_matrix = []
    for i in range(len(M[0]), 0, -1):
        new_matrix.append(list(map(lambda x: x[i-1], M)))
    return new_matrix
​
def clockwise(M):
    new_matrix = []
    for i in range(len(M[0])):
        li = list(map(lambda x: x[i], M))
        li.reverse()
        new_matrix.append(li)
    return new_matrix
​
def rotate_matrix(mat, turns=1):
    if turns >= 0:
        turns %= 4
        if turns == 0:
            return mat
        for _ in range(turns):
            mat = clockwise(mat)
        return mat
    turns = abs(turns) % 4
    if turns == 0:
        return mat
    for _ in range(turns):
        mat = anticlockwise(mat)
    return mat

