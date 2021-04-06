
def conjugate(verb, pronoun):
    res = '{} {}{}'
    pronoun_sufx = {
        1: ('Io', 'o'),
        2: ('Tu', 'i'),
        3: ('Egli', 'a'),
        4: ('Noi', 'iamo'),
        5: ('Voi', 'ate'),
        6: ('Essi', 'ano'),
    }
    root = verb[:-3]
    if root[-1] in ('c', 'g',) and pronoun in (2, 4):
        res = res.format(pronoun_sufx[pronoun][0], 
    root + 'h', 
    pronoun_sufx[pronoun][1])
    elif root[-1] == 'i' and pronoun in (2, 4):
        res = res.format(pronoun_sufx[pronoun][0],
    root[:-1],
    pronoun_sufx[pronoun][1])
    else:
        res = res.format(pronoun_sufx[pronoun][0],
    root,
    pronoun_sufx[pronoun][1])
    return res

