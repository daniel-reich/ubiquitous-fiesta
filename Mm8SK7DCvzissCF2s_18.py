
def in_alpha(word):
    alph = "abcdefghijklmnopqrstuvwxyz"
    a = 0
    for k in word:
        if k in alph:
            a += alph.index(k) +1
    return a%2==0

