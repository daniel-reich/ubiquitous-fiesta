
def concatenation_sum(n):
    if n < 10:
        return n
    
    size = len(str(n))
    pre_total = int('{}{}9'.format(size-2, '8'*(size-2)))
    remainder = (n - int('9'*(size-1))) * size
    
    return pre_total + remainder

