
def diagonalize(n, d):
    if d == 'ul':
        return [[j for j in range(j,n + j)] for j in range(0,n)]
    elif d == 'ur':
        return [[j for j in range(j, j-n ,-1)] for j in range(n - 1, n-1 + n)]
    elif d == 'll':
        return list(reversed([[j for j in range(j,n + j)] for j in range(0,n)]))
    elif d == 'lr':
        return list(reversed([[j for j in range(j, j-n ,-1)] for j in range(n - 1, n-1 + n)]))

