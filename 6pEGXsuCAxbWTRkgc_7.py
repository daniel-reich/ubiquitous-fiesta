
def loves_me(n):
    s = ('Loves me, Loves me not, ' * n).split(',')[:-n - 1]
    return (','.join(s[:-1]) + ',' + s[-1].upper()).strip(',')

