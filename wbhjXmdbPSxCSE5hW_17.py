
def sigilize(s):
    l = [ x for x in s.upper() if x.isalpha() and x not in 'AEIOU'][::-1]
    return ''.join(sorted(set(l), key= l.index))[::-1]

