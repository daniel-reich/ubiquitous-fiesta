
def eight_bit(exp):
    bstr = lambda n: bin(n)[2:] if n >= 0 else bin(256 + n)[2:]
​
    sum, spl = eval(exp), exp.split()
    a, b, op = int(spl[0]), int(spl[2]), spl[1]
    if any(not -128 <= v <= 127 for v in [a, b, sum]): 
        return 'Overflow'
    return (sum, '{} {} {} = {}'.format(bstr(a), op, bstr(b), bstr(sum)))

