
def diamond(n):
    '''
    Returns a 2d grid representing the cut and a cut description for an n-carat
    diamond as per instructions.
    '''
    if n % 2 == 1:
        cut = 'perfect cut'
        size = n
        k = 1
    else:
        cut = 'good cut'
        size = n - 1
        k = 0
​
    diamond = [[0] * n for _ in range(size)]
    j = mid = size//2
​
    for i in range(size):
        diamond[i][j] = diamond[i][size-j-k] = 1
        j = j - 1 if i < mid else j + 1
​
    return [diamond, cut]

