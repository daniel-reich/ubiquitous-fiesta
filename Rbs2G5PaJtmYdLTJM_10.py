
def is_heteromecic(n):
    '''
    Returns whether n is a pronic number as defined in the instructions
    '''
    sqrt = int((1+4*n)**0.5)  # derived from quadratic -b + sqrt(b^2-4ac)
​
    return not n%2 and sqrt*sqrt == 4*n+1

