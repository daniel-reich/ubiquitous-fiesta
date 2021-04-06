
def diagonalize(n,d):
    array = []
    total = 0
    for i in range(n):
        array.append([])
        for j in range(n):
            array[i].append(0)
    if d == 'ul':
        for k in range(n):
            for h in range(n):
                array[k][h] = h + k
    elif d == 'ur':
        for k in range(n):
            for h in range(n):
                array[k][n-h-1] = h + k
    elif d == 'll':
        for k in range(n):
            for h in range(n):
                array[n-k-1][h] = h + k
    else:
        for k in range(n):
                for h in range(n):
                    array[n-k-1][n-h-1] = h + k
    return array

