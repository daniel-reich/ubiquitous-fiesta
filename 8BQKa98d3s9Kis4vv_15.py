
def final (r, c, i):
    '''
    Creates a zero filled matrix of r rows and c columns then increments the
    rows and columns in r by 1 for each row / column included as above.
    '''
    matrix = [[0] * c for _ in range(r)]
​
    for idx, dim in i:
        idx = int(idx)
        if dim == 'r':
            matrix[idx] = [cell + 1 for cell in matrix[idx]]
        else:
            for i in range(r):
                matrix[i][idx] += 1
​
    return matrix

