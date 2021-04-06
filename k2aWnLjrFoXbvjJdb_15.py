
def vigenere(s, cip):
    decr = s.isupper()
    k = -1 if decr else 1
    l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lenl = len(l)
    ix = dict((x,y) for y,x in enumerate(l))
    s, cip = [x.upper() for x in (s,cip)]
    s = [c for c in s if c in ix]
    cip = (cip*((len(s)-1) // len(cip) + 1))[:len(s)]
    return ''.join(l[(lenl + k*ix[cc] + ix[cs]) % lenl] for cs, cc in zip(s, cip))

