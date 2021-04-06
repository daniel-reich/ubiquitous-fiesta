
def dif_ciph(m):
    '''
    Returns a decoded message string if message m is a list of numbers or vice
    versa to encode a string message to a list of numbers as described above.
    '''
    if isinstance(m, str):
        return [ord(m[0])] + [ord(b) - ord(a) for a, b in zip(m, m[1:])]
​
    # decode
    total = 0
    string = ''
    for code in m:
        total += code
        string += chr(total)
​
    return string

