
def reduce_frac(n, d):
    for i in range(min(n, d), 0, -1):
        if not n%i and not d%i:
            return '{}/{}'.format(n//i, d//i)
​
def mixed_number(frac):
    n, d = map(int, frac.lstrip('-').split('/'))
    sign = '-' if frac.startswith('-') else ''
​
    if not n%d:
        return sign + str(n//d)
    n, r = divmod(n, d)
    return sign + '{} {}'.format(n, reduce_frac(r, d)).lstrip('0 ')

