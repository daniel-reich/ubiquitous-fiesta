
def diagonalize(n, d='ul'):
    matrix = [list(range(n*2-1))[i:i+n] for i in range(n)]
    matrix = list(reversed(matrix)) if d[0] == 'l' else matrix
    return [list(reversed(row)) for row in matrix] if d[1] == 'r' else matrix

