
def to_base(n, b):
    '''
    Returns a string representation of natural number n expressed in base b
    '''
    b_str = ''
    while n > 0:
        b_str = str(n % b) + b_str
        n //= b
​
    return '0' if b_str == '' else b_str
​
def esthetic(n):
    '''
    Returns a list of the bases from 2 to 10 inclusive in which n is aesthetic
    as defined in the instructions, or the string Anti-Esthetic if there are
    none.
    '''
    bases = [to_base(n, base) for base in range(2, 11)]
    aesthetics = [base for base in range(2, 11) if all(abs(int(a) - int(b)) == 1 \
                  for a, b in zip(bases[base-2],bases[base-2][1:]))]
    
    return aesthetics if len(aesthetics) > 0 else 'Anti-Esthetic'

