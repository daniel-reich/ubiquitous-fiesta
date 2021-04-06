
def caesar_cipher(text, k):
    '''
    Returns text encrypted by rotating alpha characters k to the right.
    '''
    rotate = lambda x,k: chr(ord('A') + (ord(x) - ord('A')+k)%26) if x.isupper() else \
             chr(ord('a') + (ord(x) - ord('a')+k)%26) if x.islower() else x
​
    return ''.join([rotate(i,k) for i in text])

