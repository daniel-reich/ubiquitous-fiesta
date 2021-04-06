
def make_dartboard(n):
    '''
    Returns a square dartboard of side n as per the instructions
    '''
    def update_square(square, n, i, val):
        '''
        Updates square with the square derived from i
        '''
        for j in range(i, n-i):
            for k in range(i, n-i):
                square[j][k] = val
    
    square = [[1] * n for _ in range(n)]
    
    if n % 2 == 0:
        vals = list(range(2,n//2+1)) + list(range(n//2,1,-1))
    else:
        vals = list(range(2,n//2+2)) + list(range(n//2,1,-1))
    
    for i in range(1, n-1):
        update_square(square, n, i, vals[i-1])
​
    return [int(''.join([str(i) for i in row])) for row in square]

