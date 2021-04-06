
def encryption(string):
    import math
​
    # remove whitespace
    string = string.replace(' ', '')
​
    # the number of rows and cols
    # is dependent on the square
    # root of the length
    l = len(string)
    m = math.floor(math.sqrt(l))
    n = math.ceil(math.sqrt(l))
​
    # make sure the matrix is large
    # enough to hold the string
    while m * n < l:
        # always increment the
        # smaller dimension
        if m <= n:
            m += 1
​
        else:
            n += 1
​
    # create matrix of dim m x n
    matrix = [[0] * m for _ in range(n)]
​
    # add the chars into the matrix
    i = 0; j = 0
    for c in string:
        matrix[j][i] = c
​
        # update index values
        if j == n - 1:
            i += 1
            j = 0
​
        else:
            j += 1
​
    for (i, col) in enumerate(matrix):
        # remove placeholder zeros
        col = [c for c in col if c]
​
        # join rows into a string
        matrix[i] = ''.join(col)
​
    # join each col into a string
    encryptedString = ' '.join(matrix)
​
    return encryptedString

