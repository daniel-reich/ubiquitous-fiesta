
def final(r, c, i):
    matrix = [[0 for i in range(c)] for j in range(r)]
    for d in i:
        if "r" in d:
            row(matrix, int(d[0]))
        else:
            column(matrix, int(d[0]))
    return matrix
    
def row(matrix, num):
    for r in range(len(matrix[num])):
        matrix[num][r] += 1
    return matrix
    
def column(matrix, num):
    for c in range(len(matrix)):
        matrix[c][num] += 1
    return matrix

