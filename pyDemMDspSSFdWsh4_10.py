
def digital_decipher(eMessage, key):
    '''
    Returns eMessage deciphered with key as per the examples
    '''
    TABLE = {i:chr(ord('a')+i-1) for i in range(1,27)} # maps numbers to letters
    e_size, k_size = len(eMessage), len(str(key))
    
    # get key same size as eMessage
    key = str(key) * (e_size // k_size) + str(key)[:(e_size % k_size)]
​
    return ''.join(TABLE[c - int(key[i])] for i, c in enumerate(eMessage))

