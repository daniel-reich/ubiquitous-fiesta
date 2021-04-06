
def rolling_cipher(txt, n):
    return ''.join(chr((((ord(s) + n)-97)%26)+97) for s in txt)

