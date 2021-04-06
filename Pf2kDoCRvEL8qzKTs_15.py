
def order_people(dims, n):
    '''
    Returns a 2d snake style grid with people numbered as per the instructions,
    or error message if n won't fit.
    '''
    r, c = dims
    if r * c < n:
        return 'overcrowded'
​
    queue = [[i*c+j if i*c+j <= n else 0 for j in range(1, c+1)] for i in range(r)]
    for i, line in enumerate(queue):
        if i % 2 == 1:
            line.reverse()
​
    return queue

