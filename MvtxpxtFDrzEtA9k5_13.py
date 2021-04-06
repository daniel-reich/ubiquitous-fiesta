
def palindrome_descendant(n):
    '''
    Returns True if the digits in n or its descendants down to 2 digits derived
    as above are.
    '''
    str_n = str(n)
    
    if str_n == str_n[::-1] and len(str_n) != 1:
        return True
​
    if len(str_n) % 2 == 1:
        return False  # Cannot produce a full set of pairs
​
    
    return palindrome_descendant(int(''.join(str(int(str_n[i]) + int(str_n[i+1])) \
                                     for i in range(0, len(str_n), 2))))

