
def widen_streets(lst, n):
    return list(map(lambda elm: elm.replace('   ',  ' _ ').replace(' ', ' '*n).replace('_', ' '), lst))

