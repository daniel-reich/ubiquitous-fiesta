
def clockwise_cipher(txt):
    '''
    Returns txt scrambled via the clockwise square cipher as per instructions.
    '''
    from math import ceil
​
    size = len(txt)
    d = ceil(size**0.5)   # dimension of the square
    grid = [[' ' for _ in range(d)] for _ in range(d)]  # space fill grid
    place(txt, grid, size, d)
​
    return ''.join(grid[i][j] for i in range(d) for j in range(d))
​
def place(txt, grid, size, d):
    '''
    Places the characters in txt into grid as per the clockwise square algorithm
    '''
    m = d // 2  # the midpoint of the grid
    p = 0
    for i in range(m):
        for j in range(i, d-i-1):
            for r, c in ((i,j),(j,d-i-1),(d-i-1,d-j-1),(d-j-1,i)):
                grid[r][c] = txt[p]
                p += 1
                if p == size:
                    return  # finished populating grid
    grid[m][m] = txt[-1]   # d is odd and size = d^2

