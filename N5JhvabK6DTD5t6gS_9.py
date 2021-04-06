
def markdown(symb):
    def inner(s, w):
        z = [symb+x+symb if f(x, w) else x
             for x in s.split()]
        return ' '.join(z)
    def f(x, w):
        lop = ('.', '!', '?')
        for p in lop:
            x = x.replace(p, '')
        return x.lower() == w.lower()
    return inner

