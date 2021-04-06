
def product(lst):
    return (lambda a, b='n': a*a if b == 'n' else a*b)(*sorted(set(lst))[-2:])

