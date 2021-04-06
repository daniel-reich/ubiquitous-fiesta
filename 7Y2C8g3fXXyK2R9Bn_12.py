
def keyword_cipher(key, m):
    a = 'abcdefghijklmnopqrstuvwxyz'
    code = [i for l,i in enumerate(key) if i not in key[:l]]+ sorted({letter for letter in a if letter not in key })
    return ''.join(code[a.index(letter)] if letter.isalpha() else letter for letter in m)

