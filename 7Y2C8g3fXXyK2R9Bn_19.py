
from string import ascii_lowercase
def keyword_cipher(key, message):
    alpha = ''
    cipher = ''
    for ch in key:
        if ch not in alpha:
            alpha += ch
    for ch in ascii_lowercase:
        if ch not in alpha:
            alpha += ch
    for ch in message:
        if ch in ascii_lowercase:
            indx = ascii_lowercase.index(ch)
            cipher += alpha[indx]
        else:
            cipher += ch
    return cipher

