
def paul_cipher(clear_txt):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipher_txt = ''
    clear_txt = clear_txt.upper()
    step = 0
    for ch in clear_txt:
        if ch in alpha:
            indx = (alpha.index(ch) + step) % 26
            cipher_txt += alpha[indx]
            step = alpha.index(ch) + 1
        else:
            cipher_txt += ch
    return cipher_txt

