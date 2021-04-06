
def square_root(n):
    '''
    Returns the square root of the perfect square number n
    '''
    a, b = n, 1
    while a > b:
        a = (a + b) // 2
        b = n // a
​
    return a

