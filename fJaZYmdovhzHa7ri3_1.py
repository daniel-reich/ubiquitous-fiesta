
def max_collatz(n):
    '''
    Returns the highest value in the Collatz sequence starting with n
    '''
    return 1 if n == 1 else max(n,(max_collatz(n*3+1) if n%2 else \
                                   max_collatz(n//2)))

