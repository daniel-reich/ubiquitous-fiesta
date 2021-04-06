
def rolling_cipher(txt, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    emptystring = ''
    for eachletter in txt:
        if n < 1:
            emptystring += alphabet[alphabet.index(eachletter)+n % -25]
        else:
            emptystring += alphabet[(alphabet.index(eachletter)+n) % 26]
    return emptystring

