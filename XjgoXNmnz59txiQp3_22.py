
def split(n):
    '''
    Returns the biggest product for natural numbers (positive integers) whose
    sum equals n
    '''
    if n == 1:
        return 1
​
    pow3 = n // 3
    rem = n % 3
    if rem == 1:
        pow3 -= 1   # drop a power of 3
​
    return 3**pow3 * 2**((n-3*pow3)//2)

