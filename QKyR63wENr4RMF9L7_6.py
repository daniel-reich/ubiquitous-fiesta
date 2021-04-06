
def tweak_letters(txt, lst):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(alpha[x] for x in [(alpha.index(i)+j)%26 for i,j in zip(txt, lst)])

