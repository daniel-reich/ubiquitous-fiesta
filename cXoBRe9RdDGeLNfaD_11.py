
nbin = lambda x: bin(256+x if x<0 else x)[2:]
​
def eight_bit(exp):
    a, o, b = exp.split()
    a, b, s = map(int, (a, b, o+'1'))
    c = a + b*s
    if all(-129<i<128 for i in (a, b, c)):
        return (c, '{} {} {} = {}'.format(nbin(a), o, nbin(b), nbin(c)))
    return "Overflow"

