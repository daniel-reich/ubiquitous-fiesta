
def palindrome_type(n):
    '''
    Returns the type of palindrome which can be formed from decimal and binary
    representations of positive integer n as per injstructions
    '''
​
    TYPES = ('Neither!', 'Decimal only.', 'Binary only.', 'Decimal and binary.')
    dec_pal = 1 if str(n) == str(n)[::-1] else 0
    bin_pal = 2 if bin(n)[2:] == bin(n)[2:][::-1] else 0
​
    return TYPES[dec_pal + bin_pal]

