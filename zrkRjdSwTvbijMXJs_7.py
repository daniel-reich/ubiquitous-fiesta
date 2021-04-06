
def pad_helper(text, pad, mode):
    '''
    Helper function for encrypt(mode = 'encrypt') or decrypt(mode = 'decrypt')
    Carries out encryption / decryption as above
    '''
    from operator import add, sub  # for use in the modular arithmetic
    
    if mode == 'encrypt':
        f = sub
        start = 0
        prefix = pad[0:5]
    else:
        if text[0:5] != pad[0:5]:
            return "Error: Key IDs don't match."
        f = add
        start = 5
        prefix = ''
    pad = pad[5:]   # move past the pad id
​
    return prefix + ''.join(str(f(int(char), int(pad[i])) %10) for i, char in enumerate(text[start:]))
​
def encrypt(text, pad):
    '''
    Encrypts text with pad as described above
    '''
    return pad_helper(text, pad, 'encrypt')
​
def decrypt(cipher, pad):
    '''
    Decrypts cipher with pad as described above
    '''
    return pad_helper(cipher, pad, 'decrypt')

