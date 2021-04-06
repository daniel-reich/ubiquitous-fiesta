
def fibonacci(n):
    '''
    Returns the fibonacci value of n, given n is a positive power of 2
    '''
    i, j, k, h, t = 1, 0, 0, 1, 0
​
    while n > 0:
        if n == 1:  # final iteration
            t = j * h
            j = i * h + j * k + t
            i = i * k + t
​
        t = h**2
        h = 2 * k * h + t
        k = k**2 + t
        n //= 2
​
    return j

