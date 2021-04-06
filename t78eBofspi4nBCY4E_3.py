
def base_conv(n, b):
    '''
    Returns n in base b - using letters as per instructions - if n is an integer
    or the decimal equivalent of n if it is a base b number in letters. Error
    message if letter number cannot be converted from base b.
    '''
​
    def d2b(n, b, b_dict):
        '''
        Converts decimal integer n to base b using num/letter b_dict
        '''
        b_str = ''
        while n > 0:
            b_str = b_dict[n%b] + b_str
            n //= b
​
        return b_str
​
    def b2d(n, b, b_dict):
        '''
        Converts base letter number n to decimal using num/letter dict
        '''
        size = len(n)
        
        return sum(b**(size-i-1) * b_dict[l] for i, l in enumerate(n))
    
    BASE_DICT = {i: chr(ord('a')+i) for i in range(26)}
    BASE_DICT.update({l:i for i,l in BASE_DICT.items()})  # number/ letter dict
​
    if isinstance(n, int):
        return d2b(n, b, BASE_DICT)  # create base string
​
    if any(not l.isalpha() or BASE_DICT[l] >= b for l in n):
        return '{} is not a base {} number.'.format(n, b)
​
    return b2d(n, b, BASE_DICT)

