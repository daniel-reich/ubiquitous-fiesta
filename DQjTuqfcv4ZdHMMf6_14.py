
def kaprekar(n):
    '''
    Returns the number of iterations to reach the number 6174 as per the
    instructions, given n is a 4 digit number.
    '''
    if n == 6174:
        return 0
​
    if n < 1000:
        n *= 10
​
    big = int(''.join(sorted([d for d in str(n)], reverse=True)))
    small = int(''.join(sorted([d for d in str(n)])))
​
    return 1 + kaprekar(big - small)

