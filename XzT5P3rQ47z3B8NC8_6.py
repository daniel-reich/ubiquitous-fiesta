
from string import ascii_lowercase
def condi_cipher(msg, key, shift):
    alpha = ""
    cipher = ""
    for ch in key:
        if ch not in alpha:
            alpha += ch
    for ch in ascii_lowercase:
        if ch not in alpha:
            alpha += ch
    for i in range(len(msg)):
        if msg[i] in alpha:
            indx = alpha.index(msg[i]) 
            pos = (indx + shift) % 26
            cipher += alpha[pos]
            shift = indx + 1
        else:
            cipher += msg[i]
    return cipher

