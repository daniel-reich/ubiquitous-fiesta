
def vigenere(txt,key):
    '''
    Encrypts or decrypts txt using keyword key based on the vigenere caesar
    cipher as per the instructions
    '''
    from math import ceil
    from operator import add, sub
    
    BASE = ord('A')   # ASCII code for capital A
    
    if all(l.isupper() for l in txt):  # decrypting
        txt = list(txt)
        op = sub
    else:
        txt = [l.upper() for l in txt if l.isalpha()] # remove non letters
        op = add
        
    size = len(txt)
    key = (key.upper() * ceil(size/len(key)))[:size]  # line up key with text
    
    return ''.join(chr(BASE + op(ord(l),ord(key[i]))%26)
                   for i, l in enumerate(txt)) # decrypt / decrypt txt

