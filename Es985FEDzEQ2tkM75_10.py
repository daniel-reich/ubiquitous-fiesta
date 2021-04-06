
def caesar_cipher(txt, key):
    alph = "abcdefghijklmnopqrstuvwxyz"
    txt = list(txt.lower ())
    for i in range (len(txt)) :
        if txt[i] in alph :
            txt[i] = alph [(alph.index(txt[i])+key)%26]
    return ''.join(txt)

