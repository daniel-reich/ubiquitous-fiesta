
def rolling_cipher(txt, n):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    alpha = list(alph)
    alist = list(txt)
    newword = ''
    for i in alist:
        x = alpha.index(i)
        x += n
        if x > 25:
            x -= 26
        elif x < 0:
            x += 26
        newlet = alpha[x]
        newword = newword + newlet
    return(newword)

